#!/usr/bin/env python3
"""Creates all shorts portfolio pages. Run once, then delete this script."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

pages = {
"sebastian-maehrlein.md": """---
title: "Under the Microscope Shorts — Sebastian Maehrlein"
date: 2021-08-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Sebastian Maehrlein."
client: "Sebastian Maehrlein"
youtube_urls:
  - "https://youtu.be/Nm_MPQumLJc"
youtube_full: "https://youtu.be/KSapufbXvN8"
spotify: "https://open.spotify.com/episode/66gvhmmHNfXrKX7ywyToKa?si=hVv9R8iLSWOhFJyPIVljig"
tags: ["podcast shorts", "S3"]
category: "shorts"
---
""",
"tiffany-harte.md": """---
title: "Under the Microscope Shorts — Tiffany Harte"
date: 2021-12-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Tiffany Harte."
client: "Tiffany Harte"
youtube_urls:
  - "https://youtu.be/awocFppW5lw"
  - "https://youtu.be/VI7wYkx3xVc"
  - "https://youtu.be/W2BBAqqLIZA"
  - "https://youtu.be/IHoESrX5WVM"
  - "https://youtu.be/JOlsXNe5GlQ"
youtube_full: "https://youtu.be/QYw7KK04a40"
spotify: "https://open.spotify.com/episode/5O0iAAXNjAn8yIW29NEzFP?si=3MUp8pT7SBS1WuwVjYsdPw"
tags: ["podcast shorts", "S3"]
category: "shorts"
---
""",
"susi-seibt.md": """---
title: "Under the Microscope Shorts — Susi Seibt"
date: 2022-07-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Susi Seibt."
client: "Susi Seibt"
youtube_urls:
  - "https://youtu.be/9z9aq-YMlo0"
  - "https://youtu.be/ItNre86wOww"
youtube_full: "https://youtu.be/wCFs1I9qxyM"
spotify: "https://open.spotify.com/episode/6W4Cd0qNSPzHXWy264YlJD?si=xLiZ-UTkSIuVB8sHVfL4SQ"
tags: ["podcast shorts", "S4"]
category: "shorts"
---
""",
"rebecca-katharina-pittkowski.md": """---
title: "Under the Microscope Shorts — Rebecca Katharina Pittkowski"
date: 2022-08-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Rebecca Katharina Pittkowski."
client: "Rebecca Katharina Pittkowski"
youtube_urls:
  - "https://youtu.be/7R72Wof0APE"
youtube_full: "https://youtu.be/y7DKnTuZv3Q"
spotify: "https://open.spotify.com/episode/1LMMA1y7uZ48cctMgkjEXG?si=VDVY-I-FTg-i_Izy3H-dvw"
tags: ["podcast shorts", "S4"]
category: "shorts"
---
""",
"andy-soder-anke.md": """---
title: "Under the Microscope Shorts — Andy Soder Anke"
date: 2022-09-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Andy Soder Anke."
client: "Andy Soder Anke"
youtube_urls:
  - "https://youtu.be/PbaUPanAwd0"
youtube_full: "https://youtu.be/2ESNmFdQdas"
spotify: "https://open.spotify.com/episode/3NJkdcHpQo1yb5OFwNLAw4?si=hjyhTjoRTv62nagfWZQGxw"
tags: ["podcast shorts", "S4"]
category: "shorts"
---
""",
"claire-dancer.md": """---
title: "Under the Microscope Shorts — Claire Dancer"
date: 2022-09-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Claire Dancer."
client: "Claire Dancer"
youtube_urls:
  - "https://youtu.be/1jXCug8DBOU"
  - "https://youtu.be/Pk26-KINdxc"
youtube_full: "https://youtu.be/O4OnP-0ZTCQ"
spotify: "https://open.spotify.com/episode/56F5Wc6mrw4IGOvItBV1xd?si=gXDwUPlMR-OJHFvxlezqfw"
tags: ["podcast shorts", "S4"]
category: "shorts"
---
""",
"lisa-mcelwee-white.md": """---
title: "Under the Microscope Shorts — Lisa McElwee-White"
date: 2023-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Lisa McElwee-White."
client: "Lisa McElwee-White"
youtube_urls:
  - "https://youtu.be/xM5w69ogCVo"
