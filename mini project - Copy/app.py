from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os

app = Flask(__name__)

# Folders for media
VIDEO_FOLDER = os.path.join(os.getcwd(), 'videos')
AUDIO_FOLDER = os.path.join(os.getcwd(), 'audios')

os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

ALLOWED_VIDEO = {'mp4', 'avi', 'mkv', 'mov'}
ALLOWED_AUDIO = {'mp3', 'wav', 'ogg'}

tasks = []  # For To-Do app memory store


# ---------- HOME PAGE ----------
@app.route('/')
def home():
    return render_template('home.html')


# ---------- VIDEO PLAYER ----------
@app.route('/video_player')
def video_player():
    video_list = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(tuple(ALLOWED_VIDEO))]
    return render_template('video.html', videos=video_list)

@app.route('/video/<filename>')
def video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

@app.route('/upload_video', methods=['POST'])
def upload_video():
    file = request.files['videoFile']
    if file and file.filename.split('.')[-1].lower() in ALLOWED_VIDEO:
        file.save(os.path.join(VIDEO_FOLDER, file.filename))
    return redirect(url_for('video_player'))

@app.route('/delete_video/<filename>', methods=['POST'])
def delete_video(filename):
    path = os.path.join(VIDEO_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
    return redirect(url_for('video_player'))


# ---------- AUDIO PLAYER ----------
@app.route('/audio_player')
def audio_player():
    audio_list = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith(tuple(ALLOWED_AUDIO))]
    return render_template('audio.html', audios=audio_list)

@app.route('/audio/<filename>')
def audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    file = request.files['audioFile']
    if file and file.filename.split('.')[-1].lower() in ALLOWED_AUDIO:
        file.save(os.path.join(AUDIO_FOLDER, file.filename))
    return redirect(url_for('audio_player'))

@app.route('/delete_audio/<filename>', methods=['POST'])
def delete_audio(filename):
    path = os.path.join(AUDIO_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
    return redirect(url_for('audio_player'))


# ---------- TASK MANAGEMENT ----------
@app.route('/todo')
def todo():
    return render_template('todo.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form['task']
    tasks.append(new_task)
    return redirect(url_for('todo'))

@app.route('/delete_task/<task>', methods=['POST'])
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for('todo'))

@app.route('/update_task', methods=['POST'])
def update_task():
    old = request.form['old_task']
    new = request.form['new_task']
    if old in tasks:
        index = tasks.index(old)
        tasks[index] = new
    return redirect(url_for('todo'))


if __name__ == '__main__':
    app.run(debug=True)
