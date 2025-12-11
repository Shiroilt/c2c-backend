from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "cloud2cloud MVP backend running..."}
