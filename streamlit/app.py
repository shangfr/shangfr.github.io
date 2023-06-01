# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:11:08 2023

@author: shangfr
"""

import streamlit as st

st.set_page_config(
    page_title="FollowAI's Home",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/shangfr/shangfr.github.io',
        'Report a bug': "https://github.com/shangfr/shangfr.github.io",
        'About': "# FollowAI. Simple example of usage of streamlit and FastAPI for ML model serving."
    }
)

st.header(":white[🧊 FollowAI]")

tab1, tab2 = st.tabs(["Streamlit","Web"])


with tab1:
    st.subheader(":orange[Apps]")
    st.markdown("- 🚗 [Data-Follower](https://shangfr-data-follower-app-mokm7x.streamlit.app/)")
    st.markdown("- 🌐 [Py-Depgraph](https://shangfr-pydepgraph-app-gh2ivs.streamlit.app/)")
    st.markdown("- 🔊 [TTS](https://shangfr-streamlittts-app-xvews2.streamlit.app/)")
    st.markdown("- 💬 [Chatspider](https://shangfr-chatspider--home-lj3qer.streamlit.app/)")
    st.markdown("- 📚 [Aesopica](https://shangfr-aesopica-app-xr2547.streamlit.app/)")


with tab2:
    st.subheader(":orange[Tools]")
    st.markdown("- 🏠 [Home](https://shangfr.site/)")
    st.markdown("- 🌌 [Apps](https://app.shangfr.site/)")
    st.markdown("- 📚 [Portainer](https://portainer.shangfr.site/)")

