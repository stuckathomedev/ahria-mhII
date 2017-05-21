from duckduckpy import query
response = query('Python')
response.related_topics[0]
type(response.related_topics[0])
print(response)
