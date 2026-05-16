
# 🩺 CiltAI — Yapay Zeka Destekli Cilt Analiz Projesi

CiltAI, **YOLOv8** tabanlı nesne tespiti (object detection) modelini kullanarak cilt üzerindeki lezyonları analiz eden ve kullanıcılara modern bir web arayüzü üzerinden geri bildirim sağlayan **Flask** tabanlı bir web uygulamasıdır.

Uygulama, sadece tespit yapmakla kalmayıp modelin kararlarını açıklanabilir kılmak için ısı haritaları üretir ve sürekli öğrenme için otomatik etiketleme mekanizması barındırır.

---

## ✨ Özellikler

*   🎯 **YOLOv8 Nesne Tespiti:** Yüklenen görseller üzerinde saniyeler içinde yüksek doğrulukla cilt lezyonu tespiti.
*   🔍 **Açıklanabilir Yapay Zeka (XAI):** Modelin görsel üzerinde tam olarak nereye odaklandığını gösteren **Isı Haritası (Heatmap)** desteği.
*   🔄 **Otomatik Etiketleme (Auto-Labeling):** Kullanıcıların yüklediği yeni fotoğrafların otomatik olarak etiketlenip `datasets/` klasörüne aktarılarak veri setinin sürekli büyümesi.
*   🎨 **Modern & Responsive UI:** Mobil uyumlu, kullanıcı dostu ve **AOS (Animate On Scroll)** kütüphanesi ile zenginleştirilmiş dinamik arayüz.

---

## 📁 Proje Yapısı

```text
├── app/                  # Flask uygulama çekirdeği (Routes, Models, Templates, Static)
├── scripts/              # Model araçları
│   ├── train_yolo.py     # YOLOv8 model eğitim scripti
│   └── analyze_dataset.py# Veri seti analiz ve istatistik aracı
├── datasets/             # Otomatik etiketlenen yeni verilerin toplandığı dizin
├── best.pt               # Eğitilmiş en iyi YOLOv8 model ağırlıkları
├── run.py                # Uygulamayı başlatan ana script
└── requirements.txt      # Proje bağımlılıkları
