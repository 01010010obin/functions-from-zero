from wikipediaapi import Wikipedia
wiki = Wikipedia(language='en', user_agent="MyApp/1.0")

def bot_search(topic="Large Language Models"):
    wiki = Wikipedia(language='en', user_agent="MyApp/1.0")
    page = wiki.page(topic)
    #print(page.title)
    #print(page.summary)
    result = f"{page.title} \n {page.summary}"
    return result