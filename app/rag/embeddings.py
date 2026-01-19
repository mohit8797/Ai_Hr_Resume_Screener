# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# def get_embeddings():
#     return GoogleGenerativeAIEmbeddings(
#         model="models/embedding-001"
#     )

from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
