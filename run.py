from flask import Flask
import led

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/led')
def ledd():
    led.led(5)
    return 'led!\n'

if __name__ == '__main__':
    app.run()
