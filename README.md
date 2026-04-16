# Pranoti Kshirsagar - Personal Website

A modern, clean static website built with Hugo, inspired by Maisie Hill's design aesthetic.

## 🚀 Quick Start

### Prerequisites
- Hugo (v0.120.0 or later)
- Git

### Installation

1. Install Hugo:
```bash
brew install hugo  # macOS
# or
sudo apt-get install hugo  # Ubuntu/Debian
```

2. Run development server:
```bash
cd pranoti-site
hugo server -D
```

3. Build for production:
```bash
hugo --minify
```

## 📁 Project Structure

```
pranoti-site/
├── archetypes/       # Content templates
├── assets/           
│   ├── css/         # Stylesheets
│   ├── js/          # JavaScript
│   └── fonts/       # Custom fonts
├── content/         # Markdown content
│   ├── about/       
│   ├── services/    
│   ├── blog/        
│   └── resources/   
├── data/            # Data files (JSON/YAML)
├── layouts/         
│   ├── _default/    # Base templates
│   ├── partials/    # Reusable components
│   └── shortcodes/  # Custom shortcodes
├── static/          
│   ├── images/      # Images
│   └── icons/       # Icons
├── themes/          # Hugo themes (if any)
└── hugo.toml        # Site configuration
```

## 🎨 Design System

### Colors (Maisie Hill Inspired)
- Primary Red: `#E74C3C`
- Secondary Green: `#27AE60`
- Dark Grey: `#2C3E50`
- Light Grey: `#95A5A6`
- Off White: `#FAF9F7`

### Typography
- Display: Playfair Display
- Body: Inter

## 🔧 Configuration

Edit `hugo.toml` to update:
- Site title and description
- Menu items
- Social media links
- Base URL

## 📝 Adding Content

Create new pages:
```bash
hugo new services/podcast-production.md
hugo new blog/my-first-post.md
```

## 🚢 Deployment

The site can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

## 📄 License

© 2024 Pranoti Kshirsagar. All rights reserved.
