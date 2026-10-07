"""Generates terminal.svg: a terminal-window profile card. Static, no API needed. Edit the data below, then run: python generate.py"""
import html
E = html.escape

HOST = "rorisang@sekomane"
CW, LH, FS = 9.0, 22, 15
W = 900
X0 = 40

ART = [
    " ____   ____",
    "|  _ \\ / ___|",
    "| |_) |\\___ \\",
    "|  _ <  ___) |",
    "|_| \\_\\|____/",
    "",
    "   < / >",
    "",
]
INFO_COLS = 58
INFO = [
    ("head", HOST),
    ("row", "Role", "Software Engineer"),
    ("row", "Focus", "Full-Stack, Backend, Data, Cloud"),
    ("row", "Mission", "Reliable software & data-driven solutions"),
    ("row", "Principles", "Maintainable, Scalable, Secure"),
    ("row", "Status", "Available"),
]
SKILLS = [
    ("Software", "Java, C#, Python, PHP, JS, TS, Kotlin, React, Angular, .NET, Django, Flask"),
    ("Data", "Python, Pandas, NumPy, Scikit-learn, Power BI, SQL"),
    ("Cloud/Tools", "AWS, Docker, GitHub Actions, PostgreSQL, MySQL, REST APIs, Git"),
]
CONTACT = [
    ("GitHub", "github.com/Sekomane"),
    ("LinkedIn", "linkedin.com/in/rorisang-sekomane-413420268"),
    ("Email", "sekomanerorisang904@gmail.com"),
]

lines = []  # (x, [(cls, text)...])
def prompt(cmd, path="~"):
    return [("u", HOST), ("w", ":"), ("p", path), ("w", "$ "), ("t", cmd)]

def blank(): lines.append((X0, []))

lines.append((X0, prompt("neofetch")))
art_w = max(len(l) for l in ART) + 6
xi = X0 + art_w * CW
rows = max(len(ART), len(INFO))
for i in range(rows):
    art = ART[i] if i < len(ART) else ""
    lines.append((X0, [("a", art)]))
    if i < len(INFO):
        r = INFO[i]
        if r[0] == "head":
            lines[-1][1].clear()
            lines[-1] = (X0, [("a", art.ljust(art_w)), ("h", r[1]), ("d", " " + "-" * (INFO_COLS - len(r[1]) - 1))])
        else:
            key, val = r[1] + ":", r[2]
            dots = max(2, INFO_COLS - len(key) - len(val) - 2)
            lines[-1] = (X0, [("a", art.ljust(art_w)), ("k", key), ("d", " " + "." * dots + " "), ("v", val)])
blank()
lines.append((X0, prompt("cat skills.txt")))
kw = max(len(k) for k, _ in SKILLS) + 2
for k, v in SKILLS:
    lines.append((X0, [("k", (k + ":").ljust(kw + 1)), ("v", v)]))
blank()
lines.append((X0, prompt("cat contact.txt")))
kw = max(len(k) for k, _ in CONTACT) + 2
for k, v in CONTACT:
    lines.append((X0, [("k", (k + ":").ljust(kw + 1)), ("v", v)]))
blank()
last = len(lines)
lines.append((X0, prompt("") + [("cur", "\u2588")]))

TOP = 64
H = TOP + len(lines) * LH + 28
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
f'''<style>
text{{font-family:"Consolas","DejaVu Sans Mono","Menlo","Courier New",monospace;font-size:{FS}px;white-space:pre;fill:#e6edf3}}
.u{{fill:#3fb950;font-weight:700}}.p{{fill:#58a6ff;font-weight:700}}.w{{fill:#e6edf3}}.t{{fill:#e6edf3}}
.k{{fill:#ffa657}}.v{{fill:#a5d6ff}}.d{{fill:#484f58}}.h{{fill:#e6edf3;font-weight:700}}.a{{fill:#3fb950}}
.title{{font-size:13px;fill:#7d8590}}
@keyframes f{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes b{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
.l{{animation:f .25s backwards}}
.cur{{fill:#3fb950;animation:b 1.1s step-end infinite}}
</style>''',
f'<rect width="{W}" height="{H}" rx="12" fill="#0d1117"/>',
f'<path d="M0 12a12 12 0 0 1 12-12h{W-24}a12 12 0 0 1 12 12v32H0z" fill="#161b22"/>',
f'<line x1="0" x2="{W}" y1="44" y2="44" stroke="#30363d"/>',
'<circle cx="26" cy="22" r="6.5" fill="#ff5f56"/><circle cx="48" cy="22" r="6.5" fill="#ffbd2e"/><circle cx="70" cy="22" r="6.5" fill="#27c93f"/>',
f'<text x="{W/2}" y="27" text-anchor="middle" class="title">{HOST}: ~</text>']
for i, (x, spans) in enumerate(lines):
    if not spans: continue
    y = TOP + i * LH
    body = "".join(f'<tspan class="{c}">{E(t)}</tspan>' for c, t in spans)
    delay = f' style="animation-delay:{i*0.09:.2f}s"' if i != last else ""
    cls = "l" if i != last else ""
    o.append(f'<text x="{x}" y="{y}" xml:space="preserve" class="{cls}"{delay}>{body}</text>')
o.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#30363d"/>')
o.append('</svg>')
open("terminal.svg", "w", encoding="utf-8").write("\n".join(o))
print("Wrote terminal.svg")
