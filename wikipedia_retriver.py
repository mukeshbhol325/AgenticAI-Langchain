from langchain_community.retrievers import WikipediaRetriever

retriver=WikipediaRetriever(top_k_results=2,lang='en')

query="the geopolitical history of india and Russia"


docs=retriver.invoke(query)

print(docs[0])