from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
  return "Welcome to the blue deployment"

@app.route("/hello")
def hello_world():
    return "Hello, World! Blue deployment"
if __name__ == "__main__":
    app.run(host='0.0.0.0')