from flask import Flask, render_template, request
import random

app = Flask(__name__)

# タロットカードのデータ (例)
tarot_cards = {
    # カードデータの定義
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # カードの選択と位置の取得
        selected_cards = []
        for i in range(1, 11):
            card_type = request.form.get(f"card_type_{i}")
            card_id = request.form.get(f"card_id_{i}")
            is_reversed = request.form.get(f"reversed_{i}")
            selected_cards.append({"type": card_type, "id": card_id, "reversed": is_reversed})

        # カードの説明と画像データを格納するリスト
        card_details = [1,2,3,4,5,6,7,8,9,10,"キング"]

        # 他の処理をここに追加してください

        return render_template("result.html", card_details=card_details)

    return render_template("index.html", tarot_cards=tarot_cards)


if __name__ == "__main__":
    app.run(debug=True)
