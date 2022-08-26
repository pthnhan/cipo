from algo import find_overlap
from flask import Flask

app = Flask(__name__)

@app.route("/")
def cipo():
    mes = find_overlap(data_folder="data", class_=[9, 36, 1], threshold1=30, threshold2=70)
    return mes

if __name__ == "__main__":
    app.run(host='console.pthnhan.online', port='2609', debug=True)
