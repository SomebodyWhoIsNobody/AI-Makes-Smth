# save as utilities_panel.py
import streamlit as st
import requests
import qrcode
from io import BytesIO
import psutil

st.set_page_config(page_title="🛠️ Utilities Panel", layout="wide")
st.title("🛠️ Python Utilities Panel")

# Sidebar for navigation
app = st.sidebar.selectbox("Choose a tool:", [
    "📝 Quick Notes",
    "😂 Random Joke",
    "🌐 IP Lookup",
    "🔳 QR Code Generator",
    "📊 System Monitor"
])

if app == "📝 Quick Notes":
    st.header("📝 Quick Notes")
    note = st.text_area("Write your note here:")
    if st.button("Save Note"):
        with open("notes.txt", "a") as f:
            f.write(note + "\n---\n")
        st.success("Note saved!")

elif app == "😂 Random Joke":
    st.header("😂 Random Joke")
    if st.button("Tell me a joke"):
        resp = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        joke = resp.json().get("joke", "No joke for you!")
        st.write(f"> {joke}")

elif app == "🌐 IP Lookup":
    st.header("🌐 IP Lookup")
    if st.button("Show my IP"):
        resp = requests.get("https://ipinfo.io/json")
        data = resp.json()
        st.json(data)

elif app == "🔳 QR Code Generator":
    st.header("🔳 QR Code Generator")
    text = st.text_input("Enter text or URL:")
    size = st.slider("Box size:", 5, 20, 10)
    if st.button("Generate QR"):
        qr = qrcode.QRCode(box_size=size, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.image(buf)
        st.download_button("Download PNG", data=buf.getvalue(),
                           file_name="qrcode.png", mime="image/png")

elif app == "📊 System Monitor":
    st.header("📊 System Monitor")
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    st.metric("CPU Usage", f"{cpu} %")
    st.metric("Memory Usage", f"{mem} %")
    st.progress(cpu / 100)
    st.progress(mem / 100)
