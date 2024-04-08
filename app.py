from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '又要到饭了兄弟们，哈哈哈哈哈'

if __name__ == '__main__':
    app.run(debug=True)