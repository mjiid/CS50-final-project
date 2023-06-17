import moviepy.editor as mp
from found import ALLOWED_EXTENSIONS, app
import os

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_audio(form,filename):
    form.file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    myClip = mp.VideoFileClip(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    myClip.audio.write_audiofile(str(app.config['UPLOAD_FOLDER'][:-5]) + 'results\\' +  str(filename[:-4]).replace("_", " ") + '.mp3')

def save_audio(form, filename):
   form.file.data.save(str(app.config['UPLOAD_FOLDER'][:-5]) + 'results\\' +  str(filename[:-4]).replace("_", " ") + '.mp3')

