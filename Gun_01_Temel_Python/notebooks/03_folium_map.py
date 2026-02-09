import folium
import seaborn as sns
import random

# Veriyi yukle
df = sns.load_dataset("iris")

print("Folium haritasi hazirlaniyor...")

# Senaryo: Veriler Istanbul'daki bir parktan toplanmis olsun.
# Istanbul koordinatlari (yaklasik): 41.0082, 28.9784
base_lat = 41.0082
base_lon = 28.9784

# Haritayi baslat
m = folium.Map(location=[base_lat, base_lon], zoom_start=15)

# Ornekleme: Her turden 5 cicegi haritaya rastgele dagitalim
# (Gercek veri setinde koordinat olmadigi icin 'mock' data uretiyoruz)
subset = df.groupby("species").head(5).reset_index()

colors = {"setosa": "red", "versicolor": "green", "virginica": "blue"}

for index, row in subset.iterrows():
    # Koordinatlari hafifce rastgele kaydir (daginik gozukmesi icin)
    lat = base_lat + random.uniform(-0.005, 0.005)
    lon = base_lon + random.uniform(-0.005, 0.005)

    # Popup icerigi: HTML formatinda bilgi
    popup_text = f"""
    <b>Tur:</b> {row["species"]}<br>
    <b>Sepal Length:</b> {row["sepal_length"]}<br>
    <b>Sepal Width:</b> {row["sepal_width"]}<br>
    <b>Petal Length:</b> {row["petal_length"]}<br>
    <b>Petal Width:</b> {row["petal_width"]}<br>
    """

    # Haritaya isaretci (Marker) ekle
    folium.CircleMarker(
        location=[lat, lon],
        radius=8,
        popup=popup_text,
        color=colors[row["species"]],
        fill=True,
        fill_color=colors[row["species"]],
    ).add_to(m)

# Haritayi kaydet
m.save("iris_map.html")
print("Harita 'iris_map.html' olarak kaydedildi. Lutfen dosyayi acin.")