youtube_full: "https://youtu.be/sgQR7_5o-w0"
spotify: "https://open.spotify.com/episode/7pZU7GKZPB5etscoFvqmi6?si=TxlWgimxSmeqNydvlxSEDA"
tags: ["podcast shorts", "S5"]
category: "shorts"
---
""",
"george-mihailescu.md": """---
title: "Under the Microscope Shorts — George Mihailescu"
date: 2023-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with George Mihailescu."
client: "George Mihailescu"
youtube_urls:
  - "https://youtu.be/qtZRCzQ9rlU"
  - "https://youtu.be/_cKvg_bAipk"
  - "https://youtu.be/27H89TS7nh0"
youtube_full: "https://youtu.be/Uva_wgzlhC0"
spotify: "https://open.spotify.com/episode/6Vtpto6t6ZLwLgwRoGLrnx?si=LfMHii-1QQqShScPAdrmAw"
tags: ["podcast shorts", "S5"]
category: "shorts"
---
""",
"julio-terra.md": """---
title: "Under the Microscope Shorts — Julio Terra"
date: 2023-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Julio Terra."
client: "Julio Terra"
youtube_urls:
  - "https://youtu.be/FBZAWXxUGzk"
  - "https://youtu.be/RhtT2eCg5Zw"
youtube_full: "https://youtu.be/PDw6mArpL3A"
spotify: "https://open.spotify.com/episode/6nZdLQEBCDD9YXncCV7H2D?si=S9-CBipBRUmjoUCgUPWEHQ"
tags: ["podcast shorts", "S5"]
category: "shorts"
---
""",
"jodie-bradby.md": """---
title: "Under the Microscope Shorts — Jodie Bradby"
date: 2023-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Jodie Bradby."
client: "Jodie Bradby"
youtube_urls:
  - "https://youtu.be/dEuWJJgkMRM"
  - "https://youtu.be/j6sAnFCVWOQ"
youtube_full: "https://youtu.be/ZxOGF99jKTw"
spotify: "https://open.spotify.com/episode/7G4wlBXm4kx2u2TaAnXuMs?si=-ymgn0SzRtGBWl76sMeH1g"
tags: ["podcast shorts", "S5"]
category: "shorts"
---
""",
"steven-street.md": """---
title: "Under the Microscope Shorts — Steven Street"
date: 2023-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Steven Street."
client: "Steven Street"
youtube_urls:
  - "https://youtu.be/F5JEztKoYYs"
  - "https://youtu.be/6y0h-KFUFdo"
youtube_full: "https://youtu.be/F5JEztKoYYs"
spotify: "https://open.spotify.com/episode/4DKD950QE8czJz3dz9vMCm?si=qdYlnHQ3Qn6dhS5Zk9Bnag"
tags: ["podcast shorts", "S5"]
category: "shorts"
---
""",
"antonio-manesco.md": """---
title: "Under the Microscope Shorts — Antonio Manesco"
date: 2023-03-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Antonio Manesco."
client: "Antonio Manesco"
youtube_urls:
  - "https://youtu.be/IAmmudOU_C8"
  - "https://youtu.be/NYFpDtZ4C_k"
youtube_full: "https://youtu.be/ugeBfchs6HQ"
spotify: "https://open.spotify.com/episode/6VM0K5UBTpedHmzJEKIj7X?si=ALPexPizThG3G8X4DZTZFw"
tags: ["podcast shorts", "S5"]
category: "shorts"
---
""",
"doris-reiter.md": """---
title: "Under the Microscope Shorts — Doris Reiter"
date: 2024-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Doris Reiter."
client: "Doris Reiter"
youtube_urls:
  - "https://youtu.be/GA1Cy2O3bU4"
  - "https://youtu.be/wkBBe937S_g"
  - "https://youtu.be/5nKucChY8ew"
  - "https://youtu.be/oXgXbxNjsXE"
  - "https://youtu.be/7C0yPxKrmm4"
  - "https://youtu.be/TPfo4vPIqdo"
  - "https://youtu.be/WQHG6mF1_HA"
  - "https://youtu.be/vIKweIeqcVA"
  - "https://youtu.be/P0OixIboItU"
