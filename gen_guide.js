const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageNumber, PageBreak, LevelFormat, ExternalHyperlink
} = require('docx');
const fs = require('fs');

// ── Colour palette ──────────────────────────────────────────────────────────
const NAVY     = "1A3A5C";
const BLUE     = "2E75B6";
const LIGHT_BG = "F0F6FB";
const CODE_BG  = "F2F2F2";
const WHITE    = "FFFFFF";
const GRAY     = "666666";
const TEXT     = "1A1A1A";
const ROW_ALT  = "F7FBFE";

// ── Page geometry (US Letter, 1.25" side margins) ───────────────────────────
const PAGE_W   = 12240;
const PAGE_H   = 15840;
const MARGIN_H = 1800;  // 1.25"
const MARGIN_V = 1440;  // 1"
const CONTENT  = PAGE_W - MARGIN_H * 2;  // 8640 DXA = 6"

// ── Border helpers ──────────────────────────────────────────────────────────
const thinBorder   = (c = "CCCCCC") => ({ style: BorderStyle.SINGLE, size: 1, color: c });
const thickBorder  = (c = BLUE)     => ({ style: BorderStyle.THICK,  size: 12, color: c });
const cellBorders  = { top: thinBorder(), bottom: thinBorder(), left: thinBorder(), right: thinBorder() };
const noBorder     = { style: BorderStyle.NONE, size: 0, color: WHITE };
const noBorders    = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

// ── Text run helpers ─────────────────────────────────────────────────────────
const r  = (text, opts = {}) => new TextRun({ text, font: "Arial",       size: 22, color: TEXT,  ...opts });
const rc = (text, opts = {}) => new TextRun({ text, font: "Courier New", size: 20, color: "1A1A1A", ...opts });
const rBlue = (text) => r(text, { color: BLUE });
const rBold = (text) => r(text, { bold: true });
const rCode = (text) => rc(text, { color: BLUE });  // inline code in body text

// ── Paragraph helpers ────────────────────────────────────────────────────────
const spacer = (before = 80, after = 80) =>
  new Paragraph({ spacing: { before, after }, children: [r("")] });

const h1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 140 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE, space: 6 } },
  children: [new TextRun({ text, font: "Arial", size: 30, bold: true, color: NAVY })]
});

const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 280, after: 80 },
  children: [new TextRun({ text, font: "Arial", size: 24, bold: true, color: BLUE })]
});

const body = (text, opts = {}) => new Paragraph({
  spacing: { before: 80, after: 80, line: 280 },
  children: [r(text, opts)]
});

const bodyRuns = (runs) => new Paragraph({
  spacing: { before: 80, after: 80, line: 280 },
  children: runs
});

const note = (text) => new Paragraph({
  spacing: { before: 120, after: 120 },
  indent: { left: 480 },
  border: { left: { style: BorderStyle.THICK, size: 14, color: BLUE, space: 10 } },
  shading: { fill: LIGHT_BG, type: ShadingType.CLEAR },
  children: [r(text, { italics: true, size: 20, color: "333333" })]
});

const bullet = (runs) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  spacing: { before: 50, after: 50 },
  children: Array.isArray(runs) ? runs : [r(runs)]
});

const numbered = (runs) => new Paragraph({
  numbering: { reference: "numbers", level: 0 },
  spacing: { before: 60, after: 60 },
  children: Array.isArray(runs) ? runs : [r(runs)]
});

// code block — a single-line block (call per line for multi-line)
const codeBlock = (text) => new Paragraph({
  spacing: { before: 2, after: 2 },
  indent: { left: 360, right: 360 },
  shading: { fill: CODE_BG, type: ShadingType.CLEAR },
  border: {
    top:    { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" },
    bottom: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" },
    left:   { style: BorderStyle.THICK,  size: 14, color: BLUE },
    right:  { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" },
  },
  children: [rc(text)]
});

// ── Table cell helpers ───────────────────────────────────────────────────────
const hdrCell = (text, width) => new TableCell({
  borders: cellBorders,
  width: { size: width, type: WidthType.DXA },
  shading: { fill: NAVY, type: ShadingType.CLEAR },
  margins: { top: 100, bottom: 100, left: 160, right: 160 },
  children: [new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 20, bold: true, color: WHITE })]
  })]
});

