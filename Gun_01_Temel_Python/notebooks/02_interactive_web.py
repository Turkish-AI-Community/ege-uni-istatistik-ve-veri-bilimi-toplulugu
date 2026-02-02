import plotly.express as px
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import seaborn as sns

# Veriyi yukle
df = sns.load_dataset("iris")

# ---------------------------------------------------------
# BOLUM 1: PLOTLY (3 Boyutlu ve Interaktif)
# ---------------------------------------------------------
print("Plotly 3D grafik olusturuluyor...")

# 3 Boyutlu Scatter Plot
# Iris veri seti 3D gorsellestirme icin harikadir
fig = px.scatter_3d(
    df,
    x="sepal_length",
    y="sepal_width",
    z="petal_width",
    color="species",
    title="Plotly: 3D Iris Analizi (Cevirmek icin surukleyin)",
)

# Grafigi tarayicida ac
fig.show()

# ---------------------------------------------------------
# BOLUM 2: BOKEH (Web Icin Yuksek Performans)
# ---------------------------------------------------------
print("Bokeh grafigi olusturuluyor...")

# Ciktiyi bir HTML dosyasina kaydet
output_file("bokeh_iris.html")

# Veriyi Bokeh formatina cevir
source = ColumnDataSource(df)

# Figur olustur
p = figure(
    title="Bokeh: Iris Sepal Analizi",
    x_axis_label="Sepal Length",
    y_axis_label="Sepal Width",
    tools="pan,wheel_zoom,box_zoom,reset,save",
)

# Renk haritasi (Basitlestirilmis manuel renklendirme)
colors = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
df["color"] = df["species"].apply(lambda x: colors[x])
source = ColumnDataSource(df)

# Daireleri ciz
# size=10: Daire boyutu, alpha=0.6: Saydamlik
circles = p.scatter(
    "sepal_length",
    "sepal_width",
    source=source,
    color="color",
    size=10,
    alpha=0.6,
    legend_field="species",
)

# Hover (Uzerine gelince bilgi gosterme) aracini ekle
hover = HoverTool()
hover.tooltips = [
    ("Tur", "@species"),
    ("Uzunluk", "@sepal_length"),
    ("Genislik", "@sepal_width"),
]
p.add_tools(hover)

# Dosyayi olustur ve ac
show(p)
