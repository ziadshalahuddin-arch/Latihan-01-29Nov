import streamlit as st

st.title("Latihan: Input & Output")

st.write("Coba isi nama kamu di bawah ini:")

nama = st.text_input("Masukkan nama kamu:")

if nama:
    st.success(f"Halo, {nama}! 🎉")
    st.write("Ini contoh sederhana interaksi di Streamlit.")
