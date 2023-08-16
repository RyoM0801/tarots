from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__, static_folder='./img')

# サンプルのカードデータ
with open('card.json',encoding="utf-8_sig") as f:
    di = json.load(f)
card_data = di

transe_dict = {
    "wand": "ワンド",
    "cup": "カップ",
    "sword": "ソード",
    "pentacle": "ペンタクル",
    "page": "ページ",
    "knight": "ナイト",
    "queen": "クイーン",
    "king": "キング"
}

dir_path = os.path.join("img")
files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_card_data", methods=["POST"])
def get_card_data():
    card_type = request.form.get("card_type")
    reversed = request.form.get("reversed")
    if card_type == "major":
        rank = request.form.get("major_rank")
        ret_data = card_data[card_type][rank]
        src = ""
        for file in files_file:
            if "大アルカナ_"+rank in file:
                src = file
                break
        ret_data["src"] = os.path.join(dir_path, src).replace("\\", "/")
        ret_data["words"] = ret_data["negative_words"] if reversed == "yes" else ret_data["positive_words"]
        return jsonify(ret_data)
    elif card_type == "minor":
        suit = request.form.get("minor_suit")
        rank = request.form.get("minor_rank")
        ret_data = card_data[card_type][suit][rank]
        for file in files_file:
            suit = transe_dict[suit] if suit in transe_dict.keys() else suit
            rank = transe_dict[rank] if rank in transe_dict.keys() else rank
            src = ""
            if "小アルカナ_"+suit+"_"+rank in file:
                src = file
                break
        ret_data["src"] = os.path.join(dir_path, src).replace("\\", "/")
        ret_data["words"] = ret_data["negative_words"] if reversed == "yes" else ret_data["positive_words"]
        return jsonify(ret_data)
    return jsonify({"error": "Card data not found"})

if __name__ == "__main__":
    app.run(debug=True)
