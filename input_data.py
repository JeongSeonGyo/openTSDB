import time
import requests
import json




timestamp=[]
HR=[]
x=[]
y=[]
z=[]
with open('data.csv','r') as data:
	count=0
	first_line = data.readline()
	lines = data.readlines()
	for l in lines:
		timestamp.append(l.split(',')[0])
		HR.append(l.split(',')[1])
		x.append(l.split(',')[2])
		y.append(l.split(',')[3])
		z.append(l.split(',')[4])
		count = count+1

#send_data(timestamp,HR,x,y,z)
print "next"


cnt=0
while(1):
	
	
	if cnt == count:
		break

	
	else:
		s = "2016/%s/%s-%s:%s:%s"%(timestamp[cnt][0:2],timestamp[cnt][2:4],timestamp[cnt][4:6],timestamp[cnt][6:8],timestamp[cnt][8:10])
		ts = time.mktime(time.strptime(s,"%Y/%m/%d-%H:%M:%S"))
		
		url = "http://10.0.1.43:4242/api/put"
		data = {
		    "metric": "foo_hr.bar",
		    "timestamp": ts,
		    "value": HR[cnt],
		    "tags": {
		       "heart_rate":"HR"
		    }
		}
		
		ret = requests.post(url, data=json.dumps(data))

		data = {
		    "metric": "foo_x.bar",
		    "timestamp": ts,
		    "value": x[cnt],
		    "tags": {
		       "acc_x":"x"
		    }
		}
		
		ret = requests.post(url, data=json.dumps(data))

		data = {
		    "metric": "foo_y.bar",
		    "timestamp": ts,
		    "value": y[cnt],
		    "tags": {
		       "acc_y":"y"
		    }
		}
		
		ret = requests.post(url, data=json.dumps(data))

		data = {
		    "metric": "foo_z.bar",
		    "timestamp": ts,
		    "value": z[cnt],
		    "tags": {
		       "acc_z":"z"
		    }
		}
		
		ret = requests.post(url, data=json.dumps(data))
		
		cnt = cnt+1
		
print "ok"

		


		
