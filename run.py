from flask import Flask
import alarm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/alarm')
def alarm0():
    alarm.alarm()
    return 'alarm!\n'

if __name__ == '__main__':
    app.run()
