# Tiny Terra Spaces Guide - Static Site Generator
# Generates building guides, island guides, list pages, and multi-language stubs

import os, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header>
<div class="header-inner">
<a href="/" class="logo">Tiny Terra Spaces Guide</a>
<div class="lang-nav">
<a href="/" class="curr">English</a>
<a href="/de/">Deutsch</a>
<a href="/pt/">Portugu&ecirc;s</a>
<a href="/fr/">Fran&ccedil;ais</a>
<a href="/ja/">日本語</a>
<a href="/hi/">हिन्दी</a>
</div>
</div>
<nav class="main-nav">
<div class="main-nav-inner">
<a href="/">Home</a>
<a href="/buildings/">Buildings</a>
<a href="/islands/">Islands</a>
<a href="/guides/">Guides</a>
<a href="/top-lists/">Top Lists</a>
<a href="/tools/">Tools</a>
</div>
</nav>
</header>
<main>
<div class="wrap">'''

FOOTER = '''</div>
</main>
<footer>
<div class="wrap">
<p>&copy; 2026 Tiny Terra Spaces Guide &mdash; A fan site for Tiny Terra Spaces</p>
</div>
</footer>
</body>
</html>'''

BUILDINGS = [
    ("castle", "Castle", "How to Build the Perfect Castle", "medieval fortress, stone walls, towers"),
    ("farmhouse", "Farmhouse", "Farmhouse Building Guide", "rustic farm life, crops, animals"),
    ("church", "Church", "Church Building Guide & Design Tips", "Gothic architecture, stained glass, spire"),
    ("workshop", "Workshop", "Workshop Guide - Crafting & Production", "tools, crafting stations, production"),
    ("mill", "Mill", "Mill Building Guide - Water & Wind", "water wheel, windmill, grain processing"),
    ("dock", "Dock", "Dock Building Guide - Harbour & Trade", "harbour, boats, fishing, trade"),
    ("tavern", "Tavern", "Tavern Guide - Food, Drink & Social Hub", "inn, ale, cooking, gathering spot"),
    ("watchtower", "Watchtower", "Watchtower Guide - Defense & Views", "defense tower, lookout, archery"),
    ("blacksmith", "Blacksmith", "Blacksmith Guide - Forge & Metalwork", "forge, anvil, weapons, tools"),
    ("market", "Market", "Market Square Guide - Trade & Goods", "market stalls, trading, economy"),
    ("library", "Library", "Library Guide - Knowledge & Scrolls", "books, scrolls, study, knowledge"),
    ("garden", "Garden", "Garden Guide - Plants & Decoration", "flowers, herbs, meditation, beauty"),
    ("bakery", "Bakery", "Bakery Guide - Bread & Pastries", "oven, bread, pastries, food production"),
    ("chapel", "Chapel", "Chapel Guide - Small Shrine & Prayer", "shrine, prayer, peace, meditation"),
    ("cottage", "Cottage", "Cottage Guide - Cozy Village Homes", "village home, cozy, thatched roof"),
]

def make_page(filepath, title, desc, content, lang='en'):
    lang_attr = 'en'
    lang_prefix = ''
    if lang != 'en':
        lang_attr = lang
        lang_prefix = '/' + lang
    
    h = HEADER.format(title=html.escape(title), desc=html.escape(desc))
    h = h.replace('lang="en"', f'lang="{lang_attr}"')
    
    breadcrumb = f'<div class="breadcrumb"><a href="{lang_prefix}/">Home</a> &rsaquo; {title}</div>'
    
    page = h + '\n' + breadcrumb + '\n' + content + '\n' + FOOTER
    
    # Fix language nav if not English
    if lang != 'en':
        page = page.replace('href="/" class="curr">English</a>', 'href="/" class="">English</a>')
        lang_map = {'de': 'Deutsch', 'pt': 'Portugu&ecirc;s', 'fr': 'Fran&ccedil;ais', 'ja': '日本語', 'hi': 'हिन्दी'}
        page = page.replace(f'href="/{lang}/">{lang_map[lang]}</a>', f'href="/{lang}/" class="curr">{lang_map[lang]}</a>')
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'  Created: {filepath}')

def gen_building_pages():
    print('=== Generating Building Pages ===')
    for slug, name, subt, kw in BUILDINGS:
        content = f'''
<div class="guide-content">
<h1>{name} Building Guide</h1>
<p>Welcome to the complete guide to building the {name} in Tiny Terra Spaces. This page covers everything you need to know about designing, placing, and optimizing your {name.lower()}.</p>

