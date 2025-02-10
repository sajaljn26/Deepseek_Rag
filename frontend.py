import streamlit as st
from rag_pipeline import answer_query,retrieve_docs,llm_model

upload_file = st.file_uploader(
    "Upload a file",
    type = "pdf",
    accept_multiple_files = False
)


user_query = st.text_area("Enter your query",height = 150,placeholder = "Ask Anything")

ask_question = st.button("Ask AI Lawyer")

if ask_question:

    if upload_file:
        st.chat_message("user").write(user_query)
        

        retrieve_docs = retrieve_docs(user_query)
        fixed_response = answer_query(documents=retrieve_docs,model=llm_model,query=user_query)

        #fixed_response = "Hi I am your AI Lawyer. How can I help you?"
        st.chat_message("AI Lawyer").write(fixed_response)
    else:
        st.error("Kindly upload a valid PDF file")