# İnsan Kaynakları Analitiği: Çalışan Ayrılma Tahmini

Bu proje, bir şirketteki çalışanların hangi faktörlere bağlı olarak işten ayrılma eğiliminde olduğunu analiz eder.

## 📋 Proje Hakkında

Bu analiz, IBM HR Analytics veri setini kullanarak şu soruları yanıtlamayı hedefler:
- Hangi faktörler çalışan ayrılmasını etkiliyor?
- Departman bazında ayrılma oranları nasıl dağılıyor?
- Maaş ve memnuniyet ile ayrılma arasında nasıl bir ilişki var?
- Personel devir hızı nedir ve nasıl hesaplanır?

## 🛠️ Kullanılan Teknolojiler

- **Python 3.x**
- **Pandas** - Veri manipülasyonu
- **Matplotlib & Seaborn** - Görselleştirme
- **Scikit-learn** - Makine öğrenmesi (Logistic Regression)
- **Jupyter Notebook** - İnteraktif analiz

## 📁 Proje Yapısı

```
hr-churn-analysis/
├── data/                    # Veri setleri
├── notebooks/               # Jupyter notebooks
│   └── analysis.ipynb       # Ana analiz notebook'u
├── outputs/                 # Grafikler ve raporlar
├── requirements.txt         # Python bağımlılıkları
└── README.md                # Bu dosya
```

## 🚀 Kurulum

1. Virtual environment oluşturun:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

3. Jupyter Notebook'u başlatın:
```bash
jupyter notebook
```

## 📊 Personel Devir Hızı Formülü

```
Personel Devir Hızı = (Dönem İçinde Ayrılanlar / ((Dönem Başı + Dönem Sonu Çalışan Sayısı) / 2)) × 100
```

## 👤 Geliştirici

Almira Sultan Pamukçu - İnsan Kaynakları Analitiği Projesi