<h2>Why Build a {name}?</h2>
<p>The {name} is one of the most important structures in Tiny Terra Spaces. It provides essential functionality for your medieval island community and adds to the overall aesthetic of your settlement.</p>

<h2>Building Requirements</h2>
<ul>
<li><strong>Materials:</strong> Stone, Wood, and specialized resources</li>
<li><strong>Unlock:</strong> Progress through the game to unlock this building</li>
<li><strong>Placement:</strong> Needs a flat area on your island</li>
</ul>

<h2>Design Tips</h2>
<p>When building your {name.lower()}, consider these design tips to make it look great:</p>
<ul>
<li>Place it near complementary buildings for a cohesive village layout</li>
<li>Use pathways to connect it to other structures</li>
<li>Add decorative elements around it for visual appeal</li>
<li>Consider the terrain elevation for the best visual effect</li>
</ul>

<h2>Related Buildings</h2>
<div class="country-list">
''' + '\n'.join([f'<a href="/buildings/{s}-guide.html">{n}</a>' for s, n, _, _ in BUILDINGS[:6]]) + '''
</div>
</div>'''
        
        filepath = os.path.join(BASE, 'buildings', f'{slug}-guide.html')
        make_page(filepath, f'{subt} | Tiny Terra Spaces Guide', f'{subt}. Learn how to build the {name} in Tiny Terra Spaces with pro tips and design inspiration.', content)

def gen_homepage():
    print('=== Generating Homepage ===')
    
    building_links = '\n'.join([
        f'<div class="card"><h3><a href="/buildings/{s}-guide.html">{n}</a></h3><p>Learn how to build and optimize the {n} in Tiny Terra Spaces.</p><a href="/buildings/{s}-guide.html" class="btn">Read Guide</a></div>'
        for s, n, _, _ in BUILDINGS
    ])
    
    content = f'''
<div class="hero">
<h1>Tiny Terra Spaces Complete Guide</h1>
<p>Your ultimate resource for building, exploring, and mastering Tiny Terra Spaces &mdash; the cozy medieval island builder inspired by the beauty of Scotland.</p>
<a href="/guides/beginners-guide.html" class="btn btn-cta">Start Here: Beginner&rsquo;s Guide</a>
</div>

<section>
<h2 class="section-title">Featured Tools</h2>
<div class="card-grid">
<div class="card">
<h3><a href="/tools/island-name-generator.html">Island Name Generator</a></h3>
<p>Generate unique and creative names for your Tiny Terra Spaces islands.</p>
<a href="/tools/island-name-generator.html" class="btn">Try It Now</a>
</div>
<div class="card">
<h3><a href="/tools/building-price-calculator.html">Building Price Calculator</a></h3>
<p>Calculate material costs and plan your builds efficiently.</p>
<a href="/tools/building-price-calculator.html" class="btn">Try It Now</a>
</div>
</div>
</section>

<section>
<h2 class="section-title">Building Guides</h2>
<div class="card-grid">
{building_links}
</div>
</section>

<section>
<h2 class="section-title">Top Lists & Comparisons</h2>
<div class="card-grid">
<div class="card"><h3><a href="/top-lists/top-10-best-buildings.html">Top 10 Best Buildings</a></h3><p>Discover which buildings offer the best value and aesthetics.</p></div>
<div class="card"><h3><a href="/top-lists/5-best-island-layouts.html">5 Best Island Layouts</a></h3><p>Layout inspiration for beginners and advanced players.</p></div>
<div class="card"><h3><a href="/top-lists/best-cozy-games-like-tiny-terra-spaces.html">Best Cozy Games Like Tiny Terra Spaces</a></h3><p>Find similar cozy building games to enjoy.</p></div>
</div>
</section>

<section>
<h2 class="section-title">Quick Guides</h2>
<div class="card-grid">
<div class="card"><h3><a href="/guides/beginners-guide.html">Beginner&rsquo;s Guide</a></h3><p>Everything you need to know to start your journey.</p></div>
<div class="card"><h3><a href="/guides/mistakes-to-avoid.html">5 Mistakes to Avoid</a></h3><p>Common beginner pitfalls and how to avoid them.</p></div>
<div class="card"><h3><a href="/guides/sandbox-mode-guide.html">Sandbox Mode Guide</a></h3><p>Learn the ins and outs of creative sandbox mode.</p></div>
<div class="card"><h3><a href="/guides/island-hop-mode-guide.html">Island Hop Mode Guide</a></h3><p>Master exploration in Island Hop mode.</p></div>
</div>
</section>
'''
    
    make_page(os.path.join(BASE, 'index.html'), 'Tiny Terra Spaces Guide - Complete Building & Island Guides', 
              'Complete Tiny Terra Spaces guide with building guides, island name generator, price calculator, tips and tricks for the cozy medieval builder game.', content)

def gen_guide_pages():
    print('=== Generating Guide Pages ===')
    
    guides = [
        ("beginners-guide", "Tiny Terra Spaces Beginner's Guide", "Starting your cozy medieval island? This beginner's guide covers everything you need to know about building, resources, and enjoying Tiny Terra Spaces.",
         '''<h1>Beginner's Guide to Tiny Terra Spaces</h1>
