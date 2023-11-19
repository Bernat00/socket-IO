from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app)

asdasd = input("a")


@app.route('/')
def hello_world():
    return render_template('index.html')


@socketio.on("teszt")  # a conecct működik de a msg nem
def test_message(asd):
    print("alma")
    print(asd)


@socketio.on('connect')
def conected():
    print("connected!")
    socketio.emit("alma", asdasd)


if __name__ == '__main__':
    socketio.run(app)