const bodyCell = (text, width, bg = WHITE, bold = false) => new TableCell({
  borders: cellBorders,
  width: { size: width, type: WidthType.DXA },
  shading: { fill: bg, type: ShadingType.CLEAR },
  margins: { top: 90, bottom: 90, left: 160, right: 160 },
  children: [new Paragraph({
    children: [new TextRun({ text, font: "Arial", size: 20, color: TEXT, bold })]
  })]
});

const codeCell = (text, width, bg = WHITE) => new TableCell({
  borders: cellBorders,
  width: { size: width, type: WidthType.DXA },
  shading: { fill: bg, type: ShadingType.CLEAR },
  margins: { top: 90, bottom: 90, left: 160, right: 160 },
  children: [new Paragraph({
    children: [rc(text)]
  })]
});

// ── Sub-bullet (indented, for nested lists) ──────────────────────────────────
const subBullet = (runs) => new Paragraph({
  numbering: { reference: "sub-bullets", level: 0 },
  spacing: { before: 40, after: 40 },
  children: Array.isArray(runs) ? runs : [r(runs)]
});

// ── Document ─────────────────────────────────────────────────────────────────
const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "–",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 600, hanging: 300 } } } }]
      },
      {
        reference: "numbers",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 600, hanging: 300 } } } }]
      },
      {
        reference: "sub-bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "◦",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1020, hanging: 300 } } } }]
      },
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22, color: TEXT } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 30, bold: true, font: "Arial", color: NAVY },
        paragraph: { spacing: { before: 400, after: 140 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: BLUE },
        paragraph: { spacing: { before: 280, after: 80 }, outlineLevel: 1 } },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H },
        margin: { top: MARGIN_V, right: MARGIN_H, bottom: MARGIN_V, left: MARGIN_H }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: BLUE, space: 4 } },
          spacing: { after: 0 },
          children: [
            new TextRun({ text: "Deploy Your Hugo Website  ", font: "Arial", size: 18, bold: true, color: NAVY }),
            new TextRun({ text: "pranoti.thesciencetalk.com", font: "Arial", size: 18, color: GRAY }),
          ]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          border: { top: { style: BorderStyle.SINGLE, size: 4, color: BLUE, space: 4 } },
          spacing: { before: 0 },
          alignment: AlignmentType.RIGHT,
          children: [
            new TextRun({ text: "Page ", font: "Arial", size: 18, color: GRAY }),
            new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 18, color: GRAY }),
            new TextRun({ text: " of ", font: "Arial", size: 18, color: GRAY }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 18, color: GRAY }),
          ]
        })]
      })
    },
    children: [

      // ════════════════════════════════════════════════════════════════
      // TITLE
      // ════════════════════════════════════════════════════════════════
      spacer(600, 200),
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 100 },
        children: [new TextRun({ text: "Deploy Your Hugo Website", font: "Arial", size: 60, bold: true, color: NAVY })]
      }),
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 80 },
        children: [new TextRun({ text: "Using Git, GitHub & Netlify", font: "Arial", size: 36, color: BLUE })]
      }),
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { before: 0, after: 500 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE, space: 10 } },
        children: [new TextRun({
          text: "A professional workflow guide for independent site owners",
          font: "Arial", size: 22, color: GRAY, italics: true
        })]
      }),
      spacer(200, 80),
      new Paragraph({
        spacing: { before: 0, after: 40 },
        children: [new TextRun({ text: "Pranoti Kshirsagar", font: "Arial", size: 24, bold: true, color: TEXT })]
      }),
      new Paragraph({
        spacing: { before: 0, after: 0 },
        children: [new TextRun({ text: "pranoti.thesciencetalk.com", font: "Arial", size: 22, color: BLUE })]
      }),

      new Paragraph({ spacing: { before: 0, after: 0 }, children: [new PageBreak()] }),

      // ════════════════════════════════════════════════════════════════
      // OVERVIEW
      // ════════════════════════════════════════════════════════════════
      h1("What You Will Achieve"),
      body("This guide walks you through connecting your Hugo site to a Git-based deployment pipeline. Once set up, every change you push from your Mac triggers an automatic rebuild and deploy on Netlify — no manual uploads, no drag-and-drop, no file management."),
      spacer(80, 40),
      body("By the end of this guide you will have:", { bold: true }),
      bullet("A private GitHub repository holding your complete site source"),
      bullet("Automatic deploys triggered by a single terminal command"),
      bullet("A local development environment that never affects your live site until you decide it does"),
      bullet("Full version history of every change you have ever published"),
      spacer(80, 40),
      note("Prerequisites: A Mac computer, a Hugo site folder, and an existing Netlify site. No prior experience with Git or the Terminal is required — every command in this guide is explained."),

      // ════════════════════════════════════════════════════════════════
      // HOW IT WORKS
      // ════════════════════════════════════════════════════════════════
      h1("Understanding the Pipeline"),
      body("Your deployment pipeline has three layers. Nothing moves between them until you explicitly run git push — your local edits, experiments, and drafts stay on your Mac until you choose to publish."),
      spacer(80, 120),

      new Table({
        width: { size: CONTENT, type: WidthType.DXA },
        columnWidths: [2400, 3840, 2400],
        rows: [
          new TableRow({ children: [hdrCell("Layer", 2400), hdrCell("Contents", 3840), hdrCell("Visibility", 2400)] }),
          new TableRow({ children: [bodyCell("Your Mac", 2400, WHITE, true), bodyCell("Everything — your full working sandbox", 3840), bodyCell("You only", 2400)] }),
          new TableRow({ children: [bodyCell("GitHub (private repo)", 2400, ROW_ALT, true), bodyCell("Only what you commit and push", 3840, ROW_ALT), bodyCell("You only", 2400, ROW_ALT)] }),
          new TableRow({ children: [bodyCell("Netlify (live site)", 2400, WHITE, true), bodyCell("Exactly what GitHub has", 3840), bodyCell("Public", 2400)] }),
        ]
      }),
      spacer(160, 80),

      // ════════════════════════════════════════════════════════════════
      // NETLIFY BUILD MINUTES
      // ════════════════════════════════════════════════════════════════
      h1("Netlify Build Minutes"),
      body("Netlify's free plan includes 300 build minutes per month. A build minute is consumed whenever Netlify runs your hugo command during a Git-triggered deploy. For a typical content site updated a few times per week, 300 minutes is more than sufficient."),
      spacer(80, 40),
      body("You can monitor usage at any time in your Netlify dashboard under Site settings → Build & deploy."),
      spacer(80, 40),
      note("The real advantage of Git-based deploys is version control, automation, and the ability to develop locally without touching your live site — not build minute savings."),

      // ════════════════════════════════════════════════════════════════
      // PHASE 1
      // ════════════════════════════════════════════════════════════════
      h1("Phase 1 — Create a GitHub Account"),
      numbered("Go to github.com and click Sign up"),
      numbered("Enter your email address, choose a username and password"),
      numbered("Verify your email when GitHub sends the confirmation link"),
      spacer(80, 40),
      note("Your username will appear in your repository URL. Choose something that represents you or your organisation."),

      // ════════════════════════════════════════════════════════════════
      // PHASE 2
      // ════════════════════════════════════════════════════════════════
      h1("Phase 2 — Install Git on Your Mac"),
      numbered("Open Terminal — press Cmd + Space, type Terminal, press Enter"),
      numbered("Run the following command:"),
      spacer(40, 0),
      codeBlock("git --version"),
      spacer(40, 0),
      numbered("If Git is not installed, macOS will prompt you to install it automatically — click Install and wait for it to complete"),
      numbered([r("Run "), rCode("git --version"), r(" again to confirm. You should see something like "), rCode("git version 2.x.x")]),
      spacer(80, 40),
      note("If the install prompt does not appear, visit git-scm.com/download/mac for manual installation instructions."),

      // ════════════════════════════════════════════════════════════════
      // PHASE 3
      // ════════════════════════════════════════════════════════════════
      h1("Phase 3 — Configure Git"),
      body("Run these two commands once, using the same email address as your GitHub account:"),
      spacer(60, 0),
      codeBlock('git config --global user.name "Your Full Name"'),
      codeBlock('git config --global user.email "your@email.com"'),
      spacer(60, 40),
      body("This is a one-time setup. Git uses this information to label every commit you make."),

      // ════════════════════════════════════════════════════════════════
      // PHASE 4
      // ════════════════════════════════════════════════════════════════
      h1("Phase 4 — Prepare Your Site Folder"),

      h2("Step 1 — Initialise Git"),
      body("Navigate to your Hugo site folder in Terminal and run:"),
      spacer(40, 0),
      codeBlock("git status"),
      spacer(40, 40),
      bullet([r("If you see "), rCode("On branch main"), r(" — Git is already initialised. Proceed to Step 2.")]),
      bullet([r("If you see "), rCode("not a git repository"), r(" — run "), rCode("git init"), r(" first.")]),

      h2("Step 2 — Create a .gitignore File"),
      body("A .gitignore file tells Git which files and folders to exclude from tracking. This keeps your repository clean and sensitive files off GitHub. Create it by running the following block as a single command:"),
      spacer(60, 0),
      codeBlock("cat > .gitignore << 'EOF'"),
      codeBlock("public/"),
      codeBlock(".DS_Store"),
      codeBlock(".netlify/"),
      codeBlock(".hugo_build.lock"),
      codeBlock(".trash/"),
      codeBlock(".claude/"),
      codeBlock("resources/_gen/"),
      codeBlock("EOF"),
      spacer(60, 40),
      bodyRuns([r("Verify with "), rCode("cat .gitignore"), r(" — you should see all entries printed back.")]),
      spacer(80, 40),
      note("Themes folder: Only exclude themes/ if your theme is managed via Hugo Modules (go.mod). If your theme is a local folder inside your site directory, do not add themes/ to .gitignore — Netlify needs it present to build your site."),
      spacer(60, 40),
      note("Private files: If you have work-in-progress documents, client files, or anything you want to keep off GitHub, add those paths to .gitignore now — before running git add in the next step."),

      h2("Step 3 — Stage and Commit Your Files"),
      body("Run the following commands one at a time:"),
      spacer(40, 0),
      codeBlock("git add ."),
      codeBlock("git status"),
      spacer(40, 40),
      bodyRuns([r("Review the file list carefully. You should "), r("not", { bold: true }), r(" see "), rCode("public/"), r(", "), rCode(".DS_Store"), r(", or "), rCode(".netlify/"), r(". Once satisfied:")]),
      spacer(40, 0),
      codeBlock('git commit -m "initial commit"'),

      // ════════════════════════════════════════════════════════════════
      // PHASE 5
      // ════════════════════════════════════════════════════════════════
      h1("Phase 5 — Create a Private GitHub Repository"),
      numbered("Go to github.com/new"),
      numbered("Give it a name — for example pranoti-website"),
      numbered([r("Set visibility to "), r("Private", { bold: true })]),
      numbered("Leave all initialise options unticked — no README, no .gitignore"),
      numbered("Click Create repository"),
      spacer(80, 40),
      body("GitHub will show a setup page. Copy the two lines under or push an existing repository from the command line:"),
      spacer(40, 0),
      codeBlock("git remote add origin https://github.com/YOUR-USERNAME/your-repo.git"),
      codeBlock("git push -u origin main"),
      spacer(80, 40),
      note("Branch name: Run git branch to check your local branch name. If it is master rather than main, replace main with master in the push command above."),

      h2("Authenticating with a Personal Access Token"),
      body("When Terminal prompts for your password, your GitHub account password will not work. You need a Personal Access Token."),
      spacer(60, 40),
      numbered("Go to github.com/settings/tokens/new"),
      numbered("Name it — for example my-mac"),
      numbered("Set expiration to 90 days"),
      numbered([r("Tick only the "), r("repo", { bold: true }), r(" scope checkbox")]),
      numbered("Click Generate token"),
      numbered("Copy it immediately — GitHub displays it only once"),
      spacer(80, 40),
      body("When Terminal asks for your password, paste the token. Your username is your GitHub username."),
      spacer(80, 40),
      note("macOS credential caching: After your first successful push, macOS stores the token in Keychain automatically — future pushes will not prompt you again. When your token expires and you generate a new one, open Keychain Access, search for github.com, delete the old entry, then push again with the new token."),

      // ════════════════════════════════════════════════════════════════
      // PHASE 6
      // ════════════════════════════════════════════════════════════════
      h1("Phase 6 — Connect Netlify to GitHub"),
      numbered("Go to your Netlify dashboard at app.netlify.com"),
      numbered("Open your site, then go to Site configuration → Build and deploy → Link repository"),
      numbered("Select GitHub and authorise access"),
      numbered("Choose your repository from the list"),
      numbered("Confirm the build settings — Netlify auto-detects these from your netlify.toml:"),
      spacer(40, 0),
      subBullet([r("Build command: "), rCode("hugo --environment production")]),
      subBullet([r("Publish directory: "), rCode("public")]),
      subBullet([r("Branch: "), rCode("main")]),
      spacer(40, 40),
      numbered([r("Click "), r("Deploy site", { bold: true })]),
      spacer(80, 40),
      body("Netlify runs its first build. The deploy log will show green Complete indicators at each stage when successful. This typically takes 10 to 30 seconds."),
      spacer(80, 40),
      note("If the build fails, check the deploy log. The most common cause is a Hugo version mismatch — see the Troubleshooting section at the end of this guide."),

      new Paragraph({ spacing: { before: 0, after: 0 }, children: [new PageBreak()] }),

      // ════════════════════════════════════════════════════════════════
      // DAILY WORKFLOW
      // ════════════════════════════════════════════════════════════════
      h1("Your Daily Workflow"),
      body("From this point, publishing any change to your live site is three commands:"),
      spacer(60, 0),
      codeBlock("git add ."),
      codeBlock('git commit -m "describe what changed"'),
      codeBlock("git push"),
      spacer(60, 40),
      body("Netlify detects the push and rebuilds your site automatically. No manual steps required."),

      h2("Deploying a Single File"),
      body("To publish one specific change without staging everything else:"),
      spacer(40, 0),
      codeBlock("git add content/portfolio/events/new-event.md"),
      codeBlock('git commit -m "add new speaking event"'),
      codeBlock("git push"),

      h2("Previewing Locally Without Publishing"),
      body("Your Mac is your sandbox. Edit files freely and preview in the browser — nothing reaches GitHub or Netlify until you run git push."),
      spacer(40, 0),
      codeBlock("hugo server"),
      spacer(40, 40),
      bodyRuns([r("Open "), rCode("http://localhost:1313"), r(" in your browser. Changes appear in real time as you save files.")]),

      h2("Quick Reference"),
      spacer(40, 100),

      new Table({
        width: { size: CONTENT, type: WidthType.DXA },
        columnWidths: [3040, 5600],
        rows: [
          new TableRow({ children: [hdrCell("Task", 3040), hdrCell("Command", 5600)] }),
          new TableRow({ children: [bodyCell("Preview locally",        3040),         codeCell("hugo server",                    5600)] }),
          new TableRow({ children: [bodyCell("Check what has changed", 3040, ROW_ALT), codeCell("git status",                   5600, ROW_ALT)] }),
          new TableRow({ children: [bodyCell("Stage all changes",      3040),         codeCell("git add .",                     5600)] }),
          new TableRow({ children: [bodyCell("Stage one file",         3040, ROW_ALT), codeCell("git add path/to/file.md",      5600, ROW_ALT)] }),
          new TableRow({ children: [bodyCell("Commit",                 3040),         codeCell('git commit -m "your message"',  5600)] }),
          new TableRow({ children: [bodyCell("Deploy",                 3040, ROW_ALT), codeCell("git push",                    5600, ROW_ALT)] }),
        ]
      }),
      spacer(160, 80),

      // ════════════════════════════════════════════════════════════════
      // SECURITY
      // ════════════════════════════════════════════════════════════════
      h1("Keeping Your Token Secure"),
      body("Your Personal Access Token grants write access to your GitHub repository. Treat it as a credential."),
      spacer(80, 40),
      bullet("Store it in a password manager — not in a plain text file or desktop note"),
      bullet("Never commit it to your repository or include it in any document you share"),
      bullet("Set a 90-day expiry — GitHub will email you a reminder before it lapses"),
      bullet("If compromised, revoke it immediately at github.com/settings/tokens and generate a replacement"),

      // ════════════════════════════════════════════════════════════════
      // TROUBLESHOOTING
      // ════════════════════════════════════════════════════════════════
      h1("Troubleshooting"),
      spacer(40, 100),

      new Table({
        width: { size: CONTENT, type: WidthType.DXA },
        columnWidths: [2760, 5880],
        rows: [
          new TableRow({ children: [hdrCell("Issue", 2760), hdrCell("Resolution", 5880)] }),
          new TableRow({ children: [
            bodyCell("Authentication failed", 2760, WHITE, true),
            bodyCell("You used your GitHub account password. Go to github.com/settings/tokens, generate a Personal Access Token with repo scope, and use that as your password in Terminal.", 5880)
          ]}),
          new TableRow({ children: [
            bodyCell("Auth fails after renewing token", 2760, ROW_ALT, true),
            bodyCell("macOS cached your old token in Keychain. Open Keychain Access, search for github.com, delete the entry, then push again.", 5880, ROW_ALT)
          ]}),
          new TableRow({ children: [
            bodyCell("error: remote origin already exists", 2760, WHITE, true),
            bodyCell("Run git remote remove origin, then re-add with: git remote add origin https://github.com/USERNAME/repo.git", 5880)
          ]}),
          new TableRow({ children: [
            bodyCell("Netlify Hugo version error", 2760, ROW_ALT, true),
            bodyCell("Add HUGO_VERSION = \"0.139.0\" under [build.environment] in your netlify.toml. Replace the version number with the output of hugo version on your Mac.", 5880, ROW_ALT)
          ]}),
          new TableRow({ children: [
            bodyCell("Changes not on live site", 2760, WHITE, true),
            bodyCell("Confirm you ran all three commands: git add, git commit, and git push. Then check the Netlify deploy log for build errors.", 5880)
          ]}),
          new TableRow({ children: [
            bodyCell("Excluded file still on GitHub", 2760, ROW_ALT, true),
            bodyCell(".gitignore only prevents future tracking. To remove an already-committed file (without deleting it locally): git rm --cached path/to/file, then commit.", 5880, ROW_ALT)
          ]}),
        ]
      }),

      // ════════════════════════════════════════════════════════════════
      // CLOSING
      // ════════════════════════════════════════════════════════════════
      spacer(400, 0),
      new Paragraph({
        spacing: { before: 200, after: 200 },
        border: {
          top:    { style: BorderStyle.SINGLE, size: 6, color: BLUE, space: 8 },
          bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE, space: 8 },
        },
        shading: { fill: LIGHT_BG, type: ShadingType.CLEAR },
        indent: { left: 240, right: 240 },
        children: [r("You now have a professional deployment workflow. Your site is version-controlled, your private files stay private, and every push to GitHub deploys automatically.", { size: 22, italics: true })]
      }),
      spacer(120, 80),
      body("If you found this guide useful, share it with a fellow researcher or science communicator who manages their own site."),
      spacer(80, 40),
      bodyRuns([
        r("More guides and resources: ", { bold: true }),
        r("pranoti.thesciencetalk.com", { color: BLUE })
      ]),
    ]
  }]
});

const OUT = "/Users/pranotikshirsagar/Documents/CLAUDE/Product/Pranoti_Website/Git-Deploy-Guide-Pranoti.docx";
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(OUT, buf);
  console.log("Written:", OUT);
});
