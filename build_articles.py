import re
import json

with open("data/pdpl_ndgp_ar.txt", encoding="utf-8") as f:
    text = f.read()

text = text.replace("\u200c", "").replace("\u200b", "").replace("\u0640", "")

parts = re.split(r"^(المادة .+):\s*$", text, flags=re.MULTILINE)
headings = parts[1::2]
bodies = parts[2::2]

articles = []
for number, (heading, body) in enumerate(zip(headings, bodies), start=1):
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    clean_text = re.sub(r"[ \t]+", " ", "\n".join(lines))
    articles.append({"article_no": number, "label": heading, "text": clean_text})

print(len(articles))
print(articles[10]["label"])
print(articles[19]["label"])
print(articles[31]["label"], "|", articles[31]["text"])
print(len(articles[5]["text"]))

short = [a["article_no"] for a in articles if len(a["text"]) < 80]
print(short)

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)