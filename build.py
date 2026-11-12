from pathlib import Path
from html import escape as h
import json
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'content.json').read_text())
EMAIL=DATA['email'];OWNER=DATA['developer'];BASE=DATA['base_url'];DATE=DATA['updated']
LABELS={'privacy':'\u9690\u79c1\u653f\u7b56','terms':'\u7528\u6237\u534f\u8bae','support':'\u6280\u672f\u652f\u6301'}
def a(url,label):return f'<a href="{h(url,quote=True)}">{h(label)}</a>'
def blocks(sections):
 out=[]
 for i,section in enumerate(sections,1):
  out.append(f'<section id="section-{i}"><h2>{h(section["title"])}</h2>')
  for p in section.get('paragraphs',[]):out.append(f'<p>{h(p)}</p>')
  if section.get('items'):out.append('<ul>'+''.join(f'<li>{h(p)}</li>' for p in section['items'])+'</ul>')
  for link in section.get('links',[]):out.append('<p class="reference">'+a(link['url'],link['label'])+'</p>')
  out.append('</section>')
 return '\n'.join(out)
def shell(title,description,body,slug=None,kind=None):
 hosting_privacy=a('https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement','GitHub \u9690\u79c1\u58f0\u660e')
 canonical=BASE+(f'{slug}-{kind}.html' if slug else '')
 return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{h(description,quote=True)}"><meta name="color-scheme" content="light"><title>{h(title)} \xb7 {h(OWNER)}</title><link rel="canonical" href="{canonical}"><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#main">\u8df3\u5230\u6b63\u6587</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="index.html">{h(OWNER)}<span>\u5e94\u7528\u652f\u6301\u4e0e\u653f\u7b56</span></a><a class="header-contact" href="mailto:{EMAIL}">\u8054\u7cfb\u5f00\u53d1\u8005</a></div></header>
