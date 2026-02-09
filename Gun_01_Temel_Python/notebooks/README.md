# Veri Bilimi ve Web Uygulaması Scriptleri

Bu klasör, çeşitli veri analizi, görselleştirme ve web uygulaması yeteneklerini gösteren Python scriptlerini içerir.

## Gereksinimler

### Adım 1: uv Kurulumu (Eğer yüklü değilse)

Mac/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Adım 2: Proje Kurulumu

```bash
uv init data_workshop
cd data_workshop
uv python pin 3.11  # Uyumluluk için önemli!
uv add matplotlib seaborn pandas plotly bokeh folium streamlit gradio taipy grafanalib scikit-learn
```

## Scriptler

### 1. Statik Analiz (Matplotlib & Seaborn)

Iris veri setini kullanarak temel istatistiksel grafikler.

```bash
uv run 01_static_analysis.py
```

### 2. İnteraktif Web Grafikleri (Plotly & Bokeh)

İnteraktif 3D grafikler ve yüksek performanslı web görselleştirmeleri.

```bash
uv run 02_interactive_web.py
```

### 3. Coğrafi Analiz (Folium)

İşaretçilerle harita görselleştirmesi.

```bash
uv run 03_folium_map.py
```

### 4. Streamlit Uygulaması

Tamamen interaktif bir veri analizi paneli.

```bash
uv run streamlit run 04_streamlit_app.py
```

### 5. Makine Öğrenimi Arayüzü (Gradio)

Basit bir Makine Öğrenimi model dağıtım arayüzü.

```bash
uv run 05_gradio_ml.py
```

## Geliştirme

Kodu biçimlendirme ve denetleme:

```bash
uv run ruff check .
uv run ruff format .
```
