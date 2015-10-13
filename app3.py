from flask import Flask
app = Flask(__name__)

@app.route("/hello3/<value>")
def hello():
    return value

if __name__ == "__main__":
    app.run()
