import os, json, urllib.request, base64

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HERO_BG = "/images/hero-bg.jpg"
GAME_HEADER = "/images/header.jpg"

# Screenshot URLs for building pages
SCREENSHOTS = [
    "/images/hero-bg.jpg",
]

LANG_NAMES = {
    "en": "English", "de": "Deutsch", "pt": "Portugu&ecirc;s",
    "fr": "Fran&ccedil;ais", "ja": "日本語", "hi": "हिन्दी"
}
LANG_DIR = {"en": "", "de": "de", "pt": "pt", "fr": "fr", "ja": "ja", "hi": "hi"}

BUILDINGS = [
    ("castle", "Castle", "🏰", "Majestic Fortress & Royal Residence"),
    ("farmhouse", "Farmhouse", "🏡", "Cozy Village Home & Farm Life"),
    ("church", "Church", "⛪", "Gothic Cathedral & Sacred Space"),
    ("workshop", "Workshop", "🔧", "Crafting Hub & Production Center"),
    ("mill", "Mill", "🌾", "Grain Processing & Power Source"),
    ("dock", "Dock", "⚓", "Harbour & Trade Gateway"),
    ("tavern", "Tavern", "🍺", "Meeting Place & Social Hub"),
    ("watchtower", "Watchtower", "🏗️", "Defense Structure & Panoramic Views"),
    ("blacksmith", "Blacksmith", "🔨", "Forge & Metalworking Workshop"),
    ("market", "Market", "🏪", "Trade Square & Commerce Center"),
    ("library", "Library", "📚", "Knowledge Hall & Scroll Repository"),
    ("garden", "Garden", "🌸", "Peaceful Retreat & Herb Garden"),
    ("bakery", "Bakery", "🥖", "Bread Making & Pastry Shop"),
    ("chapel", "Chapel", "🕊️", "Quiet Shrine & Meditation Space"),
    ("cottage", "Cottage", "🏠", "Rustic Village Home & Garden"),
]

def lang_prefix(lang):
    return "/" + LANG_DIR[lang] if lang != "en" else ""

def lang_path(lang, filepath):
    if lang == "en":
        return os.path.join(BASE, filepath)
    else:
        return os.path.join(BASE, LANG_DIR[lang], filepath)

