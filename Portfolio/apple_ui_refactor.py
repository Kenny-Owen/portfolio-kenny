import re

def update_portfolio():
    file_path = r'D:\Portfolio\portfolio_kenny.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fonts update
    # Remplacer les appels Google Fonts actuels par Playfair Display (pour le serif élégant) et Inter (pour le style Apple)
    new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
    html = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=.*?" rel="stylesheet">', new_fonts, html)

    # 2. Update CSS Variables & Body font (Apple Style)
    html = html.replace("font-family: 'Plus Jakarta Sans', sans-serif;", "font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;")
    html = html.replace("font-family: 'Space Grotesk', sans-serif;", "font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', Roboto, sans-serif;")
    
    # 3. Hero Text Structure and Button styling
    # CSS for Hero
    hero_css_repl = """    .hero h1 {
      font-family: 'Playfair Display', serif; /* Élégant comme demandé par la ref */
      font-size: clamp(2.2rem, 4vw, 4rem);
      line-height: 1.1;
      color: var(--ink);
      font-weight: 500;
      letter-spacing: -0.01em;
      margin: 0 0 16px;
    }
    .hero h1 span.gradient-text {
      background: linear-gradient(135deg, #007AFF 0%, #5856D6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 600;
    }
    .hero h1 span.small-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
      font-size: 1.2rem;
      font-weight: 500;
      color: rgba(14,22,20,0.5);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      display: block;
      margin-bottom: 12px;
    }
    .hero-subtitle {
      font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
      font-size: 1.05rem;
      color: rgba(14,22,20,0.55);
      margin: 0 0 36px;
      line-height: 1.6;
      max-width: 50ch;
      font-weight: 400;
    }
    .hero-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(0, 122, 255, 0.08); /* Effet Glass Apple */
      color: #007AFF; /* Couleur bleue pour le texte */
      padding: 16px 36px;
      border-radius: 100px;
      font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
      font-size: 1rem;
      font-weight: 600;
      letter-spacing: 0.01em;
      transition: all 0.3s ease;
      backdrop-filter: blur(10px);
      border: 1px solid rgba(0, 122, 255, 0.2);
    }
    .hero-btn:hover {
      transform: translateY(-2px);
      background: rgba(0, 122, 255, 1);
      color: #FFF;
      box-shadow: 0 12px 28px rgba(0, 122, 255, 0.3);
    }
    
    /* Auras pour donner de la vie au fond blanc */
    .hero-auras {
      position: absolute;
      inset: 0;
      overflow: hidden;
      z-index: 0;
      pointer-events: none;
    }
    .hero-aura {
      position: absolute;
      border-radius: 50%;
      filter: blur(80px);
      opacity: 0.4;
    }
    .hero-aura.a1 { width: 400px; height: 400px; background: #007AFF; top: -100px; left: -100px; }
    .hero-aura.a2 { width: 300px; height: 300px; background: #5856D6; bottom: -50px; right: -50px; }
    .hero-aura.a3 { width: 500px; height: 500px; background: #34C759; top: 30%; left: 50%; transform: translateX(-50%); opacity: 0.15; }
    
    /* On assure que le contenu reste au dessus des auras */
    .hero-main { z-index: 2; position: relative; }
    nav { z-index: 100; position: relative; }"""
    
    html = re.sub(r'\.hero h1 \{.*?(?=\/\* ─── ABOUT)', hero_css_repl + '\n\n    /* ─── ABOUT', html, flags=re.DOTALL)

    # 4. Sections Backgrounds (Délimitations & Dégradés)
    # About Section
    html = html.replace('.about-section {\n      padding: 80px 0;\n      text-align: center;\n    }', 
                        '.about-section {\n      padding: 100px 0;\n      text-align: center;\n      background: linear-gradient(180deg, #FFFFFF 0%, #F2F2F7 100%);\n      border-bottom: 1px solid rgba(0,0,0,0.05);\n    }')
    
    # Cases Section
    html = html.replace('.cases-container {\n      padding: 60px 0;', 
                        '.cases-section-wrap {\n      background: linear-gradient(180deg, #1C1C1E 0%, #000000 100%);\n    }\n    .cases-container {\n      padding: 100px 0;')
    
    # Tools Section
    html = html.replace('.tools-section {\n      padding: 80px 0;\n      text-align: center;\n    }',
                        '.tools-section {\n      padding: 100px 0;\n      text-align: center;\n      background: linear-gradient(180deg, #000000 0%, #F2F2F7 15%, #FFFFFF 100%);\n    }')

    # Edu Section
    html = html.replace('background: rgba(250,245,239,0.5);', 'background: linear-gradient(180deg, #FFFFFF 0%, #E5E5EA 100%);')

    # Contact Section (already has a gradient but let's make it Apple-like)
    html = html.replace('background: linear-gradient(145deg, #12241F, #0A1411);', 'background: linear-gradient(145deg, #007AFF, #5856D6);')

    # 5. Hero HTML Update
    old_hero_center = r'<div class="hero-center">.*?</div>'
    new_hero_center = """<div class="hero-center">
        <h1>
          <span class="small-text">Alternant pour le poste de</span>
          Consultant en<br>
          <span class="gradient-text">Numérique Responsable</span>
        </h1>
        <p class="hero-subtitle">Je recherche une alternance pour accompagner les entreprises dans leur transformation numérique responsable.</p>
        <a class="hero-btn" href="#projets">Démarrer un entretien</a>
      </div>"""
    html = re.sub(old_hero_center, new_hero_center, html, flags=re.DOTALL)
    
    # Add Auras to Hero
    old_header = r'<header class="hero" id="hero">'
    new_header = """<header class="hero" id="hero">
    <!-- Auras Glassmorphism -->
    <div class="hero-auras">
      <div class="hero-aura a1"></div>
      <div class="hero-aura a2"></div>
      <div class="hero-aura a3"></div>
    </div>"""
    html = html.replace(old_header, new_header)

    # Wrap cases container in the dark background wrapper
    html = html.replace('<div class="cases-container wrap">', '<div class="cases-section-wrap">\n  <div class="cases-container wrap">')
    html = html.replace('<!-- ══════ OUTILS ══════ -->', '</div>\n<!-- ══════ OUTILS ══════ -->')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Mise à jour réussie : Apple UI, Typographie, Auras, Hero 3 lignes, Bouton bleu.")

if __name__ == '__main__':
    update_portfolio()
