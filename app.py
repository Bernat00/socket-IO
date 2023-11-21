from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def landing_page():
    if request.method == "POST":
        username = request.form.get('username')
        #    password = request.form.get('password')
        session['id'] = request.form.get('sid')
        session['username'] = username
        return redirect(url_for('chat'))

    return render_template('index.html')


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        packet = {
            'message': request.form.get('message'),
            'recipient': request.form.get('recipient'),
            'username': session['username'],
            'sender': request.form.get('sid')
        }

        socketio.emit('chat_message', packet, to=packet['recipient'])

    return render_template('chat.html')


@socketio.on('connect')
def conected():
    print("connected!")
    socketio.emit("alma", "teszt")


if __name__ == '__main__':
    socketio.run(app)
