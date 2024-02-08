from flask import Flask

app = Flask(__name__)

@app.route('/bot')
def bot_response():
    return 'This is the bot response!'

if __name__ == '__main__':
    app.run(debug=True, port=50000)
