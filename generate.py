"""Generates dark_mode.svg: a neofetch-style profile card with live GitHub stats."""
import os, html, json, urllib.request
from datetime import date

# ---------- EDIT THESE ----------
USER = "Sekomane"
CODING_SINCE = date(2021, 1, 1)   # <- change to when you started coding
# --------------------------------

TOKEN = os.environ.get("GITHUB_TOKEN")
CW, LH, PAD = 9.0, 20, 30          # char width, line height, padding
INFO_COLS = 70

ART_RAW = [
    ".-----------------------------.",
    "| o o o                       |",
    "| $ whoami                    |",
    "| > rorisang_sekomane         |",
    "| $ ./build --reliable        |",
    "| compiling...      [#####] OK|",
    "| $ run tests                 |",
    "| 128 passed, 0 failed        |",
    "| $ _                         |",
    "'-----------------------------'",
    "",
    "      ____   ____",
    "     |  _ \\ / ___|",
    "     | |_) |\\___ \\",
    "     |  _ <  ___) |",
    "     |_| \\_\\|____/",
    "",
    "   < Full-Stack />  { Backend }",
    "   [ Data ]  ( Cloud )  # Java",
]
ART_W = max(len(l) for l in ART_RAW)
ART = [l.ljust(ART_W) for l in ART_RAW]


def api(path):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "readme-gen"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=h), timeout=20) as r:
        return json.load(r)


def stats():
    try:
        u = api(f"/users/{USER}")
        stars, page = 0, 1
        while True:
            repos = api(f"/users/{USER}/repos?per_page=100&page={page}&type=owner")
            if not repos:
                break
            stars += sum(r["stargazers_count"] for r in repos)
            page += 1
        commits = api(f"/search/commits?q=author:{USER}&per_page=1")["total_count"]
        return {"Repos": u["public_repos"], "Stars": stars, "Followers": u["followers"], "Commits": f"{commits:,}"}
    except Exception as e:
        print("Could not fetch stats:", e)
        return {"Repos": "--", "Stars": "--", "Followers": "--", "Commits": "--"}


def uptime():
    t, s = date.today(), CODING_SINCE
    y, m, d = t.year - s.year, t.month - s.month, t.day - s.day
    if d < 0: m, d = m - 1, d + 30
    if m < 0: y, m = y - 1, m + 12
    return f"{y} years, {m} months, {d} days"


s = stats()
ROWS = [
    ("head", "rorisang@sekomane"),
    ("row", "OS", "Windows, Linux"),
    ("row", "Uptime", uptime()),
    ("row", "Host", "Software Engineering"),
    ("row", "Kernel", "Full-Stack & Backend Developer"),
    ("row", "IDE", "IntelliJ IDEA, VS Code, Android Studio"),
    ("blank",),
    ("row", "Languages.Programming", "Java, C#, Python, PHP, JS, TS, Kotlin"),
    ("row", "Languages.Frameworks", "React, Angular, .NET, Django, Flask"),
    ("row", "Languages.Data", "SQL, PostgreSQL, MySQL"),
    ("row", "Languages.Real", "English"),
    ("blank",),
    ("row", "Data.Analytics", "Pandas, NumPy, scikit-learn, Power BI"),
    ("row", "Cloud.DevOps", "AWS, Docker, GitHub Actions, Firebase"),
    ("blank",),
    ("head", "Contact"),
    ("row", "Email.Personal", "sekomanerorisang904@gmail.com"),
    ("row", "LinkedIn", "rorisang-sekomane"),
    ("row", "GitHub", USER),
    ("blank",),
    ("head", "GitHub Stats"),
    ("row", "Repos", str(s["Repos"])),
    ("row", "Stars", str(s["Stars"])),
    ("row", "Followers", str(s["Followers"])),
    ("row", "Commits", str(s["Commits"])),
]

E = html.escape
x_info = PAD + ART_W * CW + PAD
width = int(x_info + INFO_COLS * CW + PAD)
n = max(len(ART), len(ROWS))
height = (n + 2) * LH + PAD

out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
       '<style>text{font-family:"Consolas","DejaVu Sans Mono","Courier New",monospace;font-size:15px;white-space:pre}'
       '.k{fill:#ffa657}.v{fill:#a5d6ff}.d{fill:#616e7c}.h{fill:#e6edf3}.a{fill:#c9d1d9}</style>',
       f'<rect width="{width}" height="{height}" rx="14" fill="#161b22"/>']

for i, line in enumerate(ART):
    y = PAD + (i + 1) * LH
    out.append(f'<text x="{PAD}" y="{y}" class="a" xml:space="preserve" textLength="{ART_W*CW}" lengthAdjust="spacingAndGlyphs">{E(line)}</text>')

for i, r in enumerate(ROWS):
    y = PAD + (i + 1) * LH
    if r[0] == "blank":
        continue
    if r[0] == "head":
        title = r[1]
        fill = "—" * (INFO_COLS - len(title) - 5)
        body = f'<tspan class="h">{E(title)}</tspan> <tspan class="d">{fill}-—-</tspan>'
        out.append(f'<text x="{x_info}" y="{y}" xml:space="preserve" textLength="{INFO_COLS*CW}" lengthAdjust="spacingAndGlyphs">{body}</text>')
    else:
        key, val = r[1] + ":", r[2]
        dots = max(2, INFO_COLS - len(key) - len(val) - 2)
        body = f'<tspan class="d">. </tspan>'
        body = (f'<tspan class="k">{E(key)}</tspan> <tspan class="d">{"." * dots}</tspan> '
                f'<tspan class="v">{E(val)}</tspan>')
        out.append(f'<text x="{x_info}" y="{y}" xml:space="preserve" textLength="{INFO_COLS*CW}" lengthAdjust="spacingAndGlyphs">{body}</text>')

out.append("</svg>")
open("dark_mode.svg", "w", encoding="utf-8").write("\n".join(out))
print("Wrote dark_mode.svg")