def make_page_html(title, desc, content, lang="en", curr_section=""):
    lp = lang_prefix(lang)
    ln = LANG_NAMES
    
    # Build language nav
    lang_items = []
    for l_code, l_name in ln.items():
        href = lp + "/" if l_code == "en" else f"/{LANG_DIR[l_code]}/"
        cls = ' class="curr"' if l_code == lang else ""
        lang_items.append(f'<a href="{href}"{cls}>{l_name}</a>')
    lang_nav = "\n".join(lang_items)
    
    # Build main nav
    nav_items = [
        ("Home", lp + "/"),
        ("Buildings", lp + "/buildings/"),
        ("Guides", lp + "/guides/"),
        ("Top Lists", lp + "/top-lists/"),
        ("Tools", lp + "/tools/"),
    ]
    nav_links = []
    for n, href in nav_items:
        cls = ' class="curr"' if curr_section and curr_section in href else ""
        nav_links.append(f'<a href="{href}"{cls}>{n}</a>')
    main_nav = "\n".join(nav_links)
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="google-site-verification" content="2NcsQwj2HUewGrCxIgmFypya9srq2sfJCs5mt3-MrOk"><meta name="description" content="{desc}">
<link rel="stylesheet" href="{lp}/css/style.css">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
</head>
<body>
<header>
<div class="header-inner">
<a href="{lp}/" class="logo"><img src="{lp}{GAME_HEADER}" alt="Tiny Terra Spaces" style="height:28px;border-radius:4px"> Tiny Terra Spaces Guide</a>
<div class="lang-nav">
{lang_nav}
</div>
</div>
<nav class="main-nav">
<div class="main-nav-inner">
{main_nav}
</div>
</nav>
</header>
<main>
<div class="wrap">
{content}
</div>
</main>
<footer>
<div class="wrap">
<p>&copy; 2026 Tiny Terra Spaces Guide &mdash; A fan site for Tiny Terra Spaces. Not affiliated with the game developers.</p>
</div>
</footer>
</body>
</html>'''

def gen_homepage(lang="en"):
    lp = lang_prefix(lang)
    ln = LANG_NAMES
    
    lang_items = []
    for l_code, l_name in ln.items():
        href = "/" if l_code == "en" else f"/{LANG_DIR[l_code]}/"
        cls = ' class="curr"' if l_code == lang else ""
        lang_items.append(f'<a href="{href}"{cls}>{l_name}</a>')
    lang_nav = "\n".join(lang_items)
    
    building_cards = "\n".join([
        f'<div class="card"><h3><a href="{lp}/buildings/{s}-guide.html">{e} {n}</a></h3><p>{d}</p><a href="{lp}/buildings/{s}-guide.html" class="btn">Read Guide</a></div>'
        for s, n, e, d in BUILDINGS
    ])
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Tiny Terra Spaces Guide - Complete Building & Island Guides</title>
<meta name="google-site-verification" content="2NcsQwj2HUewGrCxIgmFypya9srq2sfJCs5mt3-MrOk"><meta name="description" content="Complete Tiny Terra Spaces guide with building guides, island name generator, price calculator, tips and tricks for the cozy medieval builder game inspired by Scotland.">
<link rel="stylesheet" href="{lp}/css/style.css">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
</head>
<body>
<header>
<div class="header-inner">
<a href="{lp}/" class="logo"><img src="{lp}{GAME_HEADER}" alt="Tiny Terra Spaces" style="height:28px;border-radius:4px"> Tiny Terra Spaces Guide</a>
<div class="lang-nav">
{lang_nav}
</div>
</div>
<nav class="main-nav">
<div class="main-nav-inner">
<a href="{lp}/" class="curr">Home</a>
<a href="{lp}/buildings/">Buildings</a>
<a href="{lp}/guides/">Guides</a>
<a href="{lp}/top-lists/">Top Lists</a>
<a href="{lp}/tools/">Tools</a>
</div>
</nav>
</header>
<main>
<div class="hero">
<div class="hero-bg" style="background-image:url('{lp}{HERO_BG}')"></div>
<div class="hero-overlay"></div>
<div class="hero-content">
<h1>Tiny Terra Spaces Guide</h1>
<p>Your ultimate companion for building, exploring, and mastering the cozy medieval island builder inspired by the beauty of Scotland. Build, relax, and create your dream island.</p>
<div class="hero-actions">
<a href="{lp}/guides/beginners-guide.html" class="btn btn-cta">Beginner&#39;s Guide</a>
<a href="{lp}/tools/island-name-generator.html" class="btn btn-outline">Island Name Generator</a>
</div>
</div>
</div>

<div class="wrap" style="padding-top:0">

<div class="section">
<h2 class="section-title"><span class="icon">🔧</span> Featured Tools</h2>
<div class="card-grid">
<div class="card">
<h3><a href="{lp}/tools/island-name-generator.html">Island Name Generator</a></h3>
<p>Generate unique and creative names for your Tiny Terra Spaces islands. Choose from Scottish, Mystical, Cozy, Grand, and Nature styles.</p>
<a href="{lp}/tools/island-name-generator.html" class="btn">Try It Now</a>
</div>
<div class="card">
<h3><a href="{lp}/tools/building-price-calculator.html">Building Price Calculator</a></h3>
<p>Plan your builds efficiently! Calculate material costs for any building type and size before you start construction.</p>
<a href="{lp}/tools/building-price-calculator.html" class="btn">Try It Now</a>
</div>
</div>
</div>

<div class="section">
<h2 class="section-title"><span class="icon">🏗️</span> Building Guides</h2>
<div class="card-grid">
{building_cards}
</div>
</div>

<div class="section">
<h2 class="section-title"><span class="icon">📊</span> Top Lists &amp; Comparisons</h2>
<div class="card-grid">
<div class="card"><h3><a href="{lp}/top-lists/top-10-best-buildings.html">Top 10 Best Buildings</a></h3><p>Discover which buildings offer the best value, aesthetics, and functionality for your island.</p></div>
<div class="card"><h3><a href="{lp}/top-lists/5-best-island-layouts.html">5 Best Island Layouts</a></h3><p>Layout inspiration for beginners and advanced players. Find the perfect design for your island.</p></div>
<div class="card"><h3><a href="{lp}/top-lists/best-cozy-games-like-tiny-terra-spaces.html">Best Cozy Games Like TTS</a></h3><p>Find similar cozy building games to enjoy while waiting for new Tiny Terra Spaces updates.</p></div>
</div>
</div>

<div class="section">
<h2 class="section-title"><span class="icon">📝</span> Quick Guides</h2>
<div class="card-grid">
<div class="card"><h3><a href="{lp}/guides/beginners-guide.html">Beginner&#39;s Guide</a></h3><p>Everything you need to know to start your cozy medieval island journey.</p></div>
<div class="card"><h3><a href="{lp}/guides/mistakes-to-avoid.html">5 Mistakes to Avoid</a></h3><p>Common beginner pitfalls and how to avoid them for a smoother game experience.</p></div>
<div class="card"><h3><a href="{lp}/guides/sandbox-mode-guide.html">Sandbox Mode Guide</a></h3><p>Learn the ins and outs of creative sandbox mode with unlimited resources.</p></div>
<div class="card"><h3><a href="{lp}/guides/island-hop-mode-guide.html">Island Hop Mode Guide</a></h3><p>Master exploration and expansion in Island Hop mode.</p></div>
</div>
</div>

</div>
</main>
<footer>
<div class="wrap">
<p>&copy; 2026 Tiny Terra Spaces Guide &mdash; A fan site for Tiny Terra Spaces. Not affiliated with the game developers.</p>
</div>
</footer>
</body>
</html>'''
    
    fp = os.path.join(BASE, LANG_DIR[lang], "index.html") if lang != "en" else os.path.join(BASE, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Homepage [{lang}]: {fp}")

def gen_building_guide(slug, name, emoji, desc, lang="en"):
    lp = lang_prefix(lang)
    content = f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/buildings/">Buildings</a> &rsaquo; {emoji} {name}</div>
<div class="guide-content">
<h1>{emoji} {name} Building Guide</h1>
<p>Welcome to the complete guide to building the <strong>{name}</strong> in Tiny Terra Spaces! This {desc.lower()} is one of the most important structures you can add to your medieval island.</p>

<h2>Why Build a {name}?</h2>
<p>The {name} adds both beauty and functionality to your island. It serves as a focal point for your village and provides essential benefits that will help your community thrive. Whether you are going for a historically accurate Scottish village or a whimsical fantasy island, the {name} fits perfectly.</p>

<h2>Building Requirements</h2>
<ul>
<li><strong>Materials Needed:</strong> A combination of wood, stone, and specialized resources</li>
<li><strong>Unlock Requirements:</strong> Reach the appropriate milestone in your island progression</li>
<li><strong>Placement Tips:</strong> Choose a flat, visible area for the best visual impact</li>
<li><strong>Size Options:</strong> Small, Medium, and Large variants available</li>
</ul>

<h2>Step-by-Step Construction</h2>
<ol>
<li><strong>Prepare the Site:</strong> Clear the area and level the ground using your tools</li>
<li><strong>Lay the Foundation:</strong> Start with a solid stone foundation to ensure stability</li>
<li><strong>Build the Framework:</strong> Erect the wooden or stone framework for the main structure</li>
<li><strong>Add Walls and Roof:</strong> Complete the shell of the building with appropriate materials</li>
<li><strong>Interior Details:</strong> Furnish and decorate the interior to bring it to life</li>
<li><strong>Surroundings:</strong> Add pathways, gardens, and lighting around the building</li>
</ol>

<h2>Design & Decoration Tips</h2>
<ul>
<li>Place your {name.lower()} where it can be seen from multiple angles</li>
<li>Use complementary buildings nearby to create a cohesive village square</li>
<li>Add greenery and flowers around the base for a lived-in feel</li>
<li>Lighting at night makes your {name.lower()} look magical - place torches or lanterns strategically</li>
<li>Pathways leading to the entrance add polish and guide visitors naturally</li>
</ul>

<h2>Optimal Placement Strategies</h2>
<p>For the best aesthetic result, consider placing your {name.lower()} in relation to other key buildings. A well-planned village layout makes your island feel like a real medieval settlement. Think about sight lines, traffic flow, and how buildings frame outdoor spaces.</p>

<h2>Related Buildings</h2>
<div class="country-list">
''' + "\n".join([f'<a href="{lp}/buildings/{s}-guide.html">{e} {n}</a>' for s, n, e, _ in BUILDINGS[:6]]) + '''
</div>
</div>'''
    
    html = make_page_html(f"{emoji} {name} Guide | Tiny Terra Spaces Guide",
        f"Complete guide to building the {name} in Tiny Terra Spaces. Learn construction tips, design ideas, and placement strategies for this {desc.lower()}.",
        content, lang, "/buildings/")
    
    fp = lang_path(lang, f"buildings/{slug}-guide.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Building [{lang}]: {slug}")

def gen_guides(lang="en"):
    lp = lang_prefix(lang)
    
    guides = [
        ("beginners-guide", "Beginner's Guide", "Starting your cozy medieval island? This comprehensive guide covers everything you need to know about building, resources, and enjoying Tiny Terra Spaces to the fullest.",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/guides/">Guides</a> &rsaquo; Beginner&rsquo;s Guide</div>
<div class="guide-content">
<h1>Beginner&#39;s Guide to Tiny Terra Spaces</h1>
<p>Welcome to Tiny Terra Spaces! This cozy medieval island builder lets you create your own Scottish-inspired paradise at your own pace.</p>

<h2>Getting Started</h2>
<p>When you first launch the game, you will find yourself on a small, peaceful island with basic resources. Your first tasks are simple: explore your surroundings, gather materials, and build your first shelter. The game is designed to be relaxing, so take your time.</p>

<h2>Essential First Buildings</h2>
<ul>
<li><strong>Farmhouse</strong> - Your starting home and base of operations. Provides basic shelter and storage.</li>
<li><strong>Workshop</strong> - Craft essential tools and items needed for expansion.</li>
<li><strong>Garden</strong> - Start growing food, herbs, and decorative plants immediately.</li>
</ul>

<h2>Top Tips for New Players</h2>
<ol>
<li><strong>Start in Sandbox Mode</strong> - Learn the mechanics without resource pressure</li>
<li><strong>Explore Thoroughly</strong> - Walk your entire island before placing any buildings</li>
<li><strong>Plan Your Layout</strong> - Sketch a rough village layout on paper first</li>
<li><strong>Build Pathways</strong> - Connect buildings with paths for a cohesive, lived-in look</li>
<li><strong>Add Decorations Early</strong> - Even simple decorations make your island feel alive</li>
</ol>

<h2>Understanding Resources</h2>
<p>Resources in Tiny Terra Spaces are plentiful but need to be managed wisely. Wood and stone are the most common building materials. Gold coins are earned through trade and completing achievements. Iron is rarer and used for advanced buildings and tools.</p>
</div>'''),
        ("mistakes-to-avoid", "5 Mistakes to Avoid", "Avoid these common beginner mistakes in Tiny Terra Spaces to save time, resources, and build a more beautiful medieval island.",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/guides/">Guides</a> &rsaquo; Mistakes to Avoid</div>
<div class="guide-content">
<h1>5 Mistakes to Avoid in Tiny Terra Spaces</h1>
<ol>
<li><strong>Building Without a Plan</strong> - Always sketch your island layout before placing foundations. It saves time and creates better results.</li>
<li><strong>Ignoring Resource Management</strong> - Keep track of your wood, stone, and gold supplies. Running out mid-build is frustrating.</li>
<li><strong>Overcrowding</strong> - Give each building breathing room. A spacious village looks more authentic and inviting.</li>
<li><strong>Skipping Decorations</strong> - Decorations transform your island from functional to beautiful. Even a few flower boxes make a difference.</li>
<li><strong>Forgetting Pathways</strong> - Paths connect your village and make it feel like a real community. Always add walkways between buildings.</li>
</ol>
</div>'''),
        ("sandbox-mode-guide", "Sandbox Mode Guide", "Learn everything about Sandbox Mode in Tiny Terra Spaces - the creative unlimited building experience with no resource constraints.",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/guides/">Guides</a> &rsaquo; Sandbox Mode</div>
<div class="guide-content">
<h1>Sandbox Mode Guide</h1>
<p>Sandbox Mode in Tiny Terra Spaces gives you unlimited resources to build your dream medieval island without any constraints. Perfect for creative players who want to design without worrying about material costs.</p>
<h2>Key Features</h2>
<ul>
<li>Unlimited wood, stone, gold, and iron - build anything instantly</li>
<li>All buildings unlocked from the start</li>
<li>No time pressure or resource management needed</li>
<li>Perfect for experimenting with different village layouts</li>
<li>Great for photographers who want to capture the perfect island scene</li>
</ul>
</div>'''),
        ("island-hop-mode-guide", "Island Hop Mode Guide", "Master Island Hop Mode in Tiny Terra Spaces - explore, discover resources, and expand your settlement across multiple islands.",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/guides/">Guides</a> &rsaquo; Island Hop Mode</div>
<div class="guide-content">
<h1>Island Hop Mode Guide</h1>
<p>Island Hop Mode lets you set sail from your home island and discover new territories. Each island has its own unique terrain, resources, and building opportunities inspired by the diverse landscapes of Scotland.</p>
<h2>How It Works</h2>
<ul>
<li>Build a dock to unlock boat travel between islands</li>
<li>Each island has unique terrain and available resources</li>
<li>Bring materials from your home island or gather locally</li>
<li>Build satellite settlements for a truly sprawling medieval kingdom</li>
</ul>
</div>'''),
    ]
    
    for slug, title, desc, body in guides:
        html = make_page_html(f"{title} | Tiny Terra Spaces Guide", desc, body, lang, "/guides/")
        fp = lang_path(lang, f"guides/{slug}.html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Guide [{lang}]: {slug}")

def gen_top_lists(lang="en"):
    lp = lang_prefix(lang)
    
    lists = [
        ("top-10-best-buildings", "Top 10 Best Buildings",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/top-lists/">Top Lists</a> &rsaquo; Top 10 Buildings</div>
<div class="guide-content">
<h1>Top 10 Best Buildings in Tiny Terra Spaces</h1>
<p>Ranked by a combination of usefulness, aesthetics, and overall value for your island community.</p>
<ol>
<li><strong>🏰 Castle</strong> - The ultimate centerpiece. Majestic, defensive, and awe-inspiring.</li>
<li><strong>🏡 Farmhouse</strong> - Your starting home. Essential for food and early progression.</li>
<li><strong>🌾 Mill</strong> - Efficient resource processing. A must-have for any serious builder.</li>
<li><strong>🏪 Market</strong> - Trade goods and attract visitors to your island.</li>
<li><strong>🍺 Tavern</strong> - Social hub that brings warmth and character to your village.</li>
<li><strong>⛪ Church</strong> - Beautiful Gothic architecture that makes a statement.</li>
<li><strong>⚓ Dock</strong> - Gateway to exploration. Unlock Island Hop Mode.</li>
<li><strong>🔧 Workshop</strong> - Craft essential items and tools for expansion.</li>
<li><strong>🏗️ Watchtower</strong> - Panoramic views and a sense of security.</li>
<li><strong>🌸 Garden</strong> - Beauty, peace, and practical herb production.</li>
</ol>
</div>'''),
        ("5-best-island-layouts", "5 Best Island Layouts",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/top-lists/">Top Lists</a> &rsaquo; Best Layouts</div>
<div class="guide-content">
<h1>5 Best Island Layouts in Tiny Terra Spaces</h1>
<ol>
<li><strong>The Central Castle Layout</strong> - Castle as the centerpiece, all buildings radiating outward in a semi-circle.</li>
<li><strong>The Seaside Village Layout</strong> - Buildings along the coastline, dock as the main focal point.</li>
<li><strong>The Terraced Hills Layout</strong> - Buildings arranged on different elevation levels for depth.</li>
<li><strong>The Forest Retreat Layout</strong> - Buildings nestled among trees, natural and organic paths.</li>
<li><strong>The Trade Hub Layout</strong> - Market and dock central, with production buildings surrounding.</li>
</ol>
</div>'''),
        ("best-cozy-games-like-tiny-terra-spaces", "Best Cozy Games Like TTS",
         f'''<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; <a href="{lp}/top-lists/">Top Lists</a> &rsaquo; Similar Games</div>
<div class="guide-content">
<h1>Best Cozy Games Like Tiny Terra Spaces</h1>
<ul>
<li><strong>Stardew Valley</strong> - The classic farming and community simulation game.</li>
<li><strong>Animal Crossing: New Horizons</strong> - Island customization and cozy living.</li>
<li><strong>Palia</strong> - MMO cozy building with community features.</li>
<li><strong>Medieval Dynasty</strong> - First-person medieval survival and village building.</li>
<li><strong>Foundation</strong> - Medieval city builder with organic road systems.</li>
<li><strong>Dave the Diver</strong> - Underwater exploration meets restaurant management.</li>
</ul>
</div>'''),
    ]
    
    for slug, title, body in lists:
        html = make_page_html(f"{title} | Tiny Terra Spaces Guide", title, body, lang, "/top-lists/")
        fp = lang_path(lang, f"top-lists/{slug}.html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Top List [{lang}]: {slug}")

def gen_section_indexes(lang="en"):
    lp = lang_prefix(lang)
    sections = [
        ("buildings", "Building Guides", "Browse all our building guides for Tiny Terra Spaces. Each guide includes construction tips, design ideas, and optimal placement strategies."),
        ("islands", "Island Guides", "Explore our island guides for Tiny Terra Spaces. Learn about different island types, terrain features, and layout strategies."),
        ("guides", "Game Guides", "Comprehensive game guides for Tiny Terra Spaces. Tips, tricks, and strategies for players of all levels."),
        ("top-lists", "Top Lists & Rankings", "Curated rankings and comparisons for Tiny Terra Spaces players. Find the best buildings, layouts, and similar games."),
        ("tools", "Useful Tools", "Interactive tools to enhance your Tiny Terra Spaces experience. Island name generator and building price calculator."),
    ]
    for sec, title, desc in sections:
        content = f'<div class="breadcrumb"><a href="{lp}/">Home</a> &rsaquo; {title}</div><h1>{title}</h1><p>{desc}</p>'
        html = make_page_html(f"{title} | Tiny Terra Spaces Guide", desc, content, lang, f"/{sec}/")
        fp = lang_path(lang, f"{sec}/index.html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Section [{lang}]: {sec}")

def gen_sitemap():
    urls = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules", "scripts")]
        for f in files:
            if f.endswith(".html") or f.endswith(".xml"):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, BASE).replace("\\", "/")
                urls.append(f'  <url><loc>https://tinyterraspacesguide.xyz/{rel}</loc></url>')
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "\n".join(urls)
    sitemap += "\n</urlset>"
    with open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"  Sitemap: {len(urls)} URLs")

# === MAIN ===
print("=== Generating Homepages ===")
for lang in ["en"]:
    gen_homepage(lang)
    gen_guides(lang)
    gen_top_lists(lang)
    gen_section_indexes(lang)

print("\n=== Generating Building Guides ===")
for slug, name, emoji, desc in BUILDINGS:
    gen_building_guide(slug, name, emoji, desc, "en")

print("\n=== Generating Multi-Language Pages ===")
for lang in ["de", "pt", "fr", "ja", "hi"]:
    gen_homepage(lang)
    gen_section_indexes(lang)

print("\n=== Copying CSS to language dirs ===")
css_content = open(os.path.join(BASE, "css", "style.css"), "rb").read()
for lang in ["de", "pt", "fr", "ja", "hi"]:
    css_dir = os.path.join(BASE, lang, "css")
    os.makedirs(css_dir, exist_ok=True)
    with open(os.path.join(css_dir, "style.css"), "wb") as f:
        f.write(css_content)

print("\n=== Generating Sitemap ===")
gen_sitemap()

print("\n=== ALL DONE! ===")