youtube_full: "https://youtu.be/2024"
spotify: "https://open.spotify.com/episode/5AyHb676TAniPi1jrIiOh7?si=dkweNetsQnW9AW9v_N9x7w"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"narayanan-t-n.md": """---
title: "Under the Microscope Shorts — Narayanan T N"
date: 2024-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Narayanan T N."
client: "Narayanan T N"
youtube_urls:
  - "https://youtu.be/Qulf8uxCtDI"
  - "https://youtu.be/x--b2F9zsv8"
  - "https://youtu.be/_Ioj-aPdo10"
youtube_full: "https://youtu.be/LraKZrZ7x1w"
spotify: "https://open.spotify.com/episode/1wft5SfflZjcZuKTM1WIo8?si=yUkfBETuSvyR1oVF8BCABA"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"tobias-heindel.md": """---
title: "Under the Microscope Shorts — Tobias Heindel"
date: 2024-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Tobias Heindel."
client: "Tobias Heindel"
youtube_urls:
  - "https://youtu.be/wCe6v5Vb07w"
  - "https://youtu.be/BLd1UDfHxAA"
  - "https://youtu.be/juGTGtIfE7s"
  - "https://youtu.be/YZVjZqX8le8"
  - "https://youtu.be/x2GCpQMMIxU"
youtube_full: "https://youtu.be/AuyXDkBT4KE"
spotify: "https://open.spotify.com/episode/6xJJQV9DNPe2Xpv9iNEJEP?si=Dc0Bl9JnSjaRoK0JzhrPag"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"armando-rastelli.md": """---
title: "Under the Microscope Shorts — Armando Rastelli"
date: 2024-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Armando Rastelli."
client: "Armando Rastelli"
youtube_urls:
  - "https://youtu.be/08qhoUjQBxk"
  - "https://youtu.be/EtPfH3Lu5jg"
  - "https://youtu.be/ccMIbfmDsIQ"
  - "https://youtu.be/14wlSIjgncA"
  - "https://youtu.be/obHb9fT563U"
youtube_full: "https://youtu.be/vZyh5O3FWQw"
spotify: "https://open.spotify.com/episode/1WlfWglXVsOmO39oVdUx4A?si=o78tNrvORveMToNR-yJQoQ"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"rinaldo-trotta.md": """---
title: "Under the Microscope Shorts — Rinaldo Trotta"
date: 2024-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Rinaldo Trotta."
client: "Rinaldo Trotta"
youtube_urls:
  - "https://youtu.be/k3wEjTwwgeY"
youtube_full: "https://youtu.be/A-LxrvuNwm8"
spotify: "https://open.spotify.com/episode/7FWlPNJsMI5AP40dE8n1cZ?si=A8GCnjsCR8C13BoyMAjHbg"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"jens-osterhoff.md": """---
title: "Under the Microscope Shorts — Jens Osterhoff"
date: 2024-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Jens Osterhoff."
client: "Jens Osterhoff"
youtube_urls:
  - "https://youtu.be/vP0hOCxaV7w"
  - "https://youtu.be/ETMx79Y4G5Q"
  - "https://youtu.be/4dLHOiAjiRA"
  - "https://youtu.be/OcszGUt6kIo"
  - "https://youtu.be/XulFPfj2w5k"
  - "https://youtu.be/GjOVraPuSmY"
  - "https://youtu.be/T0J1zraQy8g"
  - "https://youtu.be/XuCGLvXG6e0"
youtube_full: "https://youtu.be/tXXueCEZVqw"
spotify: "https://open.spotify.com/episode/65WXqmCxwXQ2u8Cd9OxymW?si=HIWsUzKRTH22RQfXN62ZrA"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"carlos-anton-solanas.md": """---
title: "Under the Microscope Shorts — Carlos Anton Solanas"
date: 2024-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Carlos Anton Solanas."
client: "Carlos Anton Solanas"
youtube_urls:
  - "https://youtu.be/46FFPzEmnxw"
  - "https://youtu.be/lkt3871lcrg"
  - "https://youtu.be/01JhC2xc5ws"
  - "https://youtu.be/qeffOuqBMqo"
  - "https://youtu.be/RIFueDxIC-s"
