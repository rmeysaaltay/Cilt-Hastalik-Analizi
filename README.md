# CiltAI — Yapay Zeka Destekli Cilt Analiz Projesi

Bu proje, YOLOv8 modelini kullanarak cilt lezyonlarını analiz eden ve kullanıcılara modern bir arayüz üzerinden tavsiyeler sunan bir Flask web uygulamasıdır.

## 🚀 Başlangıç

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

### 1. Gereksinimler
- Python 3.8+
- Sanal ortam (venv)

### 2. Kurulum ve Çalıştırma
```bash
# Proje klasörüne gidin
cd "skin-analysis-project kopyası"

# Sanal ortamı aktif edin
source venv/bin/activate

# Gerekli paketleri yükleyin (Eğer eksikse)
pip install -r requirements.txt

# Uygulamayı başlatın
python run.py
```

### 3. Kullanım
Tarayıcınızdan `http://127.0.0.1:5001` adresine giderek analiz yapmaya başlayabilirsiniz.

## 📁 Proje Yapısı
- `app/`: Flask uygulama çekirdeği (Routes, Models, Templates, Static).
- `scripts/`: Model eğitimi (`train_yolo.py`) ve veri seti analiz (`analyze_dataset.py`) araçları.
- `datasets/`: Otomatik etiketlenen yeni verilerin toplandığı alan.
- `best.pt`: Eğitilmiş YOLOv8 model ağırlıkları.

## ✨ Özellikler
- **YOLOv8 Analizi:** Saniyeler içinde hastalık tespiti.
- **Explainability (Isı Haritası):** Modelin odaklandığı alanın görselleştirilmesi.
- **Auto-Labeling:** Yüklenen her fotoğrafın otomatik etiketlenerek veri setine katılması.
- **Modern UI:** AOS animasyonlu, responsive tasarım.

---
*Tıbbi Uyarı: Bu uygulama sadece bilgilendirme amaçlıdır. Kesin teşhis için doktora danışılmalıdır.*