<p>Welcome to Tiny Terra Spaces! This cozy medieval island builder lets you create your own Scottish-inspired paradise. Here's everything you need to get started.</p>
<h2>Getting Started</h2>
<p>When you first start Tiny Terra Spaces, you'll be placed on a small island with basic resources. Your first task is to build a simple shelter and start gathering materials.</p>
<h2>Essential First Buildings</h2>
<ul>
<li>Farmhouse - Your starting home and base of operations</li>
<li>Workshop - Craft basic tools and items</li>
<li>Garden - Start growing food and herbs</li>
</ul>
<h2>Tips for New Players</h2>
<ul>
<li>Start in Sandbox Mode to learn the mechanics without pressure</li>
<li>Explore your island fully before building</li>
<li>Plan your village layout in advance</li>
</ul>'''),
        ("mistakes-to-avoid", "5 Mistakes to Avoid in Tiny Terra Spaces", "Avoid these common beginner mistakes in Tiny Terra Spaces to save time, resources, and build a better medieval island.",
         '''<h1>5 Mistakes to Avoid in Tiny Terra Spaces</h1>
<ol>
<li><strong>Building Without a Plan</strong> - Always sketch your island layout first</li>
<li><strong>Ignoring Resource Management</strong> - Keep track of your wood and stone supplies</li>
<li><strong>Overcrowding</strong> - Give each building breathing room for aesthetics</li>
<li><strong>Skipping Decorations</strong> - Decorations make your island feel alive</li>
<li><strong>Forgetting Pathways</strong> - Connect buildings with paths for a cohesive look</li>
</ol>'''),
        ("sandbox-mode-guide", "Sandbox Mode Guide", "Learn everything about Sandbox Mode in Tiny Terra Spaces - the creative unlimited building experience.",
         '''<h1>Sandbox Mode Guide</h1>
<p>Sandbox Mode in Tiny Terra Spaces gives you unlimited resources to build your dream medieval island without constraints.</p>
<h2>What You Can Do in Sandbox Mode</h2>
<ul>
<li>Build any building without resource requirements</li>
<li>Experiment with different island layouts</li>
<li>Test building combinations and color schemes</li>
</ul>'''),
        ("island-hop-mode-guide", "Island Hop Mode Guide", "Master Island Hop Mode in Tiny Terra Spaces - explore, discover, and expand across multiple islands.",
         '''<h1>Island Hop Mode Guide</h1>
<p>Island Hop Mode lets you set sail and discover new islands, each with unique landscapes and resources.</p>
<h2>How Island Hop Mode Works</h2>
<ul>
<li>Build a dock to unlock island exploration</li>
<li>Each island has unique terrain and resources</li>
<li>Bring materials from your home island</li>
</ul>'''),
    ]
    
    for slug, title, desc, body in guides:
        content = f'<div class="guide-content">{body}</div>'
        make_page(os.path.join(BASE, 'guides', f'{slug}.html'), f'{title} | Tiny Terra Spaces Guide', desc, content)

def gen_top_lists():
    print('=== Generating Top List Pages ===')
    
    lists = [
        ("top-10-best-buildings", "Top 10 Best Buildings in Tiny Terra Spaces", 
         "Discover the top 10 best buildings in Tiny Terra Spaces ranked by usefulness, aesthetics, and value.",
         '''<h1>Top 10 Best Buildings in Tiny Terra Spaces</h1>
