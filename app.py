from flask import Flask,render_template,request
from waitress import serve
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
@app.route("/index")

def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])


def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            filename = file.filename
            file.seek(0, os.SEEK_END)  
            filesize = f"{(file.tell()/1024):.2f}"
            file.seek(0)  
            return render_template('result.html', table=df.to_html(classes='data').replace('NaN',''),filename = filename,filesize = filesize)
    return render_template('index.html')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port="5000")