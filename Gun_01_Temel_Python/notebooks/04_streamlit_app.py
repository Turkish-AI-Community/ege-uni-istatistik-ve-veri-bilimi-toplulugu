import streamlit as st
import seaborn as sns
import plotly.express as px

# Sayfa Basligi
st.title("🌱 Iris Veri Analizi Paneli")
st.markdown(
    "Bu panel **Streamlit** kullanılarak Python ile yapılmıştır. HTML/CSS gerekmez."
)

# Veriyi yukle
df = sns.load_dataset("iris")

# Sidebar (Yan Panel)
st.sidebar.header("Filtreleme Secenekleri")
selected_species = st.sidebar.multiselect(
    "Gormek istediginiz turleri secin:",
    options=df["species"].unique(),
    default=df["species"].unique(),
)

# Filtreleme islemi
filtered_df = df[df["species"].isin(selected_species)]

# Veri Tablosunu Goster
st.subheader("Veri Seti Onizleme")
st.dataframe(filtered_df.head())

# Istatistikler
st.write(f"Secilen veri sayisi: **{len(filtered_df)}**")

# Grafik Cizimi (Plotly ile)
st.subheader("Gorsellestirme")
x_axis = st.selectbox("X Ekseni:", df.columns[:-1], index=0)
y_axis = st.selectbox("Y Ekseni:", df.columns[:-1], index=1)

if st.button("Grafigi Guncelle"):
    fig = px.scatter(
        filtered_df, x=x_axis, y=y_axis, color="species", title=f"{x_axis} vs {y_axis}"
    )
    st.plotly_chart(fig)

# Nasil Calistirilir Bilgisi (Kullaniciya gostermek icin)
st.sidebar.markdown("---")
st.sidebar.info("Calistirmak icin terminale: `streamlit run bu_dosya.py` yazin.")
