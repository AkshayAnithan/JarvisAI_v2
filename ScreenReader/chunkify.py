import re
from bs4 import BeautifulSoup

def split_document(document, words_per_chunk):
    # Split the document into sentences
    sentences = re.split('(?<=[.!?]) +', document)

    # Initialize the list of chunks
    chunks = []
    current_chunk = ''

    # Loop through the sentences and add them to the current chunk until it reaches the desired size
    for sentence in sentences:
        sentence_words = sentence.split()
        if len(current_chunk.split()) + len(sentence_words) <= words_per_chunk:
            current_chunk += sentence + ' '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ' '

    # Add any remaining sentences to the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks