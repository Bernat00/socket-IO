from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app)


asdasd = input("a")

users = []


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/chat')
def chat():
    # betölteni db-ből üzeneteket, majd azt küldeni
    # db_change-után emittelni a változásokat
    return render_template('chat.html')


@socketio.on("teszt")  # a conecct működik de a msg nem
def test_message(username):
    print(username)
    # session['username'] = username            nem lehet editálni a cookie-t csak https request-response dologoknál lehet
    # (magyarul form-os login kell vagy request.sid alapú)
    socketio.emit('redirect', {'url': url_for('chat')})


@socketio.on('connect')
def conected():
    print("connected!")
    socketio.emit("alma", asdasd)


@socketio.on('message')
def receave_msg(msg):
    print(msg)


if __name__ == '__main__':
    socketio.run(app)
