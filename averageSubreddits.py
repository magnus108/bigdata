from py2neo import Graph
import datetime
import calendar
import time
startTime = time.time()

def getUTCStamp(dt):
	return calendar.timegm(dt.utctimetuple())

def toMin(timeDiff):
	seconds = timeDiff
	return str("%.3f" % seconds)

graph = Graph()


query = '''
MATCH (u1:User)<-[:POSTED_BY]-(c:Comment)-[:POSTED_ON]->(s:Subreddit)
RETURN u1,count(DISTINCT(s)) as avg
'''

tick = time.time()
print("Starting query")
retval = graph.run(query)
print("Done in: " + toMin(time.time() - tick))
subredditsUsed = 0
for item in retval:
	subredditsUsed += item["avg"]

print(subredditsUsed/88570)