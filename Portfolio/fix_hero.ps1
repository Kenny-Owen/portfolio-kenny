$file = 'D:\Portfolio\portfolio_kenny.html'
$content = Get-Content $file -Raw -Encoding UTF8

# Ajouter le style hero-eyebrow si pas déjà présent
if ($content -notmatch 'hero-eyebrow') {
    $content = $content -replace '    \.hero-btn \{', '    .hero-eyebrow { font-size:0.78rem; font-weight:600; color:rgba(14,22,20,0.42); margin:0 0 8px; letter-spacing:0.06em; text-transform:uppercase; }
    .hero-btn {'
}

# Pattern pour trouver le bloc hero-bottom (flexible)
$pattern = '(<div class="hero-bottom">)[\s\S]*?(</div>\s*</div>\s*<!-- 3 piliers)'
$replacement = @'
<div class="hero-bottom">
        <p class="hero-eyebrow">Alternant pour le poste de</p>
        <h1>Consultant Num&eacute;rique<br><span>Responsable</span></h1>
        <p class="hero-subtitle">Accompagner les entreprises dans leur transformation num&eacute;rique responsable.</p>
        <a class="hero-btn" href="#projets">D&eacute;marrer un entretien &amp;nbsp; &rarr;</a>
      </div>
    </div>

    <!-- 3 piliers
'@

$content = [regex]::Replace($content, $pattern, $replacement)

Set-Content $file -Value $content -Encoding UTF8 -NoNewline
Write-Host "OK - Hero text updated"
