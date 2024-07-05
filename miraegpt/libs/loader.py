import os
from langchain_community.document_loaders import JSONLoader
from langchain_core.documents import Document

FOLDER_TO_READ = 'chat_history'
READ_PATH = os.path.join('data', FOLDER_TO_READ)
SOURCE = "source"

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata['sender'] = record.get('initiator')
    
    if SOURCE in metadata:
        source = metadata[SOURCE].split('/')
        source = source[source.index(FOLDER_TO_READ):]
        metadata["sav_id"] = source[-1].split('_')[0]
        metadata[SOURCE] = '/'.join(source)

    return metadata

def convert_json_to_documents(path_to_json: str) -> list[Document]:
    loader = JSONLoader(
        file_path=path_to_json,
        jq_schema='.chat_history[]',
        content_key='message',
        metadata_func=metadata_func
    )
    return loader.load()

if __name__ == "__main__":
    print(convert_json_to_documents(os.path.join('data', 'chat_history', '4853535_2024-6-18.json')))
