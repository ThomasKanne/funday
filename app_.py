import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Live Webcam", page_icon="📷")

st.markdown("### Dit live-kamera")

# Det enkleste: echo-stream uden egen callback
webrtc_streamer(
    key="webcam",
    # Når du kun vil vise videoen og ikke ændre på frames,
    # behøver du ingen ekstra argumenter.
)

st.info(
    "Klik **Start** og giv browseren adgang til kameraet.\n"
    "Virker kun via HTTPS eller localhost."
)
