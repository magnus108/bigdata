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

# Create the correct UTC stamps for each month.
months = []
for i in range(1,13):
	months.append(getUTCStamp(datetime.datetime(2008,i,1)))



###
### Check Total number of Obama menntions in 2008
###
query = '\
	MATCH (c:Comment) \
	WHERE c.body =~ ".*[Oo]bama.*" \
	RETURN count(c) as obamas\
	'
tick = time.time()
retval = graph.run(query)
data = retval.data()[0]
print("Obama mentions: " + str(data["obamas"]))
print("Time to find Obama mentions: " + toMin(time.time() - tick))

###
### Check total number of Romney mentions in 2008
###

query = '\
	MATCH (c:Comment) \
	WHERE c.body =~ ".*[Rr]omney.*" \
	RETURN count(c) as romneys\
	'

tick = time.time()
retval = graph.run(query)
data = retval.data()[0]
print("Romney mentions: " + str(data["romneys"]))
print("Time to find Romney mentions: " + toMin(time.time() - tick))


'''
#
obamasPrMonth = []

for i in range(1,11):
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


print("TOTAL TIME SPENT:" + toMin(time.time() - startTime))