from py2neo import Graph

graph = Graph()

for i in range(1,2):
	number = i
	if len(str(i)) == 1:
		number = "0" + str(i)
	number = str(number)

	# COMMENTS
	query = '\
	USING PERIODIC COMMIT 1000 LOAD CSV WITH HEADERS FROM "file:///Comments' + number + '.csv" AS row \
	MERGE (u:User { userID : row.userID}) \
	MERGE (s:Subreddit { subredditID : row.subredditID })\
	CREATE (c:Comment) \
	CREATE (c)-[:POSTED_BY]->(u)\
	CREATE (c)-[:POSTED_ON]->(s)'
	
	print("Inserting comments" + number)
	graph.run(query)
	print("Done inserting comments" + number)