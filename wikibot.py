print("hello")
from wikipediaapi import Wikipedia

# Wikipedia API'yi kullanarak bir sayfa yükleyin
wiki = Wikipedia(language='en', user_agent="MyApp/1.0")
page = wiki.page("Python programming language")
print(page.title)
print(page.summary)

def search(topic):
    page = wiki.page(topic)
    print(page.title)
    print(page.summary)

search("AI")

def search2(topic):
    page = wiki.page(topic)
    print(page.title)
    print(page.summary[0:10])

search2("MLOps")

def search3(topic="Deep Learning",start=0,end=1):
    page = wiki.page(topic)
    #print(page.title)
    lst=page.summary.split('.')
    sentences=".".join(lst[start:end]) + '.'
    #print(sentences)
    return sentences
search3("Deep Learning",start=0,end=1)
