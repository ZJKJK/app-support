"""Export the same policy text and hierarchy used by the public website."""
from pathlib import Path
import argparse
import json
from legal_documents import make_document, LABELS

parser = argparse.ArgumentParser()
parser.add_argument('--app', required=True, choices=['qiandu', 'pdfworkbench', 'islandledger'])
parser.add_argument('--output', required=True, type=Path)
parser.add_argument('--legacy-output', type=Path)
args = parser.parse_args()
data = json.loads(Path(__file__).with_name('content.json').read_text())
documents = {LABELS[k]: make_document(data, args.app, k) for k in ['privacy', 'terms']}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(documents, ensure_ascii=False, indent=2) + '\n')
if args.legacy_output:
    legacy = {}
    for label, doc in documents.items():
        lines = [doc['title'], '更新日期：' + doc['updated'], doc['introduction']]
        for section in doc['sections']:
            lines.append(section['title'])
            lines.extend(p['number'] + ' ' + p['text'] for p in section['paragraphs'])
            lines.extend(link['label'] + '：' + link['url'] for link in section['links'])
        legacy[label] = lines
    args.legacy_output.write_text(json.dumps(legacy, ensure_ascii=False, indent=2) + '\n')
print('Exported offline privacy policy and terms for ' + args.app)
