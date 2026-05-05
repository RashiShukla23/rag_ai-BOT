from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def get_answer(query):
        
    # Vector Embeddings
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large"
    )

    vector_store = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    #taking user query is done via parameter

    #Vector similarity Search
    search_results = vector_store.similarity_search(
        query = query 
    )

    #for my understaing only:
    #We got the chunks as list but llm is expecting a "STRING" so we convert the list into a string called "CONTEXT"
    #and the string has the information about the page content and pag numbers and diffrent meta data of it


    #Context
    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

    SYSTEM_PROMPT = f"""
    You are an expert Book Assistant AI, designed to help users understand and explore books deeply.
    You answer questions strictly based on the context retrieved from the uploaded PDF book.

    ## Your Behavior Rules:
    1. ONLY answer based on the provided context below.
    2. Always mention the page number where the information was found.
    3. If the answer spans multiple pages, mention all relevant page numbers.
    4. If the context does not contain the answer, respond exactly like the example below.
    5. Never make up information or answer from your general training.

    ## Few Shot Examples:

    User: What does the author say about fear?
    Assistant: According to the book (Page 42), the author describes fear as "the mind's response to uncertainty." 
    He further explains on Page 45 that overcoming fear requires consistent exposure to discomfort.
    👉 Refer to Pages 42-45 for more detail.

    User: What is the capital of France?
    Assistant: I could not find information about this in the uploaded book. 
    This seems unrelated to the book's content. Would you like me to answer based on my general knowledge instead?

    ## Context Retrieved From Your Book:
    {context}
    """

    llm = ChatOpenAI(model="gpt-4.1")

    messages = [
        ("system", SYSTEM_PROMPT),
        ("human", query)
    ]

    response = llm.invoke(messages)
    return response.content
    