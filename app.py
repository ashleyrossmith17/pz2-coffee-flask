from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/menu")
def menu():
    drinks = [
        {"name": "Флэт уайт", "description": "Двойной эспрессо и молоко", "price": 260},
        {"name": "Капучино", "description": "Эспрессо с плотной молочной пеной", "price": 240},
        {"name": "Фильтр-кофе", "description": "Зерно дня и чистый мягкий вкус", "price": 210},
        {"name": "Матча-латте", "description": "Японский чай и овсяное молоко", "price": 290},
        {"name": "Круассан", "description": "Сливочное тесто, выпекаем утром", "price": 190},
        {"name": "Чизкейк", "description": "Нежный сырный крем и ваниль", "price": 320},
    ]
    return render_template("menu.html", drinks=drinks)


if __name__ == "__main__":
    app.run(debug=True)
