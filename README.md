<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Rorisang Sekomane — Software Engineer</title>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet" />

<style>
  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

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
    --radius: 8px;
    --radius-lg: 12px;
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
  }

  .page {
    max-width: 950px;
    margin: 0 auto;
    padding: 3rem 2rem 4rem;
  }

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
    font-size: 48px;
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

  .chip svg {
    width: 12px;
    height: 12px;
    flex-shrink: 0;
  }

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
    width: 7px;
    height: 7px;
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

  .location svg {
    width: 11px;
    height: 11px;
  }

  .section {
    margin-bottom: 2.5rem;
    animation: fadeUp 0.5s ease both;
  }

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

  .summary-quote {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
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

  .exp-item {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 0.5rem 1.5rem;
    padding: 1.25rem 1.5rem;
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
    margin-bottom: 10px;
    transition: border-color 0.15s, transform 0.15s;
  }

  .exp-item:hover {
    border-color: var(--border-md);
    transform: translateY(-2px);
  }

  .exp-header {
    grid-column: 1 / -1;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1rem;
    flex-wrap: wrap;
  }

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

  .edu-grid,
  .skills-grid,
  .principles-grid {
    display: grid;
    gap: 10px;
  }

  .edu-grid {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }

  .skills-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  }

  .principles-grid {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }

  .edu-card,
  .skill-group,
  .principle,
  .stats-card,
  .code-block {
    background: var(--bg-2);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-lg);
  }

  .edu-card,
  .skill-group {
    padding: 1.1rem 1.25rem;
    transition: border-color 0.15s, transform 0.15s;
  }

  .edu-card:hover,
  .skill-group:hover,
  .principle:hover {
    border-color: var(--border-md);
    transform: translateY(-2px);
  }

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

  .cert-item:hover {
    border-color: var(--border-md);
  }

  .cert-icon {
    font-size: 11px;
    color: var(--amber);
  }

  .skill-group-title {
    font-size: 11.5px;
    font-weight: 500;
    color: var(--text-2);
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 7px;
  }

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

  .principle {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 9px 12px;
    font-size: 13px;
    color: var(--text-2);
    transition: border-color 0.15s, transform 0.15s;
  }

  .p-check {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
    color: var(--accent);
    margin-top: 2px;
  }

  .code-block {
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

  .tbdot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }

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
    white-space: pre;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .stats-card {
    overflow: hidden;
  }

  .stats-card img {
    width: 100%;
    height: auto;
    display: block;
  }

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

  .footer-link:hover {
    color: var(--text-2);
  }

  @keyframes fadeUp {
    from {
      opacity: 0;
      transform: translateY(14px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @media (max-width: 600px) {
    .page {
      padding: 2rem 1rem 3rem;
    }

    h1 {
      font-size: 34px;
    }

    .header {
      grid-template-columns: 1fr;
    }

    .header-right {
      align-items: flex-start;
    }

    .stats-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
</head>

<body>
<div class="page">

  <div class="header">
    <div>
      <p class="eyebrow">Software Engineer · Backend Systems · Cloud Technologies</p>

      <h1>Rorisang Sekomane</h1>

      <p class="subtitle">
        System Design · Full-Stack Engineering · Cloud Architecture · Enterprise Applications
      </p>

      <div class="contact-row">
        <a href="tel:+27639457648" class="chip">+27 63 945 7648</a>
        <a href="mailto:sekomanerorisang904@gmail.com" class="chip">sekomanerorisang904@gmail.com</a>
        <a href="https://github.com/Sekomane" target="_blank" class="chip">GitHub</a>
        <a href="https://www.linkedin.com/in/rorisang-sekomane-413420268/" target="_blank" class="chip">LinkedIn</a>
      </div>
    </div>

    <div class="header-right">
      <div class="status">
        <span class="dot"></span>
        Building Scalable Solutions
      </div>

      <div class="location">
        Pretoria, Gauteng, South Africa
      </div>
    </div>
  </div>

  <div class="section">
    <p class="section-label">About</p>

    <div class="summary-quote">
      "Building scalable software that transforms complex business requirements into reliable digital solutions."
    </div>

    <p class="summary-body">
      Software Engineer with experience designing and developing full-stack applications, backend services,
      cloud-enabled solutions, and database-driven systems. Skilled in Java, C#, .NET, React, TypeScript,
      JavaScript, SQL, Docker, AWS S3, REST APIs, and modern software engineering practices.
      <br><br>
      Focused on building maintainable architectures, improving system reliability, optimizing application
      performance, and delivering business value through clean, scalable, and secure solutions.
    </p>
  </div>

  <div class="section">
    <p class="section-label">Experience</p>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">Software Engineer Intern</p>
          <p class="exp-company">Mosebo Networks</p>
        </div>
        <span class="exp-badge">Backend Engineering</span>
      </div>

      <ul class="exp-list">
        <li>Assisted in backend application development using C# and .NET, applying object-oriented programming principles.</li>
        <li>Debugged, troubleshot, and improved application performance in collaboration with the development team.</li>
        <li>Prepared backend components and APIs for testing, integration, and deployment workflows.</li>
        <li>Worked with Docker containers, AWS S3 cloud storage, and Jaeger monitoring tools.</li>
        <li>Contributed to maintainable backend logic, system stability, and application reliability.</li>
      </ul>
    </div>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">Web Developer</p>
          <p class="exp-company">BPS Marketing (Pty) Ltd</p>
        </div>
        <span class="exp-badge">Full-Stack Development</span>
      </div>

      <ul class="exp-list">
        <li>Developed responsive web applications using React, JavaScript, HTML, CSS, and Bootstrap.</li>
        <li>Built backend services, REST API integrations, and database-connected web solutions.</li>
        <li>Translated client business requirements into practical technical implementations.</li>
        <li>Improved website performance, user experience, and mobile responsiveness.</li>
        <li>Managed frontend updates, website maintenance, and client change requests.</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <p class="section-label">Featured Projects</p>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">AI-Powered Interview Coach</p>
          <p class="exp-company">Angular · Node.js · Firebase · AI Integration</p>
        </div>
        <span class="exp-badge">Full Stack</span>
      </div>

      <ul class="exp-list">
        <li>Designed and developed an AI-powered interview simulation platform.</li>
        <li>Implemented authentication, analytics dashboards, reporting, and feedback workflows.</li>
        <li>Integrated AI services to generate interview questions and performance evaluations.</li>
        <li>Built scalable frontend and backend architecture using Angular and Node.js.</li>
      </ul>
    </div>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">Visa Application Management Platform</p>
          <p class="exp-company">React · TypeScript · REST APIs</p>
        </div>
        <span class="exp-badge">Enterprise App</span>
      </div>

      <ul class="exp-list">
        <li>Developed a multi-step visa processing and document management platform.</li>
        <li>Implemented secure document workflows and responsive user experiences.</li>
        <li>Designed reusable component structures for a scalable frontend architecture.</li>
        <li>Integrated API services, validation workflows, and user-friendly navigation flows.</li>
      </ul>
    </div>

    <div class="exp-item">
      <div class="exp-header">
        <div>
          <p class="exp-role">Business Solutions Portfolio</p>
          <p class="exp-company">BPS Marketing (Pty) Ltd</p>
        </div>
        <span class="exp-badge">Client Projects</span>
      </div>

      <ul class="exp-list">
        <li>Delivered custom business websites and digital platforms for small and medium businesses.</li>
        <li>Designed booking systems, quotation generators, dashboards, and responsive business websites.</li>
        <li>Converted client goals into digital systems that support visibility, communication, and business operations.</li>
      </ul>
    </div>
  </div>

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

  <div class="section">
    <p class="section-label">Certifications & Training</p>

    <div class="cert-list">
      <div class="cert-item"><span class="cert-icon">◆</span> Backend Developer Program — ALX</div>
      <div class="cert-item"><span class="cert-icon">◆</span> React Development — CodeTribe Academy</div>
      <div class="cert-item"><span class="cert-icon">◆</span> GitHub Actions CI/CD Automation — Udemy</div>
      <div class="cert-item"><span class="cert-icon">◆</span> Ultimate C# Masterclass — Udemy</div>
      <div class="cert-item"><span class="cert-icon">◆</span> Android & Kotlin Development — Udemy</div>
    </div>
  </div>

  <div class="section">
    <p class="section-label">Areas of Expertise</p>

    <div class="principles-grid">
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        System Architecture & Solution Design
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Enterprise Application Development
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        REST API Engineering
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Cloud-Native Solutions
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Database Architecture
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Performance Optimization
      </div>
    </div>
  </div>

  <div class="section">
    <p class="section-label">Skills</p>

    <div class="skills-grid">
      <div class="skill-group">
        <p class="skill-group-title">Programming Languages</p>
        <div class="skill-tags">
          <span class="stag">C#</span>
          <span class="stag">Java</span>
          <span class="stag">Python</span>
          <span class="stag">JavaScript</span>
          <span class="stag">TypeScript</span>
          <span class="stag">Kotlin</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">Frontend Engineering</p>
        <div class="skill-tags">
          <span class="stag">React</span>
          <span class="stag">Angular</span>
          <span class="stag">HTML5</span>
          <span class="stag">CSS3</span>
          <span class="stag">Bootstrap</span>
          <span class="stag">Responsive UI</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">Backend Engineering</p>
        <div class="skill-tags">
          <span class="stag">.NET</span>
          <span class="stag">Java EE</span>
          <span class="stag">Node.js</span>
          <span class="stag">REST APIs</span>
          <span class="stag">OOP</span>
          <span class="stag">Authentication</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">Databases</p>
        <div class="skill-tags">
          <span class="stag">MySQL</span>
          <span class="stag">PostgreSQL</span>
          <span class="stag">SQL</span>
          <span class="stag">Firebase</span>
          <span class="stag">Database Design</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">Cloud & DevOps</p>
        <div class="skill-tags">
          <span class="stag">Docker</span>
          <span class="stag">AWS S3</span>
          <span class="stag">GitHub Actions</span>
          <span class="stag">Linux</span>
          <span class="stag">CI/CD</span>
          <span class="stag">Jaeger</span>
          <span class="stag">Git</span>
        </div>
      </div>

      <div class="skill-group">
        <p class="skill-group-title">Professional Skills</p>
        <div class="skill-tags">
          <span class="stag">Problem Solving</span>
          <span class="stag">Teamwork</span>
          <span class="stag">Communication</span>
          <span class="stag">Technical Documentation</span>
          <span class="stag">Client Communication</span>
          <span class="stag">Business Analysis</span>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <p class="section-label">Engineering Mindset</p>

    <div class="code-block">
      <div class="code-titlebar">
        <span class="tbdot tb-r"></span>
        <span class="tbdot tb-y"></span>
        <span class="tbdot tb-g"></span>
        <span class="code-filename">Engineer.java</span>
      </div>

      <div class="code-body">public class Engineer {

    private final String name =
        "Rorisang Sekomane";

    private final String mindset =
        "Build scalable solutions, not temporary fixes.";

    private final String[] expertise = {
        "Architecture",
        "Backend Engineering",
        "Cloud Technologies",
        "Performance",
        "Security",
        "Reliability"
    };

    public void deliverValue() {
        analyseRequirements();
        designArchitecture();
        implementSolutions();
        automateTesting();
        deploySecurely();
        monitorPerformance();
        optimiseContinuously();
    }
}</div>
    </div>
  </div>

  <div class="section">
    <p class="section-label">Principles</p>

    <div class="principles-grid">
      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Write code that others can understand, maintain, and extend.
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Design systems for reliability before adding unnecessary complexity.
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Build scalable solutions that support real business value.
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Automate repetitive tasks and improve development workflows.
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Prioritize security, performance, and maintainability.
      </div>

      <div class="principle">
        <svg class="p-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
        Continuously improve systems, processes, and user experience.
      </div>
    </div>
  </div>

  <div class="section">
    <p class="section-label">Achievements</p>

    <p align="center">
      <img src="https://github-profile-trophy.vercel.app/?username=Sekomane&theme=darkhub&row=1&column=6&no-frame=true" alt="GitHub trophies" />
    </p>
  </div>

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

  <div class="footer">
    <p class="footer-quote">
      "Engineering is not just writing code — it's designing systems people can depend on."
    </p>

    <div class="footer-links">
      <a href="mailto:sekomanerorisang904@gmail.com" class="footer-link">Email</a>
      <a href="https://www.linkedin.com/in/rorisang-sekomane-413420268/" class="footer-link" target="_blank">LinkedIn</a>
      <a href="https://github.com/Sekomane" class="footer-link" target="_blank">GitHub</a>
    </div>
  </div>

</div>
</body>
</html>