<main id="main" class="wrap">{body}</main><footer class="wrap"><p>\u5f00\u53d1\u8005 / Developer\uff1a{h(OWNER)} \xb7 {a('mailto:'+EMAIL,EMAIL)}</p><p>\u672c\u7ad9\u4e0d\u5d4c\u5165\u5e7f\u544a\u3001\u7edf\u8ba1\u811a\u672c\u6216\u5728\u7ebf\u8868\u5355\u3002GitHub Pages \u5728\u63d0\u4f9b\u7f51\u9875\u670d\u52a1\u65f6\u53ef\u80fd\u8bb0\u5f55 IP \u5730\u5740\u7b49\u8bbf\u95ee\u65e5\u5fd7\uff0c\u8be6\u89c1 {hosting_privacy}\u3002</p><p>\xa9 2026 {h(OWNER)} \xb7 \u66f4\u65b0\u65e5\u671f\uff1a{DATE}</p></footer></body></html>'''
for slug,app in DATA['apps'].items():
 for kind,label in LABELS.items():
  nav='<nav class="tabs" aria-label="\u5e94\u7528\u76f8\u5173\u9875\u9762">'+''.join(a(f'{slug}-{k}.html',v) if k!=kind else f'<a href="{slug}-{k}.html" aria-current="page">{v}</a>' for k,v in LABELS.items())+'</nav>'
  intro=f'<a class="back" href="index.html">\u2190 \u5168\u90e8\u5e94\u7528</a><div class="page-heading"><span class="eyebrow">{h(app["name"])} \xb7 {h(app["english"])}</span><h1>{label}</h1><p class="lede">{h(app[kind+"_intro"])}</p><p class="meta">\u66f4\u65b0\u65e5\u671f\uff1a{DATE} \xb7 \u5f00\u53d1\u8005\uff1a{h(OWNER)}</p></div>'
  contact=f'<aside class="contact-card"><div><span class="eyebrow">CONTACT / \u8054\u7cfb\u65b9\u5f0f</span><h2>\u9700\u8981\u5e2e\u52a9\uff1f\u76f4\u63a5\u8054\u7cfb\u6211\u4eec</h2><p>{h(app["name"])}\u7684\u95ee\u9898\u53cd\u9988\u3001\u4f7f\u7528\u5e2e\u52a9\u4e0e\u9690\u79c1\u8bf7\u6c42\u5747\u53ef\u53d1\u9001\u81f3\u4e0b\u65b9\u90ae\u7bb1\u3002</p></div><a class="email" href="mailto:{EMAIL}?subject={slug}%20support">{EMAIL}</a></aside>'
  body=intro+nav+contact+'<article class="document">'+blocks(app[kind])+'</article>'
  (ROOT/f'{slug}-{kind}.html').write_text(shell(app['name']+' \xb7 '+label,app[kind+'_intro'],body,slug,kind))
cards=[]
for slug,app in DATA['apps'].items():
 links=''.join(a(f'{slug}-{k}.html',v) for k,v in LABELS.items())
 cards.append(f'<article class="app-card {slug}"><div class="app-mark" aria-hidden="true">{h(app["mark"])}</div><span class="eyebrow">{h(app["english"])}</span><h2>{h(app["name"])}</h2><p>{h(app["summary"])}</p><nav aria-label="{h(app["name"])}\u9875\u9762">{links}</nav></article>')
body=f'<section class="hero"><span class="eyebrow">SUPPORT & POLICIES</span><h1>\u6bcf\u4e00\u6b3e\u5e94\u7528\uff0c<br>\u90fd\u6709\u6e05\u695a\u7684\u8bf4\u660e\u3002</h1><p class="lede">\u8fd9\u91cc\u96c6\u4e2d\u63d0\u4f9b\u5343\u5ea6\u9605\u8bfb\u3001\u6620\u9875\u548c\u5c9b\u5c7f\u8d26\u672c\u7684\u4f7f\u7528\u5e2e\u52a9\u3001\u9690\u79c1\u653f\u7b56\u4e0e\u7528\u6237\u534f\u8bae\u3002</p><p class="owner-line">\u7531 {h(OWNER)} \u5f00\u53d1\u4e0e\u7ef4\u62a4 \xb7 {a("mailto:"+EMAIL,EMAIL)}</p></section><section class="app-grid" aria-label="\u9009\u62e9\u5e94\u7528">'+''.join(cards)+'</section><section class="help-note"><h2>\u53cd\u9988\u95ee\u9898\u65f6\uff0c\u53ef\u4ee5\u544a\u8bc9\u6211\u4eec\u8fd9\u4e9b\u4fe1\u606f</h2><p>\u5e94\u7528\u540d\u79f0\u4e0e\u7248\u672c\u3001iOS \u7248\u672c\u3001\u8bbe\u5907\u578b\u53f7\u3001\u64cd\u4f5c\u6b65\u9aa4\uff0c\u4ee5\u53ca\u7ecf\u8fc7\u906e\u6321\u7684\u9519\u8bef\u622a\u56fe\u3002\u8bf7\u52ff\u53d1\u9001\u5bc6\u7801\u3001\u9a8c\u8bc1\u7801\u3001\u5b8c\u6574\u4e66\u7c4d\u3001\u8eab\u4efd\u8bc1\u4ef6\u3001\u539f\u59cb\u8d26\u5355\u6216\u672a\u7ecf\u906e\u6321\u7684\u6587\u6863\u3002</p><p>\u672c\u7f51\u7ad9\u63d0\u4f9b\u7684\u662f\u516c\u5f00\u8bf4\u660e\u4e0e\u8054\u7cfb\u65b9\u5f0f\uff0c\u4e0d\u4f1a\u8981\u6c42\u4f60\u4e0a\u4f20\u5e94\u7528\u4e2d\u7684\u539f\u59cb\u5185\u5bb9\u3002</p></section>'
(ROOT/'index.html').write_text(shell('\u5e94\u7528\u652f\u6301\u4e0e\u653f\u7b56','\u5343\u5ea6\u9605\u8bfb\u3001\u6620\u9875\u4e0e\u5c9b\u5c7f\u8d26\u672c\u7684\u6280\u672f\u652f\u6301\u3001\u9690\u79c1\u653f\u7b56\u53ca\u7528\u6237\u534f\u8bae\u3002',body))
(ROOT/'404.html').write_text(shell('\u9875\u9762\u672a\u627e\u5230','\u8bf7\u4ece\u5e94\u7528\u5217\u8868\u91cd\u65b0\u6253\u5f00\u6240\u9700\u9875\u9762\u3002','<section class="hero"><span class="eyebrow">404</span><h1>\u8fd9\u4e2a\u9875\u9762\u6682\u65f6\u627e\u4e0d\u5230\u3002</h1><p>'+a(BASE,'\u8fd4\u56de\u5e94\u7528\u5217\u8868')+'</p><p>'+a('mailto:'+EMAIL,EMAIL)+'</p></section>'))
print('Generated 9 app pages, homepage and 404 page.')
