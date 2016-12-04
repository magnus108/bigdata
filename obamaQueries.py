from py2neo import Graph
import datetime
import calendar
import time
startTime = time.time()

def getUTCStamp(dt):
	return calendar.timegm(dt.utctimetuple())

def toMin(timeDiff):
	minutes = timeDiff / (1000 * 60)
	return "%.3f" % minutes

graph = Graph()

# Create the correct UTC stamps for each month.
months = []
for i in range(1,13):
	months.append(getUTCStamp(datetime.datetime(2008,i,1)))



###
### Check
###


'''
#
obamasPrMonth = []

for i in range(10,11):
	print(months[i])
	query = '\
	MATCH (c:Comment)\
	WHERE c.body =~ ".*[Oo]bama.*"\
	AND c.created_utc > "' + str(months[i]) + '"\
	AND c.created_utc < "' + str(months[i + 1]) + '"\
	RETURN count(c) as obamas \
	'
	retval = graph.run(query)
	data = retval.data()
	print(data[0]["obamas"])
	obamasPrMonth.append(data[0]["obamas"])
'''


#print(" ")
#print(months[1])
#print(months[1 + 1])
#query = '\
#	MATCH (c:Comment) \
#	WHERE c.body =~ ".*[Oo]bama.*" \
#	AND c.created_utc > "' + str(months[1]) + '" \
#	AND c.created_utc < "' + str(months[1 + 1]) + '" \
#	RETURN count(c) as obamas\
#	'

#retval = graph.run(query)	
#print(retval.data())


print("TOTAL TIME SPENT:" + str(toMin(time.time() - startTime)))