from wikibot import search3

# def test_search():
#    assert "Deep Learning" in search3("Deep Learning",start=0,end=1)


def test_search():
    result = search3("Deep Learning", start=0, end=1)
    assert result in search3("Deep Learning", start=0, end=1)
