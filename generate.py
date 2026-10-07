"""
Generates dark_mode.svg:
A developer command-center style GitHub profile card
with live GitHub statistics.
"""

import os
import html
import json
import urllib.request
from datetime import date


# ============================================================
# CONFIGURATION
# ============================================================

USER = "Sekomane"
CODING_SINCE = date(2022, 1, 1)

TOKEN = os.environ.get("GITHUB_TOKEN")

# SVG layout
PAD = 32
LINE_HEIGHT = 22
CHAR_WIDTH = 9

LEFT_WIDTH = 48
RIGHT_WIDTH = 62

BG = "#0d1117"
PANEL = "#161b22"
BORDER = "#30363d"

TEXT = "#c9d1d9"
MUTED = "#8b949e"
GREEN = "#3fb950"
BLUE = "#58a6ff"
PURPLE = "#bc8cff"
ORANGE = "#ffa657"
CYAN = "#79c0ff"


# ============================================================
# GITHUB API
# ============================================================

def api(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "rorisang-profile-generator"
    }

    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    request = urllib.request.Request(
        "https://api.github.com" + path,
        headers=headers
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def get_stats():
    """
    Fetch live GitHub statistics.
    """

    try:
        user = api(f"/users/{USER}")

        stars = 0
        page = 1

        while True:
            repos = api(
                f"/users/{USER}/repos"
                f"?per_page=100&page={page}&type=owner"
            )

            if not repos:
                break

            stars += sum(
                repo["stargazers_count"]
                for repo in repos
            )

            page += 1

        try:
            commits = api(
                f"/search/commits"
                f"?q=author:{USER}&per_page=1"
            )["total_count"]
        except Exception:
            commits = "--"

        return {
            "Repos": user["public_repos"],
            "Stars": stars,
            "Followers": user["followers"],
            "Commits": f"{commits:,}"
                if isinstance(commits, int)
                else commits
        }

    except Exception as error:

        print("Could not fetch GitHub stats:", error)

        return {
            "Repos": "--",
            "Stars": "--",
            "Followers": "--",
            "Commits": "--"
        }


# ============================================================
# HELPERS
# ============================================================

def coding_time():
    today = date.today()
    start = CODING_SINCE

    years = today.year - start.year
    months = today.month - start.month

    if today.day < start.day:
        months -= 1

    if months < 0:
        years -= 1
        months += 12

    return f"{years}y {months}m"


def escape(value):
    return html.escape(str(value))


def text_width(text):
    return len(str(text)) * CHAR_WIDTH


# ============================================================
# DATA
# ============================================================

stats = get_stats()

SYSTEM_INFO = [
    ("OS", "Windows / Linux"),
    ("ROLE", "Software Engineer"),
    ("FOCUS", "Full-Stack + Backend"),
    ("DATA", "Science + Analytics"),
    ("CLOUD", "AWS + Docker"),
    ("EDITOR", "VS Code / IntelliJ"),
    ("UPTIME", coding_time()),
]

SOFTWARE = [
    "Java",
    "C#",
    "Python",
    "PHP",
    "JavaScript",
    "TypeScript",
    "React",
    "Angular",
    ".NET",
    "Django",
    "Flask",
    "Node.js",
]

DATA = [
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Power BI",
    "SQL",
    "PostgreSQL",
    "MySQL",
]

CLOUD = [
    "AWS",
    "Docker",
    "Git",
    "GitHub Actions",
    "Firebase",
    "Linux",
    "REST APIs",
]

CONTACT = [
    ("Email", "sekomanerorisang904@gmail.com"),
    ("LinkedIn", "rorisang-sekomane"),
    ("GitHub", USER),
]


# ============================================================
# SVG SETUP
# ============================================================

WIDTH = 1200

LEFT_X = PAD
RIGHT_X = 590

HEIGHT = 700

svg = []

svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{WIDTH}" height="{HEIGHT}" '
    f'viewBox="0 0 {WIDTH} {HEIGHT}">'
)

