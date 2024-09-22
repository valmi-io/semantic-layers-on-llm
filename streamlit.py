import streamlit as st 
import datetime
from main import initiate_llm


def log(message):
    current_time = datetime.datetime.now()
    milliseconds = current_time.microsecond // 1000
    timestamp = current_time.strftime(
        "[%Y-%m-%d %H:%M:%S.{:03d}] ".format(milliseconds)
    )
    st.text(timestamp + message)


question = st.text_input("Put your question here: ", key="input")


if st.button("Submit", type="primary"):
    if question == "":
        log("Please enter your question & hit enter")
    else:
        generator = initiate_llm(question)
        log("trying to generate parameters from llm...")
        params = next(generator)
        st.info(f"llm generated parameters: {params}")
        log("trying to fetch data from source data...")
        data = next(generator)
        st.dataframe(data)
