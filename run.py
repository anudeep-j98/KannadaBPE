import streamlit as st
import json
import ast
from utils import *

stoi, itos = load_tokenizer()

# Streamlit app structure
st.title("Kannada Text Encoder and Decoder")

# Tabs for encoding and decoding
tab1, tab2 = st.tabs(["Encode", "Decode"])

with tab1:
    st.header("Encode Kannada Text")
    input_text = st.text_area("Enter Kannada text to encode:")
    input_text = clean_text(input_text)
    if st.button("Encode"):
        if input_text:
            encoded_result = encode_text(input_text)
            st.success("Encoded Result:")
            st.write(encoded_result)
        else:
            st.error("Please enter some text to encode.")

with tab2:
    st.header("Decode Kannada Text")
    input_encoded = st.text_area("Enter encoded integers (comma-separated):")
    if st.button("Decode"):
        if input_encoded:
            try:
                input_encoded = input_encoded.strip()
                encoded_list = ast.literal_eval(input_encoded)
                decoded_result = decode_tokens(encoded_list)
                st.success("Decoded Result:")
                st.write(decoded_result)
            except ValueError:
                st.error("Invalid input! Please enter comma-separated integers.")
        else:
            st.error("Please enter encoded integers to decode.")
