"""Generates card.svg: a dashboard-style profile card with live GitHub stats + contribution heatmap."""
import os, json, html, urllib.request

USER = "Sekomane"
NAME = "RORISANG SEKOMANE"
SUBTITLE = "SOFTWARE ENGINEER  •  DATA  •  CLOUD"
EMAIL = "sekomanerorisang904@gmail.com"
AVAILABLE = True
WEEKS = 47

SOFTWARE = ["Java", "C#", "Python", "TypeScript", "React", "Angular", ".NET", "Django"]
DATA = ["Python", "Pandas", "NumPy", "Scikit-learn", "Power BI", "SQL"]
CLOUD = ["AWS", "Docker", "GitHub Actions", "PostgreSQL", "MySQL", "REST APIs"]

TOKEN = os.environ.get("GITHUB_TOKEN")
E = html.escape


def call(path, body=None):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "readme-gen"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request("https://api.github.com" + path, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)


def get_stats():
    s = {"REPOS": "--", "STARS": "--", "FOLLOWERS": "--", "COMMITS": "--"}
    try:
        u = call(f"/users/{USER}")
        s["REPOS"], s["FOLLOWERS"] = u["public_repos"], u["followers"]
        stars, page = 0, 1
        while True:
            repos = call(f"/users/{USER}/repos?per_page=100&page={page}&type=owner")
            if not repos: break
            stars += sum(r["stargazers_count"] for r in repos); page += 1
        s["STARS"] = stars
        s["COMMITS"] = f'{call(f"/search/commits?q=author:{USER}&per_page=1")["total_count"]:,}'
    except Exception as e:
        print("stats failed:", e)
    return s


def get_heatmap():
    q = 'query($l:String!){user(login:$l){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{contributionLevel}}}}}}'
    try:
        cal = call("/graphql", {"query": q, "variables": {"l": USER}})["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        weeks = [[d["contributionLevel"] for d in w["contributionDays"]] for w in cal["weeks"]][-WEEKS:]
        return weeks, f'{cal["totalContributions"]:,}'
    except Exception as e:
        print("heatmap failed:", e)
        return [], "--"


stats = get_stats()
weeks, total = get_heatmap()

W, H = 900, 660
LV = {"NONE": "#21262d", "FIRST_QUARTER": "#0e4429", "SECOND_QUARTER": "#006d32", "THIRD_QUARTER": "#26a641", "FOURTH_QUARTER": "#39d353"}
o = []
a = o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a('''<defs>
<linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#3fb950"/><stop offset=".5" stop-color="#58a6ff"/><stop offset="1" stop-color="#bc8cff"/></linearGradient>
<clipPath id="c"><rect width="900" height="660" rx="18"/></clipPath>
</defs>
<style>
text{font-family:"Segoe UI","Helvetica Neue",Arial,sans-serif;fill:#e6edf3}
.m{font-family:"Consolas","DejaVu Sans Mono","Courier New",monospace}
.lbl{font-size:11px;letter-spacing:2.5px;fill:#7d8590;font-weight:600}
.dim{fill:#7d8590}
@keyframes p{0%,100%{opacity:1}50%{opacity:.25}}
.pulse{animation:p 1.8s ease-in-out infinite}
</style>''')
a('<g clip-path="url(#c)">')
a(f'<rect width="{W}" height="{H}" fill="#0d1117"/>')
a(f'<rect width="{W}" height="4" fill="url(#g)"/>')
# header
a(f'<text x="40" y="52" font-size="28" font-weight="700" letter-spacing="1.5">{E(NAME)}</text>')
a(f'<text x="40" y="78" class="m" font-size="12" letter-spacing="2" fill="#58a6ff" style="fill:#58a6ff">{E(SUBTITLE)}</text>')
if AVAILABLE:
    a('<rect x="716" y="34" width="144" height="32" rx="16" fill="#0e2a17" stroke="#238636"/>')
    a('<circle cx="736" cy="50" r="5" fill="#3fb950" class="pulse"/>')
    a('<text x="750" y="54" class="m" font-size="11" letter-spacing="2" style="fill:#3fb950">AVAILABLE</text>')
# dividers
for y in (100, 340, 602):
    a(f'<line x1="0" x2="{W}" y1="{y}" y2="{y}" stroke="#21262d"/>')
a('<line x1="300" x2="300" y1="100" y2="340" stroke="#21262d"/>')
a('<line x1="300" x2="300" y1="340" y2="602" stroke="#21262d"/>')
a('<line x1="600" x2="600" y1="340" y2="602" stroke="#21262d"/>')
# about
a('<text x="40" y="134" class="lbl">ABOUT</text>')
a('<text x="40" y="176" font-size="21" font-weight="600">Building reliable</text>')
a('<text x="40" y="203" font-size="21" font-weight="600">software systems</text>')
for i, t in enumerate(["BACKEND", "FULL-STACK", "DATA", "CLOUD"]):
    x, y = 40 + (i % 2) * 118, 232 + (i // 2) * 34
    w = 106
    a(f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="#161b22" stroke="#30363d"/>')
    a(f'<text x="{x+w/2}" y="{y+17}" text-anchor="middle" class="m" font-size="10.5" letter-spacing="1.5">{t}</text>')
# activity
a('<text x="340" y="134" class="lbl">GITHUB ACTIVITY</text>')
for i, (k, v) in enumerate(stats.items()):
    x = 340 + i * 130
    a(f'<text x="{x}" y="180" font-size="32" font-weight="700" style="fill:#e6edf3">{v}</text>')
    a(f'<text x="{x}" y="200" class="lbl" style="font-size:10px">{k}</text>')
a(f'<text x="860" y="134" text-anchor="end" class="m dim" font-size="11" style="fill:#7d8590">{total} contributions · last year</text>')
gx, gy, pitch = 340, 224, 11
for wi in range(WEEKS):
    days = weeks[wi] if wi < len(weeks) else []
    for di in range(7):
        lv = days[di] if di < len(days) else "NONE"
        a(f'<rect x="{gx+wi*pitch}" y="{gy+di*pitch}" width="9" height="9" rx="2" fill="{LV.get(lv, LV["NONE"])}"/>')
# skill columns
def col(x, title, items, color):
    a(f'<text x="{x}" y="374" class="lbl">{title}</text>')
    for i, t in enumerate(items):
        y = 406 + i * 26
        a(f'<circle cx="{x+4}" cy="{y-4}" r="4" fill="{color}"/>')
        a(f'<text x="{x+20}" y="{y}" font-size="15">{E(t)}</text>')
col(40, "SOFTWARE", SOFTWARE, "#3fb950")
col(340, "DATA &amp; ANALYTICS", DATA, "#58a6ff")
col(640, "CLOUD &amp; TOOLS", CLOUD, "#bc8cff")
# footer
a('<text x="40" y="636" class="m" font-size="12" style="fill:#7d8590">github.com/' + USER + '</text>')
a(f'<text x="860" y="636" text-anchor="end" class="m" font-size="12" style="fill:#7d8590">{E(EMAIL)}</text>')
a('</g>')
a(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#30363d"/>')
a('</svg>')
open("card.svg", "w", encoding="utf-8").write("\n".join(o))
print("Wrote card.svg")
