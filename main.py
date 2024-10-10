import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="FrontEndcoders", page_icon="🚀", layout="wide")

st.write(
    """
    # 🚀 FrontEndcoders
    ### By Abel Nagy (CPD63P)
    """
)

col1, col2 = st.columns([2, 1])

with col1:
    # GitHub button
    st.markdown(
        """
        <a href="https://github.com/nahu02" target="_blank">
        <button style="
            background-color: #24292e;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            display: inline-flex;
            align-items: center;
            ">
        <svg style="margin-right: 10px;" height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true">
            <path fill="white" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
        </svg>
        Visit my GitHub
        </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.text("")

    # Intro text
    st.markdown(
        """
        Welcome to **FrontEndcoders**, a simple frontend for my thesis project. 
        This application uses [RestfulEncoders](https://github.com/nahu02/RestfulEncoders),
        and showcases the power and flexibility of my custom-built
        [EncoderHubCore](https://github.com/nahu02/EncoderHubCore) library.
        
        You can use any of the encoding models defined there with just a few clicks!
        
        🔍 **Key Features**:
        - Dynamically interchangeable components
        - Modular encoding models
        - Easy configuration for different use cases
        - User-friendly interface for encoding operations

        This demo showcases 2 encoding models, but others could
        be easily added to the service, thanks to its modular architecture.
        
        Ready to give it a try? Let's get started!
        """
    )

with col2:
    # Animation
    st_lottie(
        "https://lottie.host/e910fded-9557-4e6b-ab3f-0f53e76d0e93/W4Ys4QNDsU.json",
        speed=0.1,
        loop=True,
    )

# Placeholder JSON data
st.write("## Placeholder API Response")

placeholder_rest_json = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
).json()

st.json(placeholder_rest_json)
