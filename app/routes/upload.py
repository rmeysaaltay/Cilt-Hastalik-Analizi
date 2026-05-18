import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    # SAM1-34: Kullanıcı fotoğraf yükleyebilmeli (GET)
    if request.method == 'POST':
        # SAM1-45: Fotoğraf yükleme alanı (POST)
        file = request.files.get('photo')

        # SAM1-36: Kullanıcı hatalı yüklemede uyarı almalı
        if not file or file.filename == '':
            return render_template('upload.html', error='Lütfen bir dosya seçin.')
        
        if not allowed_file(file.filename):
            return render_template('upload.html', error='Sadece PNG, JPG, JPEG yükleyebilirsiniz.')

        filename = secure_filename(file.filename)
        save_path = os.path.join('app/static/uploads', filename)
        file.save(save_path)

        # SAM1-49: Yüklenen fotoğraf verisini analiz sürecine gönder
        return redirect(url_for('analysis.analyze', filename=filename))

    # SAM1-45: Fotoğraf yükleme alanı
    return render_template('upload.html')