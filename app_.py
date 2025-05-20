import streamlit as st
from camera_input_live import camera_input_live
import numpy as np
import cv2

st.set_page_config(page_title="Pokémon Live Scanner", page_icon="🎥")
st.title("Live Pokémon Card Scanner (camera_input_live)")

st.write("""
Prøv denne alternative live-cam:  
`camera_input_live(debounce=200)` giver ~5fps.  
""")

# Brug live kamera-komponent
img_file = camera_input_live(debounce=80)

if img_file is not None:
    # img_file er en UploadedFile-lignende objekt
    img_bytes = img_file.getvalue()
    img_arr = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

    # === STUB: genkendelse (læg model-kald her senere) ===
    label = "Genkender kort…"
    confidence = None

    # Tegn label på frame
    h, w, _ = img_arr.shape
    if confidence is None:
        text = label
    else:
        text = f"{label}: {confidence*100:.1f}%"
    cv2.putText(img_arr, text, (10, h - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    st.image(img_arr, channels="BGR")
