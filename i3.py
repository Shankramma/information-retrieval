import os
import codecs
def word_split(text):
    word_list = []
    wcurrent = []
    windex = None

    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
            windex = i
        elif wcurrent:
            word = u''.join(wcurrent)
            word_list.append((windex - len(word) + 1, word))
            wcurrent = []

    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex - len(word) + 1, word))
    print(word_list)

    return word_list

def words_cleanup(words):
    cleaned_words = []
    for index, word in words:
        if len(word) < _WORD_MIN_LENGTH or word in _STOP_WORDS:
            continue
        cleaned_words.append((index, word))
    return cleaned_words

def words_normalize(words):
    normalized_words = []
    for index, word in words:
        wnormalized = word.lower()
        normalized_words.append((index, wnormalized))
    return normalized_words
def word_index(text):
    words = word_split(text)
    words = words_normalize(words)
    words = words_cleanup(words)
    return words
def inverted_index(text):
    inverted = {}

    for index, word in word_index(text):
        locations = inverted.setdefault(word, [])
        locations.append(index)

    return inverted
def inverted_index_add(inverted, doc_id, doc_index):
    for word, locations in doc_index.iteritems():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted
def search(inverted, query):
    words = [word for _, word in word_index(query) if word in inverted]
    results = [set(inverted[word].keys()) for word in words]
    return reduce(lambda x, y: x & y, results) if results  else []


list=[]
for txt in os.listdir('/home/sukruti/2nd_sem/trse_assignment/corpus'):
    list.append(txt)
for i in list:
    fileExtension = i.split(".")[-1]
    if fileExtension == "txt":
        with codecs.open(i, "r",encoding='utf-8', errors='ignore') as file:
            content=file.read()
            word_split(content)
