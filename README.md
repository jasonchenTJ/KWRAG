# KWRAG
This is a project about LLM RAG knowledge ChatBot.

![Image](https://github.com/user-attachments/assets/5dca8b44-02c8-4ae4-8864-7570c894f36f)

You can upload ypur personal knowledge into vector database.
![Image](https://github.com/user-attachments/assets/eb5c44aa-e6aa-4a02-a87d-f814b4625c63)

And there is a simple login page for user accessing control.

<img width="800" alt="Image" src="https://github.com/user-attachments/assets/5411edbc-76c6-4d37-a339-f8623330accf">

Tech architect: 


| 技术内容                                       | 相关模块说明                                                                                                                                                      |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 前端：Vue.js , html,  css , javascripts        | 前端页面登录知识库问答交互界面批量上传文档功能                                                                                                                    |
| 后端：python 3 + langchain + fastapi           | 发布调用LLM接口发布调用embedding 接口（包含写入和相似度查询）                                                                                                     |
| 数据库:postgres 16.3向量数据库:pgvector        | PG库存储一些基本数据库平台的管理信息PGVECTOR 存储知识库的特征向量信息                                                                                             |
| LLM大模型：Llama3-Chinese| Llama3-Chinese是以Meta-Llama-3-8B为底座，使用 DORA + LORA+ 的训练方法，在50w高质量中文多轮SFT数据 + 10w英文多轮SFT数据 + 2000单轮自我认知数据训练而来的大模型。
| Embedding 内嵌模型：word2vec |  |
| 代码开发辅助：chatgpt-4O文心一言 | 辅助生成代码  | 
| 开发工具:后端: pycharm 社区版前端: vscode      | 需要安装vue.js插件                                                                                                                                                |
