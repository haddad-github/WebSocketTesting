from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('button_clicked')
def handle_button_click(item):
    # Broadcast the button clicked event and the item (rock, paper, scissors) to all clients
    socketio.emit('button_clicked', item)

if __name__ == '__main__':
    socketio.run(app)

