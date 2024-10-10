from os import getenv

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# API base URL
BASE_URL = getenv("API_URL")


def get_encoders():
    try:
        response = requests.get(f"{BASE_URL}/encoders")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to fetch encoders: {str(e)}")
        return []


def get_encoder_description(encoder_name):
    try:
        response = requests.get(f"{BASE_URL}/encoders/{encoder_name}")
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        st.error(f"Failed to fetch description for {encoder_name}: {str(e)}")
        return None


def encode_message(encoder_name, message):
    try:
        response = requests.post(f"{BASE_URL}/encoders/{encoder_name}", json=message)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        st.error(f"Failed to encode message using {encoder_name}: {str(e)}")
        return None
