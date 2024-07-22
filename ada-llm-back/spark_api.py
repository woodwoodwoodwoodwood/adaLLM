from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

# 星火认知大模型的配置
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
SPARKAI_APP_ID = '2087ff0e'
SPARKAI_API_SECRET = 'ZDg4Mjg2NDlhNWUwNzA5ZjM5M2YxOTI5' # 请替换为您的API_SECRET
SPARKAI_API_KEY = '562ea31be2df40e0b808ad7d03145cfe'    # 请替换为您的API_KEY
SPARKAI_DOMAIN = '4.0Ultra'

def get_spark_response(prompt):
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    result = spark.generate([messages], callbacks=[handler])
    
    # 提取 generations 中的 text 字段
    if result and result.generations and result.generations[0]:
        response_text = result.generations[0][0].text
    else:
        response_text = "No response generated."

    return response_text
