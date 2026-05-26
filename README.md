<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Rorisang Sekomane — Software Developer</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0d1117;
    --bg-2: #161b22;
    --bg-3: #21262d;
    --border: rgba(255,255,255,0.08);
    --border-md: rgba(255,255,255,0.13);
    --border-hi: rgba(255,255,255,0.22);
    --text: #e6edf3;
    --text-2: #8b949e;
    --text-3: #484f58;
    --accent: #3fb950;
    --accent-dim: rgba(63,185,80,0.12);
    --accent-2: #58a6ff;
    --accent-2-dim: rgba(88,166,255,0.10);
    --amber: #d29922;
    --amber-dim: rgba(210,153,34,0.12);
    --teal: #56d364;
    --radius: 8px;
    --radius-lg: 12px;
  }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
  }

  /* ── layout ── */
  .page {
    max-width: 900px;
    margin: 0 auto;
    padding: 3rem 2rem 4rem;
  }

  /* ── header ── */
  .header {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 2rem;
    align-items: start;
    padding-bottom: 2.5rem;
    border-bottom: 0.5px solid var(--border);
    margin-bottom: 2.5rem;
    animation: fadeUp 0.5s ease both;
  }

  .eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-3);
    margin-bottom: 0.55rem;
  }

  h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 46px;
    font-weight: 400;
    line-height: 1.05;
    letter-spacing: -0.02em;
    color: var(--text);
    margin-bottom: 0.6rem;
  }

  .subtitle {
    font-size: 14px;
    color: var(--text-2);
    margin-bottom: 1.4rem;
    letter-spacing: 0.01em;
  }

  .contact-row {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
  }

  .chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 13px;
    border: 0.5px solid var(--border-md);
    border-radius: 100px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-2);
    text-decoration: none;
    transition: border-color 0.15s, color 0.15s, background 0.15s;
  }

  .chip:hover {
    border-color: var(--border-hi);
    color: var(--text);
    background: var(--bg-3);
  }

  .chip svg { width: 12px; height: 12px; flex-shrink: 0; }

  .header-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 9px;
    padding-top: 4px;
  }

  .status {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius);
    font-size: 11.5px;
    font-family: 'DM Mono', monospace;
    color: var(--text-2);
  }

  .dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-dim);
  }

  .location {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-3);
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .location svg { width: 11px; height: 11px; }

  /* ── sections ── */
  .section {
    margin-bottom: 2.5rem;
    animation: fadeUp 0.5s ease both;
  }

  .section:nth-child(2) { animation-delay: 0.05s; }
  .section:nth-child(3) { animation-delay: 0.10s; }
  .section:nth-child(4) { animation-delay: 0.15s; }
  .section:nth-child(5) { animation-delay: 0.20s; }
  .section:nth-child(6) { animation-delay: 0.25s; }
  .section:nth-child(7) { animation-delay: 0.30s; }
  .section:nth-child(8) { animation-delay: 0.35s; }

  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-3);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .section-label::after {
    content: '';
    flex: 1;
    height: 0.5px;
    background: var(--border);
  }

  /* ── summary ── */
  .summary-quote {
    font-family: 'DM Serif Display', serif;
    font-size: 19px;
    font-style: italic;
    color: var(--text);
    line-height: 1.5;
    padding: 1.25rem 1.5rem;
    border-left: 2px solid var(--border-hi);
    background: var(--bg-2);
    border-radius: 0 var(--radius) var(--radius) 0;
    margin-bottom: 1rem;
  }

  .summary-body {
    font-size: 14px;
    color: var(--text-2);
    line-height: 1.8;
  }

  /* ── experience ── */
  .exp-item {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 0.5rem 1.5rem;
    padding: 1.25rem 1.5rem;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
    margin-bottom: 10px;
    transition: border-color 0.15s;
  }

  .exp-item:hover { border-color: var(--border-md); }

  .exp-header { grid-column: 1 / -1; display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; flex-wrap: wrap; }

  .exp-role {
    font-size: 15px;
    font-weight: 500;
    color: var(--text);
  }

  .exp-company {
    font-size: 13px;
    color: var(--text-2);
    margin-top: 2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .exp-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 3px 9px;
    border-radius: 100px;
    border: 0.5px solid var(--border-md);
    color: var(--text-3);
    white-space: nowrap;
    align-self: flex-start;
  }

  .exp-list {
    grid-column: 1 / -1;
    padding-left: 0;
    list-style: none;
    margin-top: 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .exp-list li {
    font-size: 13.5px;
    color: var(--text-2);
    padding-left: 1.25rem;
    position: relative;
    line-height: 1.65;
  }

  .exp-list li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: var(--accent);
    font-size: 10px;
    top: 3px;
  }

  /* ── education ── */
  .edu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 10px;
  }

  .edu-card {
    padding: 1.1rem 1.25rem;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
    transition: border-color 0.15s;
  }

  .edu-card:hover { border-color: var(--border-md); }

  .edu-degree {
    font-size: 13.5px;
    font-weight: 500;
    color: var(--text);
    margin-bottom: 4px;
  }

  .edu-inst {
    font-size: 12.5px;
    color: var(--text-2);
    margin-bottom: 8px;
  }

  .edu-status {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 3px 10px;
    border-radius: 100px;
    display: inline-block;
  }

  .status-progress {
    background: var(--accent-dim);
    color: var(--accent);
    border: 0.5px solid rgba(63,185,80,0.25);
  }

  .status-complete {
    background: var(--accent-2-dim);
    color: var(--accent-2);
    border: 0.5px solid rgba(88,166,255,0.20);
  }

  /* ── certs ── */
  .cert-list {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
  }

  .cert-item {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 13px;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius);
    font-size: 12px;
    color: var(--text-2);
    transition: border-color 0.15s;
  }

  .cert-item:hover { border-color: var(--border-md); }
  .cert-icon { font-size: 11px; color: var(--amber); }

  /* ── skills grid ── */
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 10px;
  }

  .skill-group {
    padding: 1rem 1.1rem;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
    transition: border-color 0.15s;
  }

  .skill-group:hover { border-color: var(--border-md); }

  .skill-group-title {
    font-size: 11.5px;
    font-weight: 500;
    color: var(--text-2);
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .skill-group-title svg { width: 13px; height: 13px; color: var(--text-3); }

  .skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
  }

  .stag {
    font-family: 'DM Mono', monospace;
    font-size: 10.5px;
    padding: 3px 9px;
    background: var(--bg-3);
    border: 0.5px solid var(--border);
    border-radius: 100px;
    color: var(--text-2);
  }

  /* ── code block ── */
  .code-block {
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
  }

  .code-titlebar {
    display: flex;
    align-items: center;
    gap: 7px;
    padding: 10px 14px;
    border-bottom: 0.5px solid var(--border);
    background: var(--bg-3);
  }

  .tbdot { width: 10px; height: 10px; border-radius: 50%; }
  .tb-r { background: #ff5f57; }
  .tb-y { background: #ffbd2e; }
  .tb-g { background: #28c840; }

  .code-filename {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-3);
    margin-left: auto;
  }

  .code-body {
    padding: 1.25rem 1.5rem;
    font-family: 'DM Mono', monospace;
    font-size: 12.5px;
    line-height: 1.9;
    overflow-x: auto;
  }

  .ln { color: var(--text-3); margin-right: 1.5rem; user-select: none; }
  .kw { color: #ff7b72; }
  .ty { color: #ffa657; }
  .st { color: #a5d6ff; }
  .fn { color: #d2a8ff; }
  .cm { color: var(--text-3); font-style: italic; }
  .va { color: var(--text); }
  .nu { color: #79c0ff; }

  /* ── github stats ── */
  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .stats-card {
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
  }

  .stats-card img { width: 100%; height: auto; display: block; }

  /* ── principles ── */
  .principles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 7px;
  }

  .principle {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 9px 12px;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius);
    font-size: 13px;
    color: var(--text-2);
    transition: border-color 0.15s;
  }

  .principle:hover { border-color: var(--border-md); }

  .p-check {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
    color: var(--accent);
    margin-top: 2px;
  }

  /* ── footer ── */
  .footer {
    border-top: 0.5px solid var(--border);
    padding-top: 1.5rem;
    margin-top: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .footer-quote {
    font-family: 'DM Serif Display', serif;
    font-size: 13px;
    font-style: italic;
    color: var(--text-3);
  }

  .footer-links {
    display: flex;
    gap: 16px;
  }

  .footer-link {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-3);
    text-decoration: none;
    letter-spacing: 0.05em;
    transition: color 0.15s;
  }

  .footer-link:hover { color: var(--text-2); }

  /* ── animation ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── responsive ── */
  @media (max-width: 600px) {
    h1 { font-size: 32px; }
    .header { grid-template-columns: 1fr; }
    .header-right { align-items: flex-start; }
    .stats-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
<div class="page">

  <!-- ── HEADER ── -->
  <div class="header">
    <div>
      <p class="eyebrow">Software Developer · Computer Science Graduate</p>
      <h1>Rorisang Sekomane</h1>
      <p class="subtitle">
        Full-Stack Development &nbsp;·&nbsp; Backend Systems &nbsp;·&nbsp; Cloud &amp; DevOps &nbsp;·&nbsp; Enterprise Platforms
      </p>
      <div class="contact-row">
        <a href="tel:+27639457648" class="chip">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6A19.79 19.79 0 012.12 4.18 2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
          +27 63 945 7648
        </a>
        <a href="mailto:Sekomanerorisang904@gmail.com" class="chip">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          Sekomanerorisang904@gmail.com
        </a>
        <a href="https://github.com/Sekomane" target="_blank" class="chip">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
          github.com/Sekomane
        </a>
        <a href="https://www.linkedin.com/in/rorisang-sekomane-413420268/" target="_blank" class="chip">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          LinkedIn
        </a>
      </div>
    </div>
    <div class="header-right">
      <div class="status"><span class="dot"></span> Open to opportunities</div>
      <div class="location">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
        Pretoria, Gauteng, ZA
      </div>
    </div>
  </div>

  <!-- ── SUMMARY ── -->
  <div class="section">
    <p class="section-label">About</p>
    <div class="summary-quote">"Build once. Scale continuously."</div>
    <p class="summary-body">Computer Science graduate currently pursuing an Advanced Diploma at Tshwane University of Technology. Experienced in software development, web applications, backend systems, cloud technologies, and database integration through internships, freelance projects, and academic work. Skilled in Java, C#, Python, JavaScript, React, SQL, REST APIs, Docker, and AWS S3. A quick learner with strong analytical thinking, collaboration, and communication skills who thrives on complex challenges and continuously developing new technical skills.</p>
  </div>

  <!-- ── EXPERIENCE ── -->
  <div class="section">
    <p class="section-label">Experience</p>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">Software Engineer Intern</p>
          <p class="exp-company">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg>
            Mosebo Networks
          </p>
        </div>
        <span class="exp-badge">Internship</span>
      </div>
      <ul class="exp-list">
        <li>Assisted in backend application development using C# and .NET, applying object-oriented programming concepts.</li>
        <li>Debugged, troubleshot, and improved system performance in collaboration with the development team to enhance application stability.</li>
        <li>Prepared backend components and APIs for testing and integration, working with Docker containers and development environments.</li>
        <li>Gained exposure to AWS S3 cloud storage services and monitoring tools including Jaeger for observability.</li>
        <li>Adapted quickly to modern development tools and workflows within collaborative team environments.</li>
      </ul>
    </div>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">Web Developer</p>
          <p class="exp-company">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg>
            BPS Marketing (Pty) Ltd
          </p>
        </div>
        <span class="exp-badge">Freelance</span>
      </div>
      <ul class="exp-list">
        <li>Developed responsive web applications using React, JavaScript, HTML, and CSS.</li>
        <li>Assisted with backend services, REST API integration, and database connectivity.</li>
        <li>Translated client business requirements directly into technical solutions.</li>
        <li>Enhanced website performance and user experience through continuous improvements.</li>
        <li>Managed frontend updates, website maintenance, and client change requests.</li>
      </ul>
    </div>
  </div>

  <!-- ── EDUCATION ── -->
  <div class="section">
    <p class="section-label">Education</p>
    <div class="edu-grid">
      <div class="edu-card">
        <p class="edu-degree">Advanced Diploma in Computer Science</p>
        <p class="edu-inst">Tshwane University of Technology</p>
        <span class="edu-status status-progress">In Progress · Part-time</span>
      </div>
      <div class="edu-card">
        <p class="edu-degree">Diploma in Computer Science</p>
        <p class="edu-inst">Tshwane University of Technology</p>
        <span class="edu-status status-complete">Completed</span>
      </div>
    </div>
  </div>

  <!-- ── CERTIFICATIONS ── -->
  <div class="section">
    <p class="section-label">Certifications &amp; Training</p>
    <div class="cert-list">
      <div class="cert-item"><span class="cert-icon">◆</span> Backend Developer Program — ALX</div>
      <div class="cert-item"><span class="cert-icon">◆</span> React Development — CodeTribe Academy</div>
      <div class="cert-item"><span class="cert-icon">◆</span> GitHub Actions CI/CD Automation — Udemy</div>
      <div class="cert-item"><span class="cert-icon">◆</span> Ultimate C# Masterclass — Udemy</div>
      <div class="cert-item"><span class="cert-icon">◆</span> Android &amp; Kotlin Development — Udemy</div>
    </div>
  </div>

  <!-- ── SKILLS ── -->
  <div class="section">
    <p class="section-label">Skills</p>
    <div class="skills-grid">

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
          Programming Languages
        </p>
        <div class="skill-tags">
          <span class="stag">C#</span><span class="stag">Java</span><span class="stag">Python</span>
          <span class="stag">JavaScript</span><span class="stag">Kotlin</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          Web &amp; Frontend
        </p>
        <div class="skill-tags">
          <span class="stag">React</span><span class="stag">HTML5</span><span class="stag">CSS3</span>
          <span class="stag">Node.js</span><span class="stag">Angular</span><span class="stag">TypeScript</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          Backend &amp; APIs
        </p>
        <div class="skill-tags">
          <span class="stag">.NET</span><span class="stag">REST APIs</span><span class="stag">Java EE</span>
          <span class="stag">Node.js</span><span class="stag">OOP</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
          Databases
        </p>
        <div class="skill-tags">
          <span class="stag">SQL</span><span class="stag">PostgreSQL</span><span class="stag">MySQL</span>
          <span class="stag">Firebase</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
          Cloud &amp; DevOps
        </p>
        <div class="skill-tags">
          <span class="stag">Docker</span><span class="stag">AWS S3</span><span class="stag">GitHub Actions</span>
          <span class="stag">Linux</span><span class="stag">CI/CD</span><span class="stag">Jaeger</span>
          <span class="stag">Git</span><span class="stag">Agile</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
          Professional Skills
        </p>
        <div class="skill-tags">
          <span class="stag">Teamwork</span><span class="stag">Adaptability</span>
          <span class="stag">Continuous Learning</span><span class="stag">Time Management</span>
          <span class="stag">Attention to Detail</span><span class="stag">Accountability</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg>
          Consulting &amp; Business
        </p>
        <div class="skill-tags">
          <span class="stag">Requirements Gathering</span><span class="stag">Stakeholder Engagement</span>
          <span class="stag">Solution Design</span><span class="stag">Technical Docs</span>
          <span class="stag">Business Analysis</span><span class="stag">Client Communication</span>
        </div>
      </div>

    </div>
  </div>

  <!-- ── CODE BLOCK ── -->
  <div class="section">
    <p class="section-label">Engineering Mindset</p>
    <div class="code-block">
      <div class="code-titlebar">
        <span class="tbdot tb-r"></span>
        <span class="tbdot tb-y"></span>
        <span class="tbdot tb-g"></span>
        <span class="code-filename">Developer.java</span>
      </div>
      <div class="code-body">
<span class="ln">01</span><span class="kw">public class</span> <span class="ty">Developer</span> {
<span class="ln">02</span>  <span class="kw">private final</span> <span class="ty">String</span> <span class="va">name</span>    = <span class="st">"Rorisang Sekomane"</span>;
<span class="ln">03</span>  <span class="kw">private final</span> <span class="ty">String</span> <span class="va">mindset</span> = <span class="st">"Build once. Scale continuously."</span>;
<span class="ln">04</span>
<span class="ln">05</span>  <span class="kw">private final</span> <span class="ty">String</span>[] <span class="va">stack</span> = {
<span class="ln">06</span>    <span class="st">"Java"</span>, <span class="st">"C#"</span>, <span class="st">"Python"</span>, <span class="st">"JavaScript"</span>,
<span class="ln">07</span>    <span class="st">"React"</span>, <span class="st">.NET"</span>, <span class="st">"Docker"</span>, <span class="st">"AWS S3"</span>, <span class="st">"SQL"</span>
<span class="ln">08</span>  };
<span class="ln">09</span>
<span class="ln">10</span>  <span class="kw">private final</span> <span class="ty">String</span>[] <span class="va">priorities</span> = {
<span class="ln">11</span>    <span class="st">"Architecture"</span>, <span class="st">"Performance"</span>, <span class="st">"Reliability"</span>,
<span class="ln">12</span>    <span class="st">"Security"</span>, <span class="st">"Maintainability"</span>, <span class="st">"User Experience"</span>
<span class="ln">13</span>  };
<span class="ln">14</span>
<span class="ln">15</span>  <span class="kw">public void</span> <span class="fn">deliverSolutions</span>() {
<span class="ln">16</span>    <span class="fn">analyze</span>(); <span class="fn">design</span>(); <span class="fn">develop</span>();
<span class="ln">17</span>    <span class="fn">test</span>(); <span class="fn">deploy</span>(); <span class="fn">optimize</span>();
<span class="ln">18</span>  }
<span class="ln">19</span>}
      </div>
    </div>
  </div>

  <!-- ── PRINCIPLES ── -->
  <div class="section">
    <p class="section-label">Principles</p>
    <div class="principles-grid">
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        Write code that others can maintain
      </div>
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        Design for scale before scale is needed
      </div>
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        Prioritise reliability over complexity
      </div>
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        Automate repetitive processes
      </div>
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        Focus on measurable business impact
      </div>
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        Continuously improve systems and processes
      </div>
    </div>
  </div>

  <!-- ── GITHUB STATS ── -->
  <div class="section">
    <p class="section-label">GitHub Analytics</p>
    <div class="stats-grid">
      <div class="stats-card">
        <img
          src="https://github-readme-stats.vercel.app/api?username=Sekomane&show_icons=true&theme=github_dark&hide_border=true&bg_color=161b22&title_color=8b949e&text_color=8b949e&icon_color=3fb950"
          alt="GitHub stats"
          loading="lazy"
        />
      </div>
      <div class="stats-card">
        <img
          src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sekomane&layout=compact&theme=github_dark&hide_border=true&bg_color=161b22&title_color=8b949e&text_color=8b949e"
          alt="Top languages"
          loading="lazy"
        />
      </div>
    </div>
  </div>

  <!-- ── FOOTER ── -->
  <div class="footer">
    <p class="footer-quote">"Engineering is not just writing code — it's designing systems people can depend on."</p>
    <div class="footer-links">
      <a href="mailto:Sekomanerorisang904@gmail.com" class="footer-link">Email</a>
      <a href="https://www.linkedin.com/in/rorisang-sekomane-413420268/" class="footer-link" target="_blank">LinkedIn</a>
      <a href="https://github.com/Sekomane" class="footer-link" target="_blank">GitHub</a>
    </div>
  </div>

</div>
</body>
</html>
