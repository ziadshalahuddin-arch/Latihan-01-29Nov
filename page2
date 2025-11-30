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
