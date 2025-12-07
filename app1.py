import streamlit as st
import qrcode
import io
st.title("QR Code Generator")
text = st.text_input("Enter text/URL:")

if st.button("Generate"):
    if text != "":
        qr = qrcode.make(text)
        buf = io.BytesIO()
        qr.save(buf, format="PNG")
        img_bytes = buf.getvalue()
        st.image(img_bytes)
    else:
        st.error("Please enter some text.")
else:
    st.write("Enter text and click Generate.")