<ol>
<li><strong>Castle</strong> - The centerpiece of any island, majestic and functional</li>
<li><strong>Farmhouse</strong> - Essential for food production and starting your village</li>
<li><strong>Mill</strong> - Crucial for processing resources efficiently</li>
<li><strong>Market</strong> - Trade goods and attract villagers</li>
<li><strong>Tavern</strong> - Social hub that brings your island to life</li>
<li><strong>Church</strong> - Beautiful Gothic architecture, a must-have landmark</li>
<li><strong>Dock</strong> - Unlock exploration and trade routes</li>
<li><strong>Workshop</strong> - Craft essential tools and items</li>
<li><strong>Watchtower</strong> - Defense and stunning panoramic views</li>
<li><strong>Garden</strong> - Beauty, relaxation, and herb production</li>
</ol>'''),
        ("5-best-island-layouts", "5 Best Island Layouts in Tiny Terra Spaces",
         "Five proven island layouts for Tiny Terra Spaces that balance beauty, efficiency, and functionality.",
         '''<h1>5 Best Island Layouts in Tiny Terra Spaces</h1>
<ol>
<li><strong>The Central Castle Layout</strong> - Castle in the center, buildings radiating outward</li>
<li><strong>The Seaside Village Layout</strong> - Buildings along the coastline, dock as focal point</li>
<li><strong>The Terraced Hills Layout</strong> - Buildings on different elevation levels</li>
<li><strong>The Forest Retreat Layout</strong> - Nestled among trees, natural aesthetic</li>
<li><strong>The Trade Hub Layout</strong> - Market and dock centered, production surrounding</li>
</ol>'''),
        ("best-cozy-games-like-tiny-terra-spaces", "Best Cozy Games Like Tiny Terra Spaces",
         "Looking for more cozy building games? Here are the best games like Tiny Terra Spaces to try.",
         '''<h1>Best Cozy Games Like Tiny Terra Spaces</h1>
<ul>
<li><strong>Stardew Valley</strong> - The classic farming and community sim</li>
<li><strong>Animal Crossing: New Horizons</strong> - Island customization at its finest</li>
<li><strong>Palia</strong> - MMO cozy building and exploration</li>
<li><strong>Medieval Dynasty</strong> - First-person medieval survival and building</li>
<li><strong>Foundation</strong> - Medieval city builder with organic roads</li>
</ul>'''),
    ]
    
    for slug, title, desc, body in lists:
        content = f'<div class="guide-content">{body}</div>'
        make_page(os.path.join(BASE, 'top-lists', f'{slug}.html'), f'{title} | Tiny Terra Spaces Guide', desc, content)

def gen_tools_index():
    print('=== Generating Tools Index ===')
    content = '''
<h1>Tiny Terra Spaces Tools</h1>
<p>Useful tools to enhance your Tiny Terra Spaces experience.</p>
<div class="card-grid">
<div class="card">
<h3><a href="/tools/island-name-generator.html">Island Name Generator</a></h3>
<p>Generate unique, creative names for your islands with a single click.</p>
<a href="/tools/island-name-generator.html" class="btn">Open Tool</a>
</div>
<div class="card">
<h3><a href="/tools/building-price-calculator.html">Building Price Calculator</a></h3>
<p>Calculate material costs and plan your building projects efficiently.</p>
<a href="/tools/building-price-calculator.html" class="btn">Open Tool</a>
</div>
</div>'''
    make_page(os.path.join(BASE, 'tools', 'index.html'), 'Tiny Terra Spaces Tools - Generator & Calculator', 
              'Useful tools for Tiny Terra Spaces including island name generator and building price calculator.', content)

def gen_index_pages():
    print('=== Generating Section Index Pages ===')
    sections = ['buildings', 'islands', 'guides', 'top-lists']
    titles = {'buildings': 'Building Guides', 'islands': 'Island Guides', 'guides': 'Game Guides', 'top-lists': 'Top Lists & Rankings'}
    for sec in sections:
        content = f'<h1>{titles[sec]}</h1><p>Browse all our {titles[sec].lower()} for Tiny Terra Spaces.</p>'
        make_page(os.path.join(BASE, sec, 'index.html'), f'{titles[sec]} | Tiny Terra Spaces Guide', f'{titles[sec]} for Tiny Terra Spaces.', content)

def gen_sitemap():
    print('=== Generating Sitemap ===')
    urls = []
    for root, dirs, files in os.walk(BASE):
        for f in files:
            if f.endswith('.html') and 'node_modules' not in root:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, BASE).replace('\\', '/')
                urls.append(f'  <url><loc>https://tinyterraspacesguide.xyz/{rel}</loc></url>')
    
    sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
''' + '\n'.join(urls) + '\n</urlset>'
    
    with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f'  Sitemap generated with {len(urls)} URLs')

if __name__ == '__main__':
    gen_homepage()
    gen_building_pages()
    gen_guide_pages()
    gen_top_lists()
    gen_tools_index()
    gen_index_pages()
    gen_sitemap()
    print('\n=== All pages generated! ===')
