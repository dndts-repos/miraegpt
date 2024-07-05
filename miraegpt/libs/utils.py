import os
from langchain_core.documents import Document

from miraegpt.libs.loader import convert_json_to_documents

CHAT_HISTORY_PATH = os.path.join("data", "chat_history")

def write_markdown_file(content, filename):
  """Writes the given content as a markdown file to the local directory.

  Args:
    content: The string content to write to the file.
    filename: The filename to save the file as.
  """
  with open(f"trace/{filename}.md", "w") as f:
    f.write(content)

def isFileExist(sav_id: int):
  for filename in os.listdir(CHAT_HISTORY_PATH):
    temp = filename.split('_')
    if temp[0] == sav_id:
      return True, filename
  return False, None

def get_chat_histories(documents: list[Document]) -> list[list[Document]]:
  chat_histories = []
  for document in documents:
    sav_id = document.metadata['sav_id']
    flag, filename = isFileExist(sav_id)
    if flag:
      chat_history = convert_json_to_documents(os.path.join(CHAT_HISTORY_PATH, filename))
      chat_histories.append(chat_history)
  return chat_histories

    