svg.append(f"""
<style>

text {{
    font-family:
        "JetBrains Mono",
        "Fira Code",
        "Consolas",
        "DejaVu Sans Mono",
        monospace;
}}

.title {{
    fill: {TEXT};
    font-size: 24px;
    font-weight: bold;
}}

.subtitle {{
    fill: {MUTED};
    font-size: 13px;
}}

.label {{
    fill: {MUTED};
    font-size: 13px;
}}

.value {{
    fill: {TEXT};
    font-size: 13px;
}}

.green {{
    fill: {GREEN};
}}

.blue {{
    fill: {BLUE};
}}

.purple {{
    fill: {PURPLE};
}}

.orange {{
    fill: {ORANGE};
}}

.cyan {{
    fill: {CYAN};
}}

.muted {{
    fill: {MUTED};
}}

.skill {{
    fill: {TEXT};
    font-size: 13px;
}}

.small {{
    fill: {MUTED};
    font-size: 11px;
}}

.stat-number {{
    fill: {TEXT};
    font-size: 24px;
    font-weight: bold;
}}

.stat-label {{
    fill: {MUTED};
    font-size: 11px;
}}

</style>
""")

# Background
svg.append(
    f'<rect width="{WIDTH}" height="{HEIGHT}" '
    f'rx="18" fill="{BG}" '
    f'stroke="{BORDER}" stroke-width="1"/>'
)


# ============================================================
# HEADER
# ============================================================

svg.append(
    f'<text x="{PAD}" y="48" class="title">'
    f'rorisang@sekomane'
    f'</text>'
)

svg.append(
    f'<text x="{PAD}" y="70" class="subtitle">'
    f'~/developer/profile'
    f'</text>'
)

# Status
svg.append(
    f'<circle cx="285" cy="65" r="5" fill="{GREEN}"/>'
)

svg.append(
    f'<text x="298" y="70" class="green">'
    f'ONLINE'
    f'</text>'
)

# Header separator
svg.append(
    f'<line x1="{PAD}" y1="88" '
    f'x2="{WIDTH - PAD}" y2="88" '
    f'stroke="{BORDER}"/>'
)


# ============================================================
# LEFT PANEL — TERMINAL
# ============================================================

svg.append(
    f'<rect x="{LEFT_X}" y="110" '
    f'width="520" height="545" rx="12" '
    f'fill="{PANEL}" stroke="{BORDER}"/>'
)

# Terminal top bar
svg.append(
    f'<circle cx="{LEFT_X + 20}" cy="132" r="5" fill="#ff5f56"/>'
)

svg.append(
    f'<circle cx="{LEFT_X + 38}" cy="132" r="5" fill="#ffbd2e"/>'
)

svg.append(
    f'<circle cx="{LEFT_X + 56}" cy="132" r="5" fill="#27c93f"/>'
)

svg.append(
    f'<text x="{LEFT_X + 80}" y="137" class="small">'
    f'rorisang@sekomane:~'
    f'</text>'
)


# Terminal content
terminal_lines = [

    ("green", "$ whoami"),
    ("value", "rorisang_sekomane"),
    ("muted", ""),

    ("green", "$ cat role.txt"),
    ("value", "Software Engineer"),
    ("value", "Full-Stack • Backend • Data • Cloud"),
    ("muted", ""),

    ("green", "$ ./build --production"),
    ("value", "Architecture .............. OK"),
    ("value", "Backend ................... OK"),
    ("value", "Data pipelines ............ OK"),
    ("value", "Testing ................... OK"),
    ("value", "Deployment ................ OK"),
    ("muted", ""),

    ("green", "$ system --status"),
    ("cyan", "● APIs .................... operational"),
    ("cyan", "● Databases ............... connected"),
    ("cyan", "● Cloud ................... available"),
    ("cyan", "● CI/CD ................... automated"),
    ("muted", ""),

    ("green", "$ focus"),
    ("purple", "Software Engineering"),
    ("purple", "Data Science & Analytics"),
    ("purple", "Cloud & DevOps"),
    ("muted", ""),

    ("green", "$ echo $PHILOSOPHY"),
    ("orange", "\"Build systems people can depend on.\""),
    ("muted", ""),

    ("green", "$ _"),
]

terminal_y = 170

for color, line in terminal_lines:

    svg.append(
        f'<text x="{LEFT_X + 22}" '
        f'y="{terminal_y}" '
        f'class="{color}">'
        f'{escape(line)}'
        f'</text>'
    )

    terminal_y += 21


# ============================================================
# RIGHT PANEL — PROFILE
# ============================================================

