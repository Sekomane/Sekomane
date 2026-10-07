import os
import html
import json
import urllib.request
import urllib.parse
from datetime import date, datetime, timedelta



# ============================================================
# CONFIGURATION
# ============================================================

USER = "Sekomane"

TOKEN = os.environ.get("GITHUB_TOKEN")

# Card dimensions
WIDTH = 1200
HEIGHT = 760

PAD = 34

# Main colours
BG = "#0d1117"
PANEL = "#161b22"
PANEL_2 = "#0f141a"
BORDER = "#30363d"

TEXT = "#f0f6fc"
MUTED = "#8b949e"

GREEN = "#3fb950"
BLUE = "#58a6ff"
PURPLE = "#bc8cff"
CYAN = "#79c0ff"
ORANGE = "#ffa657"

# Contribution heatmap colours
HEAT_0 = "#21262d"
HEAT_1 = "#0e4429"
HEAT_2 = "#006d32"
HEAT_3 = "#26a641"
HEAT_4 = "#39d353"


# ============================================================
# SVG HELPERS
# ============================================================

def escape(value):
    return html.escape(str(value))


def svg_text(x, y, text, css_class="", anchor=None):
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""

    return (
        f'<text x="{x}" y="{y}" class="{css_class}"'
        f'{anchor_attr}>{escape(text)}</text>'
    )


def rounded_rect(x, y, width, height, fill=PANEL, stroke=BORDER, radius=10):
    return (
        f'<rect x="{x}" y="{y}" '
        f'width="{width}" height="{height}" '
        f'rx="{radius}" fill="{fill}" stroke="{stroke}"/>'
    )


def line(x1, y1, x2, y2, stroke=BORDER, width=1):
    return (
        f'<line x1="{x1}" y1="{y1}" '
        f'x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{width}"/>'
    )


# ============================================================
# GITHUB API
# ============================================================

def api(path):
    """
    Request data from GitHub's REST API.
    """

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "rorisang-profile-generator",
        "X-GitHub-Api-Version": "2026-03-10",
    }

    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    request = urllib.request.Request(
        "https://api.github.com" + path,
        headers=headers,
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


# ============================================================
# GITHUB PROFILE STATISTICS
# ============================================================

def get_repositories():
    """
    Fetch all public repositories owned by the user.
    """

    repositories = []
    page = 1

    while True:

        repos = api(
            f"/users/{USER}/repos"
            f"?type=owner"
            f"&per_page=100"
            f"&page={page}"
        )

        if not repos:
            break

        repositories.extend(repos)

        if len(repos) < 100:
            break

        page += 1

    return repositories


def get_profile_stats():
    """
    Fetch:
        - public repositories
        - total stars
        - followers
    """

    user = api(f"/users/{USER}")

    repositories = get_repositories()

    stars = sum(
        repo.get("stargazers_count", 0)
        for repo in repositories
    )

    return {
        "repos": user.get("public_repos", 0),
        "stars": stars,
        "followers": user.get("followers", 0),
    }


# ============================================================
# CONTRIBUTION ACTIVITY
# ============================================================

def empty_activity():
    """
    Create an empty 52-week activity map.
    """

    today = date.today()

    # Start on the Sunday 51 weeks before the current week.
    start = today - timedelta(days=today.weekday() + 1)
    start -= timedelta(weeks=51)

    activity = {}

    for day_offset in range(52 * 7):
        current = start + timedelta(days=day_offset)
        activity[current] = 0

    return activity


def get_commit_activity():
    """
    Build a 52-week contribution-style activity map.

    GitHub's commit search endpoint is used here because it gives
    us commit dates that can be grouped by day.
    """

    activity = empty_activity()

    start_date = min(activity.keys())
    end_date = max(activity.keys())

    query = (
        f"author:{USER} "
        f"committer-date:{start_date.isoformat()}"
        f"..{end_date.isoformat()}"
    )

    try:

        encoded_query = urllib.parse.quote(query)

        result = api(
            f"/search/commits"
            f"?q={encoded_query}"
            f"&per_page=100"
        )

        # GitHub search only returns the first page of results here.
        # We still use the result as a real activity source rather
        # than fabricating contribution values.
        for item in result.get("items", []):

            commit = item.get("commit", {})
            author = commit.get("author", {})

            commit_date = author.get("date")

            if not commit_date:
                continue

            try:
                day = datetime.fromisoformat(
                    commit_date.replace("Z", "+00:00")
                ).date()

                if day in activity:
                    activity[day] += 1

            except ValueError:
                continue

    except Exception as error:

        print("Could not fetch contribution activity:", error)

    return activity


# ============================================================
# DATA
# ============================================================

try:

    stats = get_profile_stats()

except Exception as error:

    print("Could not fetch GitHub profile:", error)

    stats = {
        "repos": "--",
        "stars": "--",
        "followers": "--",
    }


activity = get_commit_activity()


# ============================================================
# TECH STACK
# ============================================================

SOFTWARE = [
    "Java",
    "C#",
    "Python",
    "React",
    "Angular",
    ".NET",
    "Django",
    "Flask",
]

DATA_ANALYTICS = [
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Power BI",
    "SQL",
]

FOOTER_STACK = [
    "AWS",
    "Docker",
    "GitHub Actions",
    "PostgreSQL",
    "REST APIs",
]


# ============================================================
# SVG
# ============================================================

svg = []

svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{WIDTH}" height="{HEIGHT}" '
    f'viewBox="0 0 {WIDTH} {HEIGHT}">'
)


