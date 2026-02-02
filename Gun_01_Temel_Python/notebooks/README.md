# Veri Bilimi ve Web Uygulaması Scriptleri

Bu klasör, çeşitli veri analizi, görselleştirme ve web uygulaması yeteneklerini gösteren Python scriptlerini içerir.

## Gereksinimler

Bu proje bağımlılık yönetimi için `uv` kullanır.

1. **`uv` Kurulumu** (Eğer yüklü değilse):

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Bağımlılıkların Yüklenmesi**:

    ```bash
    uv sync
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
