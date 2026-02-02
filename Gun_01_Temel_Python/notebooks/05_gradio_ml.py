import gradio as gr
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier

# 1. Model Egitimi (Arka Plan)
print("Model egitiliyor...")
df = sns.load_dataset("iris")
X = df.drop("species", axis=1)
y = df["species"]

# Basit bir KNN (En yakin komsu) modeli
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)


# 2. Tahmin Fonksiyonu
def cicek_tahmin_et(sepal_len, sepal_wid, petal_len, petal_wid):
    # Kullanicidan gelen veriyi modelin anlayacagi formata cevir
    prediction = model.predict([[sepal_len, sepal_wid, petal_len, petal_wid]])
    return prediction[0]


# 3. Gradio Arayuzu
# Inputs: Kullanicinin girecegi degerler
# Outputs: Cikan sonuc
demo = gr.Interface(
    fn=cicek_tahmin_et,
    inputs=[
        gr.Slider(0, 10, label="Sepal Length (Canak Yaprak Uzunlugu)"),
        gr.Slider(0, 10, label="Sepal Width (Canak Yaprak Genisligi)"),
        gr.Slider(0, 10, label="Petal Length (Tac Yaprak Uzunlugu)"),
        gr.Slider(0, 10, label="Petal Width (Tac Yaprak Genisligi)"),
    ],
    outputs="text",
    title="🌸 Iris Cicegi Tur Tahminleyicisi",
    description="Degerleri girin, Yapay Zeka hangi tur oldugunu tahmin etsin.",
)

if __name__ == "__main__":
    demo.launch()
