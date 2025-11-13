from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask app deployed successfully on Vercel using UV!"

if __name__ == "__main__":
    app.run()
