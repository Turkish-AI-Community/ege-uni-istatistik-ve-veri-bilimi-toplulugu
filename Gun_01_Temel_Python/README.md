# Gün 1 - Temel Python

**Eğitmen:** Uğurcan Uzunkaya

## İçerik

Bu bölümde, temel Python kullanımına dair kavramlar ile Python'un güçlü veri bilimi ve görselleştirme araçları ele alınmaktadır. Ayrıca `uv` paket yöneticisi kullanılarak nasıl proje ayağa kaldırılacağı, bağımlılıkların nasıl yönetileceği ve makine öğrenmesi/web arayüzü gibi konular işlenmektedir.

## Dosyalar ve Klasörler

### 📂 Kaynaklar (`/kaynaklar`)

- `Veri Analizi Araçları.pdf`: Ders sırasında kullanılan ana sunum dosyası ve veri analizine giriş temel kavramları.

### 📓 Notebooks ve Kodlar (`/notebooks`)

Bu klasörde veri analizi, veri görselleştirme ve web uygulaması yapımını gösteren Python scriptleri ve proje dosyaları bulunmaktadır:

- `01_static_analysis.py`: Matplotlib ve Seaborn kullanılarak Iris veri seti üzerinde statik analiz çalışmaları.
- `02_interactive_web.py`: Plotly ve Bokeh kütüphaneleriyle oluşturulan interaktif web grafikleri.
- `03_folium_map.py`: Folium kullanılarak işaretleyicilerle (marker) yapılan coğrafi veri analizi ve haritalandırma uygulaması.
- `04_streamlit_app.py`: Streamlit çatısı ile geliştirilen interaktif veri analizi paneli uygulaması.
- `05_gradio_ml.py`: Gradio ile oluşturulmuş basit bir makine öğrenimi model dağıtım (deployment) arayüzü.
- `pyproject.toml`, `requirements.txt`, `uv.lock`: Projenin paket yönetimi (uv) bağımlılıklarını ve yapılandırmasını içeren dosyalar.
- `bokeh_iris.html`, `iris_map.html`: Kodların çalıştırılması sonucu üretilmiş interaktif HTML formatındaki grafikler.
- `README.md`: Scriptlerin nasıl çalıştırılacağını (ör. `uv run`) anlatan kullanım rehberi.