# ============================================================
# STYLES
# ============================================================

svg.append(
    f"""
<style>

    text {{
        font-family:
            "Inter",
            "Segoe UI",
            "DejaVu Sans",
            sans-serif;
    }}

    .name {{
        fill: {TEXT};
        font-size: 25px;
        font-weight: 700;
        letter-spacing: 1px;
    }}

    .headline {{
        fill: {MUTED};
        font-size: 13px;
        font-weight: 500;
        letter-spacing: 1px;
    }}

    .section {{
        fill: {TEXT};
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 1px;
    }}

    .body {{
        fill: {TEXT};
        font-size: 14px;
    }}

    .muted {{
        fill: {MUTED};
        font-size: 12px;
    }}

    .available {{
        fill: {GREEN};
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
    }}

    .stat-number {{
        fill: {TEXT};
        font-size: 25px;
        font-weight: 700;
    }}

    .stat-label {{
        fill: {MUTED};
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 1px;
    }}

    .skill {{
        fill: {TEXT};
        font-size: 13px;
    }}

    .footer {{
        fill: {MUTED};
        font-size: 12px;
    }}

    .footer-highlight {{
        fill: {TEXT};
        font-size: 12px;
    }}

</style>
"""
)


# ============================================================
# BACKGROUND
# ============================================================

svg.append(
    f'<rect x="1" y="1" '
    f'width="{WIDTH - 2}" height="{HEIGHT - 2}" '
    f'rx="16" fill="{BG}" '
    f'stroke="{BORDER}" stroke-width="1"/>'
)


# ============================================================
# HEADER
# ============================================================

svg.append(
    svg_text(
        PAD,
        48,
        "RORISANG SEKOMANE",
        "name",
    )
)

svg.append(
    svg_text(
        PAD,
        70,
        "SOFTWARE ENGINEER • DATA • CLOUD",
        "headline",
    )
)

# Availability
svg.append(
    f'<circle cx="{WIDTH - 145}" cy="43" r="5" '
    f'fill="{GREEN}"/>'
)

svg.append(
    svg_text(
        WIDTH - 132,
        48,
        "AVAILABLE",
        "available",
    )
)

svg.append(
    line(
        PAD,
        94,
        WIDTH - PAD,
        94,
    )
)


# ============================================================
# TOP TWO-COLUMN AREA
# ============================================================

TOP_Y = 94
TOP_HEIGHT = 235

LEFT_X = PAD
LEFT_WIDTH = 400

RIGHT_X = 454
RIGHT_WIDTH = WIDTH - RIGHT_X - PAD


# Vertical divider
svg.append(
    line(
        RIGHT_X - 27,
        TOP_Y,
        RIGHT_X - 27,
        TOP_Y + TOP_HEIGHT,
    )
)


# ------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------

svg.append(
    svg_text(
        LEFT_X,
        128,
        "ABOUT",
        "section",
    )
)

about_lines = [
    "Building reliable",
    "software systems",
    "across backend, data",
    "and cloud platforms.",
]

about_y = 158

for text in about_lines:

    svg.append(
        svg_text(
            LEFT_X,
            about_y,
            text,
            "body",
        )
    )

    about_y += 21


# Backend tag
tag_x = LEFT_X
tag_y = 252
tag_width = 105
tag_height = 28

svg.append(
    f'<rect x="{tag_x}" y="{tag_y}" '
    f'width="{tag_width}" height="{tag_height}" '
    f'rx="7" fill="{PANEL_2}" stroke="{BORDER}"/>'
)

svg.append(
    svg_text(
        tag_x + tag_width / 2,
        tag_y + 19,
        "BACKEND",
        "muted",
        anchor="middle",
    )
)


# ------------------------------------------------------------
# GITHUB ACTIVITY
# ------------------------------------------------------------

svg.append(
    svg_text(
        RIGHT_X,
        128,
        "GITHUB ACTIVITY",
        "section",
    )
)


# Statistics
STAT_START_X = RIGHT_X
STAT_Y = 165
STAT_GAP = 130

github_stats = [
    ("REPOS", stats["repos"]),
    ("STARS", stats["stars"]),
    ("FOLLOWERS", stats["followers"]),
]

for index, (label, value) in enumerate(github_stats):

    x = STAT_START_X + index * STAT_GAP

    svg.append(
        svg_text(
            x,
            STAT_Y,
            value,
            "stat-number",
        )
    )

    svg.append(
        svg_text(
            x,
            STAT_Y + 19,
            label,
            "stat-label",
        )
    )


# Activity panel
ACTIVITY_X = RIGHT_X
ACTIVITY_Y = 205
ACTIVITY_WIDTH = RIGHT_WIDTH
ACTIVITY_HEIGHT = 100

