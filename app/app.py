from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Jenkins CI/CD Practical</h1>
    <h2>Welcome! Version 1</h2>
    <p>Application deployed successfully using Jenkins.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
