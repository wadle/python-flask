from flask import Flask

app = Flask(__name__)

info = [
    {
        "name": "Jitendra Wadle",
        "age": 33
    }
]

@app.get("/info") #http://127.0.0.1:5000/info
def get_info():
    return {"info": info}