youtube_full: "https://youtu.be/Jtp48ChGNyA"
spotify: "https://open.spotify.com/episode/7bLMmutTW1PCDtNmAUargV?si=Ijy1XOamTu6ENjkwdWCvWg"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"pascale-senellart.md": """---
title: "Under the Microscope Shorts — Pascale Senellart"
date: 2024-03-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Pascale Senellart."
client: "Pascale Senellart"
youtube_urls:
  - "https://youtu.be/VXUuddezJck"
  - "https://youtu.be/TeLed2xfEAg"
  - "https://youtu.be/Py4pWn8O9dw"
  - "https://youtu.be/Dvu_cC9sKD8"
  - "https://youtu.be/EQpBvnkAnSw"
  - "https://youtu.be/fChd682RMXc"
  - "https://youtu.be/LOojX5bUMP4"
  - "https://youtu.be/kNqhZIiecDo"
youtube_full: "https://youtu.be/Lc4K2DJXzSw"
spotify: "https://open.spotify.com/episode/4GXOsLLpH6KodDDJDH0eIr?si=Fj9-wg-oTky2_R7YvOeA7A"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"mete-atature.md": """---
title: "Under the Microscope Shorts — Mete Atature"
date: 2024-03-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Mete Atature."
client: "Mete Atature"
youtube_urls:
  - "https://youtu.be/Vu_2Cxfck60"
  - "https://youtu.be/aBvAI-MVN0c"
  - "https://youtu.be/XdQEQOwS_lQ"
  - "https://youtu.be/ulJzuCoUjWc"
  - "https://youtu.be/hg_czu60lZs"
  - "https://youtu.be/wjg8fazv1Jk"
  - "https://youtu.be/r4n4IUplNGA"
  - "https://youtu.be/y83LRYBlc6Y"
youtube_full: "https://youtu.be/KUm6S7_RSPU"
spotify: "https://open.spotify.com/episode/4n7b8ZfkAGGiiGc7J5Vfye?si=Cm4iXXtATJ-mbeD0r8HItQ"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"francesca-calegari.md": """---
title: "Under the Microscope Shorts — Francesca Calegari"
date: 2024-03-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Francesca Calegari."
client: "Francesca Calegari"
youtube_urls:
  - "https://youtu.be/k1IAZqc8ev8"
  - "https://youtu.be/Cbx_klc8fU0"
  - "https://youtu.be/PbGkfQHV2SM"
  - "https://youtu.be/HWlfjDr16tE"
youtube_full: "https://youtu.be/dmaA6mwSJXI"
spotify: "https://open.spotify.com/episode/6S2PY64OACEqk0iPPckL8y?si=eGJ4qw1PT-GflPcOnhK8nA"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"emanuele-pelucchi.md": """---
title: "Under the Microscope Shorts — Emanuele Pelucchi"
date: 2024-03-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Emanuele Pelucchi."
client: "Emanuele Pelucchi"
youtube_urls:
  - "https://youtu.be/uqRjL0RQB8E"
  - "https://youtu.be/reBkMMV4KYU"
  - "https://youtu.be/cM8Mjnc19ro"
