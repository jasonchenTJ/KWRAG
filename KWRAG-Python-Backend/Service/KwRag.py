import configparser
import requests
from langchain_core.documents import Document
from langchain_postgres import PGVector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres.vectorstores import PGVector

class KwRag():

    def __init__(self):
        self.conf = './config/env_setting.conf'
        self.db_vector_connection = ''
        self.section = 'ENV'
        self.username = self.getConfigVal('username')
        self.password = self.getConfigVal('password')
        self.LLM_API = self.getConfigVal('LLM_API')
        self.embeddingBuild = 'D:\\AI\\text2vec-base-chinese'
        self.embeddings = HuggingFaceEmbeddings(model_name=self.embeddingBuild)
        self.vectorstore = PGVector(
                embeddings=self.embeddings,
                collection_name=self.getConfigVal('collection_name'),
                embedding_length =768,
                connection=self.getConfigVal('connection'),
                use_jsonb=True,
        )


    def userLogon(self,username,password):
        if username == self.username and password == self.password:
            return 1
        else:
            return 0

    def LLMTalk(self,message):
        data = {"content":message}
        response = requests.post(self.LLM_API, json=data)
        return response.json()

    def embeddingTalk(self,message):
        return self.vectorstore.similarity_search(message, k=1)[0].page_content.replace('\n','</br>')

    def RAGTalk(self,message):
        kwMessage = self.embeddingTalk(message)
        return self.LLMTalk("问题提示{},问题：{}".format(kwMessage,message))

    def embeddingLoad(self,docs):
        try:
            self.vectorstore.add_documents(docs, ids=[doc.metadata["id"] for doc in docs])
        except Exception as e:
            print('embeddingLoad error {}'.format(e))
            return 1
        return 0


    def getConfigVal(self, key):
        cf = configparser.ConfigParser()
        cf.read(self.conf)
        val = cf.get(self.section, key)
        return val;


if __name__ == '__main__':
    kw = KwRag()
    print(kw.username)


