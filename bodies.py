from py2neo import Graph

graph = Graph()

query = """
MATCH (n:Comment) RETURN n.body
"""

data = graph.run(query)

for d in data:
    print(d['n.body'])
