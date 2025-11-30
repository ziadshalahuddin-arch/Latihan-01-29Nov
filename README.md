# Latihan-01-29Nov
Latihan 01 PrakBigData (29 Nov)

import streamlit as st

st.title("Latihan: Input & Output")

st.write("Coba isi nama kamu di bawah ini:")

nama = st.text_input("Masukkan nama kamu:")

if nama:
    st.success(f"Halo, {nama}! 🎉")
    st.write("Ini contoh sederhana interaksi di Streamlit.")

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Latihan: Visualisasi Data")

st.write("Grafik sederhana hubungan x dan sin(x)")

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.set_title("Grafik sin(x)")

st.pyplot(fig)

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
