from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('button_clicked')
def handle_button_click(item):
    socketio.emit('button_clicked', item)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