svg.append(
    rounded_rect(
        ACTIVITY_X,
        ACTIVITY_Y,
        ACTIVITY_WIDTH,
        ACTIVITY_HEIGHT,
        fill=PANEL_2,
        stroke=BORDER,
        radius=8,
    )
)

svg.append(
    svg_text(
        ACTIVITY_X + 16,
        ACTIVITY_Y + 22,
        "Contribution / Activity",
        "muted",
    )
)


# ============================================================
# CONTRIBUTION HEATMAP
# ============================================================

HEAT_X = ACTIVITY_X + 16
HEAT_Y = ACTIVITY_Y + 38

CELL = 7
CELL_GAP = 3

# Activity data is arranged into 52 columns × 7 rows.
start_day = min(activity.keys())

# Move to Sunday.
while start_day.weekday() != 6:
    start_day -= timedelta(days=1)


def heat_colour(count, maximum):
    if count <= 0:
        return HEAT_0

    if maximum <= 0:
        return HEAT_0

    ratio = count / maximum

    if ratio <= 0.25:
        return HEAT_1

    if ratio <= 0.50:
        return HEAT_2

    if ratio <= 0.75:
        return HEAT_3

    return HEAT_4


max_activity = max(activity.values()) if activity else 0


for week in range(52):

    for weekday in range(7):

        current = start_day + timedelta(
            weeks=week,
            days=weekday,
        )

        count = activity.get(current, 0)

        x = HEAT_X + week * (CELL + CELL_GAP)
        y = HEAT_Y + weekday * (CELL + CELL_GAP)

        svg.append(
            f'<rect x="{x}" y="{y}" '
            f'width="{CELL}" height="{CELL}" '
            f'rx="2" fill="{heat_colour(count, max_activity)}"/>'
        )


# ============================================================
# DIVIDER
# ============================================================

MIDDLE_Y = 329

svg.append(
    line(
        PAD,
        MIDDLE_Y,
        WIDTH - PAD,
        MIDDLE_Y,
    )
)

# Vertical divider for lower section
LOWER_DIVIDER_X = WIDTH / 2

svg.append(
    line(
        LOWER_DIVIDER_X,
        MIDDLE_Y,
        LOWER_DIVIDER_X,
        650,
    )
)


# ============================================================
# LOWER SECTION
# ============================================================

LOWER_Y = 365


# ------------------------------------------------------------
# SOFTWARE
# ------------------------------------------------------------

SOFTWARE_X = PAD

svg.append(
    svg_text(
        SOFTWARE_X,
        LOWER_Y,
        "SOFTWARE",
        "section",
    )
)

software_y = LOWER_Y + 32

for skill in SOFTWARE:

    svg.append(
        f'<circle cx="{SOFTWARE_X + 5}" '
        f'cy="{software_y - 5}" '
        f'r="3" fill="{BLUE}"/>'
    )

    svg.append(
        svg_text(
            SOFTWARE_X + 17,
            software_y,
            skill,
            "body",
        )
    )

    software_y += 25


# ------------------------------------------------------------
# DATA & ANALYTICS
# ------------------------------------------------------------

DATA_X = LOWER_DIVIDER_X + 34

svg.append(
    svg_text(
        DATA_X,
        LOWER_Y,
        "DATA & ANALYTICS",
        "section",
    )
)

data_y = LOWER_Y + 32

for skill in DATA_ANALYTICS:

    svg.append(
        f'<circle cx="{DATA_X + 5}" '
        f'cy="{data_y - 5}" '
        f'r="3" fill="{PURPLE}"/>'
    )

    svg.append(
        svg_text(
            DATA_X + 17,
            data_y,
            skill,
            "body",
        )
    )

    data_y += 25


# ============================================================
# FOOTER
# ============================================================

FOOTER_DIVIDER_Y = 650

svg.append(
    line(
        PAD,
        FOOTER_DIVIDER_Y,
        WIDTH - PAD,
        FOOTER_DIVIDER_Y,
    )
)


# Technology stack
footer_stack = " • ".join(FOOTER_STACK)

svg.append(
    svg_text(
        PAD,
        680,
        footer_stack,
        "footer-highlight",
    )
)


# GitHub
svg.append(
    svg_text(
        PAD,
        718,
        f"github.com/{USER}",
        "footer",
    )
)


# Email
svg.append(
    svg_text(
        WIDTH - PAD,
        718,
        "sekomanerorisang904@gmail.com",
        "footer",
        anchor="end",
    )
)


# ============================================================
# CLOSE SVG
# ============================================================

svg.append("</svg>")


# ============================================================
# WRITE FILE
# ============================================================

OUTPUT_FILE = "dark_mode.svg"

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8",
) as file:

    file.write("\n".join(svg))


print()
print("==========================================")
print(" GitHub profile SVG generated successfully")
print("==========================================")
print(f"File: {OUTPUT_FILE}")
print(f"User: {USER}")
print(f"Repos: {stats['repos']}")
print(f"Stars: {stats['stars']}")
print(f"Followers: {stats['followers']}")
print("==========================================")
```
