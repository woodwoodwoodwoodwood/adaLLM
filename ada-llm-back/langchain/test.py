from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
from langchain.schema import Document
from langchain.schema.retriever import BaseRetriever
from typing import List
from pydantic import Field
from langchain.document_loaders import DirectoryLoader
import os

# 设置 tesseract 的路径
os.environ["TESSERACT_PATH"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Tesseract-OCR"

SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
SPARKAI_APP_ID = '2087ff0e'
SPARKAI_API_SECRET = 'ZDg4Mjg2NDlhNWUwNzA5ZjM5M2YxOTI5'
SPARKAI_API_KEY = '562ea31be2df40e0b808ad7d03145cfe'
SPARKAI_DOMAIN = '4.0Ultra'

class SparkAPIRetriever(BaseRetriever):
    document_dir: str = Field(..., description="The directory where documents are stored")
    documents: List[Document] = []
    loader: DirectoryLoader = None

    def __init__(self, document_dir: str, **kwargs):
        super().__init__(**kwargs)
        self.document_dir = document_dir
        self.loader = DirectoryLoader(path=self.document_dir, show_progress=True)
        self.documents = self.load_documents()

    def load_documents(self) -> List[Document]:
        # 使用 DirectoryLoader 加载文档
        return self.loader.load()

    def _get_relevant_documents(self, query: str, *, run_manager=None) -> List[Document]:
        return [doc for doc in self.documents if query.lower() in doc.page_content.lower()]

    async def _aget_relevant_documents(self, query: str, *, run_manager=None) -> List[Document]:
        return await super()._aget_relevant_documents(query, run_manager=run_manager)
    
class SparkAPILLM:
    def __init__(self, api_url: str, app_id: str, api_secret: str, api_key: str, domain: str):
        self.api_url = api_url
        self.app_id = app_id
        self.api_secret = api_secret
        self.api_key = api_key
        self.domain = domain

    def generate(self, prompt: str):
        spark = ChatSparkLLM(
            spark_api_url=self.api_url,
            spark_app_id=self.app_id,
            spark_api_key=self.api_key,
            spark_api_secret=self.api_secret,
            spark_llm_domain=self.domain,
            streaming=False,
        )
        messages = [ChatMessage(role="user", content=prompt)]
        handler = ChunkPrintHandler()
        response = spark.generate([messages], callbacks=[handler])

        # 确保正确访问 LLMResult 的内容
        generations = response.generations
        if generations and generations[0]:
            text = generations[0][0].text
            # print(f"Response from LLM: {text}")
            return {"content": text}
        return {"content": "No response from LLM"}

    
class RetrievalQA:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def __call__(self, inputs):
        query = inputs["query"]
        docs = self.retriever._get_relevant_documents(query)
        context = " ".join([doc.page_content for doc in docs])
        response = self.llm.generate(context + "\n\n" + query)
        return response["content"]
    
def create_rag_chain():
    retriever = SparkAPIRetriever(
        document_dir='../uploads'
    )
    llm = SparkAPILLM(
        api_url=SPARKAI_URL,
        app_id=SPARKAI_APP_ID,
        api_secret=SPARKAI_API_SECRET,
        api_key=SPARKAI_API_KEY,
        domain=SPARKAI_DOMAIN
    )
    qa_chain = RetrievalQA(retriever=retriever, llm=llm)
    return qa_chain


