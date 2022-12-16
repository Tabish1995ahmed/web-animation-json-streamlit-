import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


def get(path:str):
    with open(path,"r") as p:
        return json.load(p)
    
path = get("./ani.json")
st_lottie(path)


def get_url(url:str):
    r = requests.grt(url)
    if r.status_code !=200:
        return None
    return r.json()
url = get_url ("https://assets1.lottiefiles.com/packages/lf20_10jxod3a.json")
st_lottie(url)
