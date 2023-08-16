import os
import json
category_dict = {
    "wand": "情熱、行動力",
    "cup": "感情、想像力",
    "sword": "思考、知性",
    "pentacle": "資産、安定性"
}
num_dict = {
    "1": "スタート、始まり",
    "2": "バランス、選択",
    "3": "発展、創造性",
    "4": "安定、現実",
    "5": "変化、チャレンジ",
    "6": "美、調和",
    "7": "神秘、探求",
    "8": "継続、力",
    "9": "精神性、リセット",
    "10": "完成、完結",
    "page": "若さ、未熟",
    "knight": "美しさ、行動力",
    "queen": "女性性、受容",
    "king":"自信、権力"
}

with open('card_bk.json',encoding="utf-8_sig") as f:
    di = json.load(f)
card_data = di
for category, data in card_data["minor"].items():
    for num, dat in data.items():
        text = category_dict[category] + "-" + num_dict[num]
        dat["description"] = dat["description"] + "("+ text +")"

with open('card.json', 'w', encoding='utf-8-sig') as f:
    json.dump(card_data, f, indent=4, ensure_ascii=False)