# System information
svg.append(
    f'<text x="{RIGHT_X}" y="135" class="title">'
    f'SYSTEM PROFILE'
    f'</text>'
)

svg.append(
    f'<line x1="{RIGHT_X}" y1="148" '
    f'x2="1165" y2="148" '
    f'stroke="{BORDER}"/>'
)

y = 175

for label, value in SYSTEM_INFO:

    svg.append(
        f'<text x="{RIGHT_X}" y="{y}" class="label">'
        f'{escape(label):<12}'
        f'</text>'
    )

    svg.append(
        f'<text x="{RIGHT_X + 115}" y="{y}" class="value">'
        f'{escape(value)}'
        f'</text>'
    )

    y += 24


# ============================================================
# GITHUB STATS
# ============================================================

y += 10

svg.append(
    f'<text x="{RIGHT_X}" y="{y}" class="title">'
    f'GITHUB'
    f'</text>'
)

y += 14

svg.append(
    f'<line x1="{RIGHT_X}" y1="{y}" '
    f'x2="1165" y2="{y}" '
    f'stroke="{BORDER}"/>'
)

y += 42

github_stats = [
    ("REPOS", stats["Repos"]),
    ("STARS", stats["Stars"]),
    ("FOLLOWERS", stats["Followers"]),
    ("COMMITS", stats["Commits"]),
]

stat_x = RIGHT_X

for label, value in github_stats:

    svg.append(
        f'<text x="{stat_x}" y="{y}" '
        f'class="stat-number">'
        f'{escape(value)}'
        f'</text>'
    )

    svg.append(
        f'<text x="{stat_x}" y="{y + 18}" '
        f'class="stat-label">'
        f'{label}'
        f'</text>'
    )

    stat_x += 135


# ============================================================
# SKILLS
# ============================================================

y += 65

svg.append(
    f'<text x="{RIGHT_X}" y="{y}" class="title">'
    f'TECH STACK'
    f'</text>'
)

y += 14

svg.append(
    f'<line x1="{RIGHT_X}" y1="{y}" '
    f'x2="1165" y2="{y}" '
    f'stroke="{BORDER}"/>'
)

y += 32


def draw_skill_section(title, skills, color, start_y):

    svg.append(
        f'<text x="{RIGHT_X}" y="{start_y}" '
        f'class="{color}">'
        f'{escape(title)}'
        f'</text>'
    )

    current_x = RIGHT_X
    current_y = start_y + 25

    for skill in skills:

        box_width = text_width(skill) + 22

        # Wrap
        if current_x + box_width > 1165:

            current_x = RIGHT_X
            current_y += 32

        svg.append(
            f'<rect x="{current_x}" y="{current_y - 17}" '
            f'width="{box_width}" height="25" rx="7" '
            f'fill="{BG}" stroke="{BORDER}"/>'
        )

        svg.append(
            f'<text x="{current_x + 11}" '
            f'y="{current_y}" '
            f'class="skill">'
            f'{escape(skill)}'
            f'</text>'
        )

        current_x += box_width + 8

    return current_y + 40


y = draw_skill_section(
    "SOFTWARE ENGINEERING",
    SOFTWARE,
    "blue",
    y
)

y = draw_skill_section(
    "DATA SCIENCE & ANALYTICS",
    DATA,
    "purple",
    y
)

y = draw_skill_section(
    "CLOUD / DEVOPS",
    CLOUD,
    "cyan",
    y
)


# ============================================================
# FOOTER / CONTACT
# ============================================================

footer_y = HEIGHT - 48

svg.append(
    f'<line x1="{PAD}" y1="{footer_y - 22}" '
    f'x2="{WIDTH - PAD}" y2="{footer_y - 22}" '
    f'stroke="{BORDER}"/>'
)

svg.append(
    f'<text x="{PAD}" y="{footer_y}" class="small">'
    f'github.com/{USER}'
    f'</text>'
)

svg.append(
    f'<text x="{WIDTH - 330}" y="{footer_y}" class="small">'
    f'Engineering • Data • Cloud'
    f'</text>'
)


# ============================================================
# WRITE SVG
# ============================================================

svg.append("</svg>")

with open(
    "dark_mode.svg",
    "w",
    encoding="utf-8"
) as file:

    file.write("\n".join(svg))


print("Wrote dark_mode.svg")
