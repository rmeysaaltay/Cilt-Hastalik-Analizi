from flask import Blueprint, render_template
from app.models import db, Analysis

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analyze/<filename>')
def analyze(filename):
    # SAM1-49: Arkadaşının modeli buraya bağlanacak
    # Şimdilik sahte sonuç döndürüyoruz
    result = {
        "sonuc": "Karma Cilt",
        "detay": "T bölgenizde yağlanma, yanaklarda kuruluk tespit edildi.",
        "oneriler": [
            "Günde iki kez yüz yıkama",
            "Nemlendirici kullanın",
            "Haftalık kil maskesi öneririz"
        ],
        "skor": 68
    }

    # SAM1-42, 43: Veritabanına kaydet
    kayit = Analysis(
        filename=filename,
        sonuc=result['sonuc'],
        detay=result['detay'],
        skor=result['skor']
    )
    db.session.add(kayit)
    db.session.commit()

    image_path = f"uploads/{filename}"
    return render_template('result.html', result=result, image_path=image_path, filename=filename)