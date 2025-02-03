print("hello")
from wikipediaapi import Wikipedia

# Wikipedia API'yi kullanarak bir sayfa yükleyin
wiki = Wikipedia(language='en', user_agent="MyApp/1.0")
page = wiki.page("Python programming language")
print(page.title)
print(page.summary)
