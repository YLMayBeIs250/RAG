import os
from openai import OpenAI


class Model:
    """
    实例化的时候默认使用deepseek的api_key
    """
    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key or os.environ.get("ARK_API_KEY")
        self.base_url = base_url or "https://ark.cn-beijing.volces.com/api/v3"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def get_base_client(self):
        client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        return client

    def get_base_completion(self, query, docs):
        context = "\n".join([doc.page_content for doc in docs])
        response = self.client.chat.completions.create(
            model="ep-20250521230712-zmlbp",
            messages=[
                {"role": "system", "content": f"根据以下上下文回答问题：\n{context}\n"},
                {"role": "user", "content": f"问题：{query}"},
            ]
        )
        return response

