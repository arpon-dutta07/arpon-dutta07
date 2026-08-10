import os

headers = [
    ('arpon-header-aboutme.svg', '🖤 ABOUT ME', 'DEVELOPER PROFILE & OVERVIEW'),
    ('arpon-header-analytics.svg', '📊 GITHUB ANALYTICS', 'REAL-TIME CONTRIBUTION METRICS'),
    ('arpon-header-snake.svg', '🐍 CONTRIBUTION SNAKE', 'INTERACTIVE ACTIVITY GRID'),
    ('arpon-header-mission.svg', '🎯 MISSION STATEMENT', 'CORE VALUES & DRIVING PURPOSE'),
    ('arpon-header-skills.svg', '🛠️ LANGUAGES & TOOLS', 'TECH ARSENAL & PLATFORMS'),
    ('arpon-header-philosophy.svg', '💭 CODING PHILOSOPHY', 'ENGINEERING PRINCIPLES'),
    ('arpon-header-connect.svg', '📫 CONNECT WITH ME', 'LET\'S BUILD SOMETHING AMAZING')
]

template = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="75" viewBox="0 0 800 75">
  <defs>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF0033"/>
      <stop offset="50%" stop-color="#FF3366"/>
      <stop offset="100%" stop-color="#FF6688"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF0033" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#D90429" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#0D0D0D" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      @keyframes expandLine {{
        0% {{ width: 0px; opacity: 0; }}
        100% {{ width: 760px; opacity: 1; }}
      }}
      @keyframes fadeInText {{
        0% {{ opacity: 0; transform: translateY(-5px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      .title-text {{ font-family: 'Fira Code', 'Orbitron', 'Segoe UI', monospace; font-size: 20px; font-weight: 800; fill: url(#titleGrad); filter: url(#glow); animation: fadeInText 0.8s ease-out; }}
      .sub-text {{ font-family: 'Fira Code', 'Segoe UI', monospace; font-size: 10px; font-weight: 600; fill: #888888; letter-spacing: 2px; }}
      .animated-line {{ animation: expandLine 1s ease-out forwards; }}
    </style>
  </defs>

  <!-- Title Text -->
  <text x="20" y="32" class="title-text">{title}</text>
  <text x="780" y="32" class="sub-text" text-anchor="end">{subtitle}</text>

  <!-- Glowing Underline -->
  <rect x="20" y="48" width="760" height="2" rx="1" fill="url(#lineGrad)" class="animated-line"/>
  <circle cx="20" cy="49" r="3" fill="#FF0033" filter="url(#glow)"/>
</svg>
'''

for filename, title, subtitle in headers:
    content = template.format(title=title, subtitle=subtitle)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print('Regenerated valid XML SVG section headers!')
