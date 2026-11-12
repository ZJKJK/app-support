"""Shared document structure for the website and bundled iOS readers."""
import re

LABELS = {'privacy': '隐私政策', 'terms': '用户协议', 'support': '技术支持'}


def make_document(data, slug, kind):
    app = data['apps'][slug]
    sections = []
    for number, source in enumerate(app[kind], 1):
        title = re.sub(r'^[一二三四五六七八九十]+、', '', source['title'])
        texts = source.get('paragraphs', []) + source.get('items', [])
        sections.append({
            'title': f'{number}. {title}',
            'paragraphs': [
                {'number': f'{number}.{i + 1}', 'text': text,
                 'emphasized': i in source.get('emphasis', [])}
                for i, text in enumerate(texts)
            ],
            'links': source.get('links', []),
        })
    intro = {
        'terms': '请在使用应用前仔细阅读本协议，尤其是以粗体标注的内容来源、功能限制及免责与责任限制条款。',
        'privacy': '本政策说明应用如何处理信息，以及你可以如何管理相关选择。请重点阅读以粗体标注的授权、数据范围和关闭方式。',
        'support': '如需使用帮助、反馈问题或提出隐私请求，请按下方说明联系开发者。',
    }[kind]
    return {
        'title': app['name'] + LABELS[kind],
        'updated': data['updated'].replace('-', '年', 1).replace('-', '月', 1) + '日',
        'version': app.get('terms_version', data['updated']) if kind == 'terms' else data['updated'],
        'introduction': intro,
        'sections': sections,
    }
