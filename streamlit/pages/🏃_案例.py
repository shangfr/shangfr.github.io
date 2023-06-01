# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:36:32 2023

@author: shangfr
"""
import json
import requests
import streamlit as st

st.subheader(":orange[🏄 Interact with FastAPI endpoint]")
with st.expander("Demo"):
    API_HOST = 'backend'
    API_PORT = 8500
    backend = f'http://{API_HOST}:{API_PORT}'


    st.caption("计算器")

    option = st.selectbox('请选择计算类型：',
                          ('加', '减', '乘', '除'))
    st.write("")
    st.write("选择数值：")
    x = st.slider("X", 0, 100, 20)
    y = st.slider("Y", 0, 130, 10)
    # converting the inputs into a json format
    inputs = {"operation": option, "x": x, "y": y}
    # when the user clicks on button it will fetch the API
    if st.button('计算'):
        res = requests.post(url=f"{backend}/calculate", data=json.dumps(inputs))
        st.subheader(f"算法API返回值： `{res.json()}`")
