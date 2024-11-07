import re
from langchain.schema import Document

class TableTextSplitter:
    def __init__(self, headers_to_split_on):
        self.headers_to_split_on = headers_to_split_on

    def split_text(self, data_text):
        chunks = []

        for tag, _ in self.headers_to_split_on:
            pattern = rf"<{tag}>(.*?)</{tag}>"
            matches = re.findall(pattern, data_text, re.DOTALL)

            for match in matches:
                # 각 분할된 텍스트를 Document 객체로 추가
                chunks.append(Document(page_content=match))

        return chunks  