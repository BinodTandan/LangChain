from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='langchain_document_loader/FCM_Concepts_Transportaion_5.0.csv')

docs = loader.load()

print(docs[1].page_content)
