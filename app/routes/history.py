from flask import Blueprint, render_template
from app.models import Analysis

history_bp = Blueprint('history', __name__)

@history_bp.route('/history')
def history():
    # SAM1-42, 43, 52: Geçmiş analizleri tarihe göre sırala
    analizler = Analysis.query.order_by(Analysis.created_at.desc()).all()
    return render_template('history.html', analizler=analizler)