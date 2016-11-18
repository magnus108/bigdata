from py2neo import Graph

graph = Graph()

query = """
LOAD CSV WITH HEADERS FROM "file:///Users.csv" AS row
CREATE (n:User)
SET n = row
"""

graph.run(query)

query = """
LOAD CSV WITH HEADERS FROM "file:///Comments.csv" AS row
CREATE (n:Comment)
SET n = row
"""

graph.run(query)

query = """
LOAD CSV WITH HEADERS FROM "file:///Subreddits.csv" AS row
CREATE (n:Subreddit)
SET n = row
"""

graph.run(query)

query = """
CREATE INDEX ON :User(userID)
"""

graph.run(query)

query = """
CREATE INDEX ON :Comment(commentID)
"""

graph.run(query)

query = """
CREATE INDEX ON :Subreddit(subredditID)
"""

graph.run(query)

query = """
MATCH (c:Comment),(u:User)
WHERE c.userID = u.userID
CREATE (c)-[:POSTED_BY]->(u)
"""

graph.run(query)

query = """
MATCH (c:Comment),(s:Subreddit)
WHERE c.subredditID = s.subredditID
CREATE (c)-[:POSTED_ON]->(s)
"""

graph.run(query)
