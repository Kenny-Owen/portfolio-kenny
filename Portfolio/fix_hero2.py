# -*- coding: utf-8 -*-
import re

with open(r'D:\Portfolio\portfolio_kenny.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. FOND DE PAGE : changer le fond rose/sable en quelque chose de propre ──
html = html.replace(
    'background: radial-gradient(circle at 50% 0%, #FFF7ED 0%, var(--sand) 100%);',
    'background: linear-gradient(160deg, #E8EFF8 0%, #F4F7FA 40%, #EDF2F0 100%);'
)

# ─── 2. REMPLACER TOUT LE BLOC CSS DU HERO ───────────────────────────────────
OLD_HERO_CSS = r"""    /* ═══════════════════════════════════════════════════════
       HERO — Arche horseshoe avec flottement individuel
       Référence : Core HR / AI Photos Generator layout
       ═══════════════════════════════════════════════════════ */
    .hero-wrapper { padding: 100px 24px 40px; }"""

# Trouver la fin du bloc hero CSS (jusqu'au commentaire ABOUT)
# On remplace tout depuis le début du hero CSS jusqu'à "/* ─── ABOUT"
pattern_hero_css = re.compile(
    r'/\* ═+\s*HERO.*?(?=/\* ─── ABOUT)', 
    re.DOTALL
)

NEW_HERO_CSS = """    /* ═══════════════════════════════════════════════════════
       HERO — Gauche/Droite orbit (Core HR style)
       Images gauche tournent CW, images droite tournent CCW
       Texte centré entre les deux groupes
       ═══════════════════════════════════════════════════════ */
    .hero-wrapper { padding: 100px 24px 40px; }

    header.hero {
      background: #FFFFFF;
      border-radius: var(--radius);
      border: 1px solid rgba(14,22,20,0.05);
      box-shadow: 0 2px 40px rgba(14,22,20,0.07);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* Zone 3 colonnes : [orbite gauche] [texte] [orbite droite] */
    .hero-main {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 70px 48px 48px;
      gap: 20px;
      min-height: 520px;
    }

    /* Conteneur d'une orbite */
    .hero-orbit-wrap {
      position: relative;
      width: 300px;
      height: 440px;
      flex-shrink: 0;
    }

    /* L'anneau rotatif */
    .hero-orbit-ring {
      position: absolute;
      inset: 0;
    }
    .hero-orbit-ring.cw  { animation: orbit-cw  22s linear infinite; }
    .hero-orbit-ring.ccw { animation: orbit-ccw 26s linear infinite; }

    @keyframes orbit-cw  { to { transform: rotate( 360deg); } }
    @keyframes orbit-ccw { to { transform: rotate(-360deg); } }

    /* Image : positionnée par JS, contre-rotation pour rester droite */
    .hero-node {
      position: absolute;
      width: 138px;
      height: 126px;
      border-radius: 22px;
      overflow: hidden;
      background: #F5F5F5;
      border: 2.5px solid #FFFFFF;
      box-shadow: 0 8px 28px rgba(0,0,0,0.10), 0 2px 6px rgba(0,0,0,0.05);
      will-change: transform;
      cursor: default;
    }
    .hero-node img { width:100%; height:100%; object-fit:cover; }
    .hero-node:hover {
      box-shadow: 0 18px 44px rgba(0,0,0,0.16);
      z-index: 10;
    }

    /* Contre-rotation de chaque image dans son anneau */
    .cw  .hero-node { animation: orbit-ccw 22s linear infinite; }
    .ccw .hero-node { animation: orbit-cw  26s linear infinite; }

    /* Colonne texte centrale */
    .hero-center {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      max-width: 340px;
      margin: 0 auto;
    }
    .hero-eyebrow {
      font-size: 0.74rem;
      font-weight: 600;
      color: rgba(14,22,20,0.40);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin: 0 0 14px;
    }
    .hero h1 {
      font-family: 'Fraunces', serif;
      font-size: clamp(1.85rem, 3.2vw, 2.6rem);
      line-height: 1.1;
      color: var(--ink);
      font-weight: 500;
      letter-spacing: -0.02em;
      margin: 0 0 16px;
    }
    .hero h1 span { color: var(--signal); font-style: italic; }
    .hero-subtitle {
      font-size: 0.83rem;
      color: rgba(14,22,20,0.50);
      margin: 0 0 28px;
      line-height: 1.65;
      max-width: 28ch;
    }
    .hero-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: #1C2321;
      color: #FFF;
      padding: 13px 26px;
      border-radius: 100px;
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.01em;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .hero-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(28,35,33,0.22);
    }

    /* 3 pilliers en bas */
    .hero-pillars {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid rgba(14,22,20,0.07);
      text-align: center;
    }
    .hero-pillar {
      padding: 22px 24px;
      border-right: 1px solid rgba(14,22,20,0.07);
    }
    .hero-pillar:last-child { border-right: none; }
    .hero-pillar h3 { font-size: 0.82rem; font-weight: 700; margin-bottom: 5px; color: var(--ink); }
    .hero-pillar p  { font-size: 0.71rem; color: rgba(14,22,20,0.46); line-height: 1.5; }

    """

html = pattern_hero_css.sub(NEW_HERO_CSS, html)

# ─── 3. ABOUT-SECTION-TITLE : agrandir "Qui suis-je ?" ──────────────────────
html = html.replace(
    '.about-section-title {\n      font-size: 0.95rem;\n      color: rgba(14,22,20,0.45);\n      font-weight: 600;\n      margin-bottom: 24px;\n    }',
    '.about-section-title {\n      font-family: \'Fraunces\', serif;\n      font-size: 2rem;\n      color: var(--ink);\n      font-weight: 500;\n      margin-bottom: 32px;\n      letter-spacing: -0.02em;\n    }'
)

# ─── 4. REMPLACER LE HTML DU HERO ────────────────────────────────────────────
OLD_HERO_HTML = re.compile(
    r'<!-- ══════ HERO ══════ -->.*?(?=<!-- ══════ ABOUT)',
    re.DOTALL
)

NEW_HERO_HTML = """<!-- ══════ HERO ══════ -->
<div class="hero-wrapper">
  <header class="hero" id="hero">

    <div class="hero-main">

      <!-- GROUPE GAUCHE : tourne dans le sens des aiguilles -->
      <div class="hero-orbit-wrap">
        <div class="hero-orbit-ring cw" id="ring-left">
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=280&q=85" alt="Nature"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=280&q=85" alt="Capteurs"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=280&q=85" alt="Planification"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=280&q=85" alt="Data"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=280&q=85" alt="Montagne"></div>
        </div>
      </div>

      <!-- TEXTE CENTRAL -->
      <div class="hero-center">
        <p class="hero-eyebrow">Alternant pour le poste de</p>
        <h1>Consultant Numérique<br><span>Responsable</span></h1>
        <p class="hero-subtitle">Accompagner les entreprises dans leur transformation numérique responsable.</p>
        <a class="hero-btn" href="#projets">Démarrer un entretien &nbsp; ➔</a>
      </div>

      <!-- GROUPE DROITE : tourne dans le sens inverse -->
      <div class="hero-orbit-wrap">
        <div class="hero-orbit-ring ccw" id="ring-right">
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=280&q=85" alt="Équipes"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=280&q=85" alt="Événement"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1456324463128-7ff6903988d8?w=280&q=85" alt="Bureau"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=280&q=85" alt="Médical"></div>
          <div class="hero-node"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=280&q=85" alt="Dashboard"></div>
        </div>
      </div>

    </div>

    <!-- 3 piliers en bas de la carte -->
    <div class="hero-pillars">
      <div class="hero-pillar">
        <h3>Éco-conception</h3>
        <p>Sobriété logicielle, efficacité énergétique et cycle de vie produit.</p>
      </div>
      <div class="hero-pillar">
        <h3>Conduite de projet</h3>
        <p>Cadrage, coordination transverse et documentation des livrables.</p>
      </div>
      <div class="hero-pillar">
        <h3>Stratégie RSE</h3>
        <p>Impact carbone, conformité réglementaire et transformation durable.</p>
      </div>
    </div>
  </header>
</div>

"""

html = OLD_HERO_HTML.sub(NEW_HERO_HTML, html)

# ─── 5. REMPLACER LE JS DU HERO ──────────────────────────────────────────────
OLD_JS = re.compile(
    r'/\* ══+\s*HERO RING.*?window\.addEventListener\(\'resize\',\s*positionNodes\);',
    re.DOTALL
)

NEW_JS = """/* ══════════ HERO ORBITS — positionne les images sur ellipse ══════════
   * Chaque anneau (ring-left / ring-right) contient N images.
   * JS place chaque image sur une ellipse (rx, ry) autour du centre.
   * CSS anime la rotation de l'anneau + contre-rotation de chaque image.
   * ═════════════════════════════════════════════════════════════════ */
  function positionOrbit(ringId, rx, ry) {
    const ring = document.getElementById(ringId);
    if (!ring) return;
    const nodes = ring.querySelectorAll('.hero-node');
    const n = nodes.length;
    nodes.forEach((node, i) => {
      // Répartition uniforme, départ depuis le haut (-90°)
      const angle = (i / n) * 2 * Math.PI - Math.PI / 2;
      const x = Math.cos(angle) * rx;
      const y = Math.sin(angle) * ry;
      // On soustrait la moitié des dimensions de l'image (138/2=69, 126/2=63)
      node.style.left = `calc(50% + ${x}px - 69px)`;
      node.style.top  = `calc(50% + ${y}px - 63px)`;
    });
  }

  positionOrbit('ring-left',  105, 170);
  positionOrbit('ring-right', 105, 170);
  window.addEventListener('resize', () => {
    positionOrbit('ring-left',  105, 170);
    positionOrbit('ring-right', 105, 170);
  });"""

html = OLD_JS.sub(NEW_JS, html)

# ─── 6. RESPONSIVE : mise à jour du media query ──────────────────────────────
html = html.replace(
    '.hero-ring { display: none; }\n      .hero-stage { min-height: 360px; }\n      header.hero { min-height: auto; }\n      .hero-pillars { grid-template-columns: 1fr; }',
    '.hero-main { flex-direction: column; padding: 40px 20px 30px; min-height: auto; }\n      .hero-orbit-wrap { width: 100%; height: 260px; }\n      .hero-pillars { grid-template-columns: 1fr; }'
)

with open(r'D:\Portfolio\portfolio_kenny.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("OK — Hero orbit gauche/droite + fond + about title")
