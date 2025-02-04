from wikipediaapi import Wikipedia
wiki = Wikipedia(language='en', user_agent="MyApp/1.0")

def bot_search(topic="LLMS"):
    page = wiki.page(topic)
    #print(page.title)
    #print(page.summary)
    result = print(f"{page.title} \n {page.summary}")
    return result