youtube_full: "https://youtu.be/nIkOBfUGycg"
spotify: "https://open.spotify.com/episode/6W1sLcIvrT67ScCXFw15kc?si=D_glXRAMQcqmYmQjOEURZA"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"elisa-riedo.md": """---
title: "Under the Microscope Shorts — Elisa Riedo"
date: 2024-04-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Elisa Riedo."
client: "Elisa Riedo"
youtube_urls:
  - "https://youtu.be/G1RiSMhQcPc"
  - "https://youtu.be/HYtsXu2pOUo"
  - "https://youtu.be/j8Nwt5QfQbg"
  - "https://youtu.be/no4YDZXdRLs"
youtube_full: "https://youtu.be/S6k9Bw0XmxI"
spotify: "https://open.spotify.com/episode/6OMI2G1XjwkaQQIewaDlvy?si=8H6F2pz5QU6jLExlAaDtUA"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"brian-gerardot.md": """---
title: "Under the Microscope Shorts — Brian Gerardot"
date: 2024-04-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Brian Gerardot."
client: "Brian Gerardot"
youtube_urls:
  - "https://youtu.be/_rdo3LhRafY"
  - "https://youtu.be/r72G1yFcJSo"
  - "https://youtu.be/ksrKuen499g"
youtube_full: "https://youtu.be/6GbR_X6_yJQ"
spotify: "https://open.spotify.com/episode/6vLLgU6sqWo4ZcIwT7mQWr?si=yvSFJ-DwTyq8565XGD57RQ"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"wolfgang-loeffler.md": """---
title: "Under the Microscope Shorts — Wolfgang Loeffler"
date: 2024-04-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Wolfgang Loeffler."
client: "Wolfgang Loeffler"
youtube_urls:
  - "https://youtu.be/WYFiWwpsNl4"
  - "https://youtu.be/0BzMV3AdPok"
youtube_full: "https://youtu.be/ak9WHrumboI"
spotify: "https://open.spotify.com/episode/7K0GHsIWA8Y6p36aI9cHrw?si=QeMvGcrBRpOUwi5JPlKq9g"
tags: ["podcast shorts", "S6"]
category: "shorts"
---
""",
"anna-musial.md": """---
title: "Under the Microscope Shorts — Anna Musial"
date: 2025-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Anna Musial."
client: "Anna Musial"
youtube_urls:
  - "https://youtu.be/tEJTAcmVoD4"
youtube_full: "https://youtu.be/MVkOnro3gyw"
spotify: "https://open.spotify.com/episode/2j4gsyvidqPOaEl7BYvmGf?si=puq5108QSC-_2JtmKYKFiw"
tags: ["podcast shorts", "S7"]
category: "shorts"
---
""",
"martin-rejhon.md": """---
title: "Under the Microscope Shorts — Martin Rejhon"
date: 2025-01-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Martin Rejhon."
client: "Martin Rejhon"
youtube_urls:
  - "https://youtu.be/O9Yawq3p1KM"
  - "https://youtu.be/gpnB3TsEIDM"
youtube_full: "https://youtu.be/KkRwgiVHAHM"
spotify: "https://open.spotify.com/episode/7KgwzIGjXiU2i7zUkImQna?si=-kJCHxDXRTWCsP9BiCbZOQ"
tags: ["podcast shorts", "S7"]
category: "shorts"
---
""",
"krist-v-gerneay.md": """---
title: "Under the Microscope Shorts — Krist V. Gerneay"
date: 2025-02-01
draft: false
type: "portfolio/shorts"
description: "Short clips from the Under the Microscope podcast with Krist V. Gerneay."
client: "Krist V. Gerneay"
youtube_urls:
  - "https://youtu.be/jI4t_I3gz3E"
  - "https://youtu.be/D3UsG5nqblU"
youtube_full: "https://youtu.be/obihbtvzCss"
spotify: "https://open.spotify.com/episode/1XOlKQksRk7hGE3DBmcRO8?si=iMK2KpeAREONY56Pzl-ZWA"
tags: ["podcast shorts", "S7"]
category: "shorts"
---
""",
}

count = 0
for filename, content in pages.items():
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(content)
        count += 1
        print(f"Created: {filename}")
    else:
        print(f"Skipped (exists): {filename}")

print(f"\nDone: {count} new files created")
