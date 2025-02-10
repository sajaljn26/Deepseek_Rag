# AI Lawyer - Legal Document Query Application

This project is an AI-powered legal assistant that allows users to upload PDF documents and ask legal questions. The AI retrieves relevant information from the uploaded document and provides answers based on the content.

## Features
- **PDF Upload**: Upload legal documents in PDF format.
- **Query Interface**: Ask questions related to the uploaded document.
- **Document Retrieval**: Uses advanced retrieval techniques to find relevant sections in the document.
- **AI-Powered Answers**: Provides accurate answers using an LLM (Large Language Model).

## Technologies Used
- **Streamlit**: For building the interactive web interface.
- **LangChain**: For document loading, splitting, and vector storage.
- **PDFPlumber**: To extract text from PDF documents.
- **FAISS**: For vector-based document retrieval.
- **HuggingFace Transformers**: For embedding generation using pre-trained models.
- **DeepSeek R1 Distill LLaMA 70B**: For powerful, accurate large language model responses.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install streamlit langchain pdfplumber faiss-cpu sentence-transformers
  ```

### Project Structure
```
├── app.py                 # Main Streamlit app
├── rag_pipeline.py        # RAG (Retrieval-Augmented Generation) pipeline functions
├── pdfs/                  # Directory to store uploaded PDFs
├── vectorstore/           # Directory for FAISS vector database
└── README.md              # Project documentation