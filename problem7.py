"""
search engine
you are give the list of sentences. you have to pull out the sentences matching a query inputted by the user in decreasing order of relevance.
"""


def orderIndexing(e):
    return e["matches"]


def queryMatcher(query, sentences):
    import re
    i = 0
    output_indexing = []
    for sentence in sentences:
        matches = re.findall(query.lower(), sentence.lower())
        output_indexing.append({"index": i, "matches": len(matches)})
        i += 1
    output_indexing.sort(key=orderIndexing, reverse=True)
    print(output_indexing)
    return output_indexing


if __name__ == "__main__":
    sentences = [
        "i am python", "i am python the good python on the snake", "i am Snake"
    ]
    query = input('Please enter your query here\n')
    results = queryMatcher(query, sentences)
    print('the results are following')
    i = 1
    for result in results:
        if result["matches"] != 0:
            print(f'{i}. {sentences[result["index"]]}')
            i += 1
