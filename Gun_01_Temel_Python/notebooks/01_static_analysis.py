# Gerekli Kutuphaneler
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veri Setini Yukle
# Seaborn icerisinde Iris veri seti hazir gelir
print("Veri seti yukleniyor...")
df = sns.load_dataset("iris")

# Veri setinin ilk 5 satirini goster
print("Ilk 5 satir:")
print(df.head())

# ---------------------------------------------------------
# BOLUM 1: MATPLOTLIB (Temel Cizim)
# ---------------------------------------------------------
print("\nMatplotlib grafigi hazirlaniyor...")

plt.figure(figsize=(10, 6))
# X ekseni: Canak Yaprak Uzunlugu, Y ekseni: Tac Yaprak Uzunlugu
plt.scatter(df["sepal_length"], df["petal_length"], c="blue", alpha=0.5)

plt.title("Matplotlib: Iris Sepal vs Petal Uzunlugu")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# BOLUM 2: SEABORN (Istatistiksel Guzellik)
# ---------------------------------------------------------
print("\nSeaborn Pairplot hazirlaniyor (Bu biraz zaman alabilir)...")

# Pairplot: Tum degiskenlerin birbirleriyle iliskisini tek seferde cizer
# 'hue' parametresi renklendirme icin kullanilir (Turlerine gore)
sns.set_theme(style="ticks")
sns.pairplot(df, hue="species", palette="husl")

print("Grafigi gormek icin pencereye bakin.")
plt.show()
