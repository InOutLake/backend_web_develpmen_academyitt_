from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        message = request.form["message"]

        phone_regex = re.compile(r"^(\+\d{11}|\d{11})$")
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        errors = []
        if not phone_regex.match(phone):
            errors.append("Номер телефона набран неверно")
        if not email_regex.match(email):
            errors.append("Почта не соответствует формату example@example.ex")
        if errors:
            return render_template("contact_us.html", errors=errors, **request.form)
        
        message_out = f"Имя: {name},\nТелефон: {phone},\nEmail: {email},\nСообщение: {message}"
        message_out = message_out.splitlines()

        return render_template("contact_us.html", message_out=message_out)
    return render_template("contact_us.html")

if __name__ == "__main__":
    app.run(debug=True)