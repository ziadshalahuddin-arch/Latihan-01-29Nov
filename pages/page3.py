import streamlit as st

st.title("Latihan: Settings & Widgets")

st.write("Coba ubah preferensi di bawah:")

tema = st.selectbox(
    "Pilih tema warna:",
    ["Default", "Light", "Dark"]
)

notif = st.checkbox("Aktifkan notifikasi")

volume = st.slider("Atur volume:", 0, 100, 50)

st.write("---")
st.subheader("Hasil Pengaturan")

st.write(f"🎨 Tema: **{tema}**")
st.write(f"🔔 Notifikasi: **{'Aktif' if notif else 'Mati'}**")
st.write(f"🔊 Volume: **{volume}%**")
