import streamlit as st
from indexing import index_pdf
from chat import get_answer

st.title("Book Q&A bot")

uploaded_file = st.file_uploader("Select the pdf you want to upload", type=["pdf"])

if uploaded_file is not None:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if "indexed" not in st.session_state:
        with st.spinner("Indexing your book..."):
            index_pdf(uploaded_file.name)
        st.session_state.indexed = True

    st.success("Book indexed! Ask anything.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.chat_input("Ask anything about the book")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.spinner("Thinking..."):
            response = get_answer(query)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

else:
    st.warning("Please upload a PDF book to get started")