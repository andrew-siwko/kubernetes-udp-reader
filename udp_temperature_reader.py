print('starting kubernetes test')
def ctof(c):
    return(c/5*9+32)

import socket
import json
import datetime

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('got socket:',s)
port=23229
s.bind(('',port))
last_t1=-1
last_t2=-1

while True:
    data=s.recv(1000)
    print(data)
    try:
        data_string=json.loads(data)
        if 'temperature_1' in data_string and 'temperature_2' in data_string:
            t1=data_string['temperature_1']
            t2=data_string['temperature_2']
            if last_t1!=t1 or last_t2!=t2:
                last_t1=t1 
                last_t2=t2
                ts=datetime.datetime.now().strftime('%m/%d/%Y %H:%M')
                print(ts,round(ctof(t1),1),round(ctof(t2),1),round((t1-t2)/5*9,1))
                with open('temps.csv','a') as f:
                    f.write(ts+','+str(round(ctof(data_string['temperature_1']),1))+','+str(round(ctof(data_string['temperature_2']),1))+','+str(round((data_string['temperature_1']-data_string['temperature_2'])/5*9,1))+'\n')
        else:
            print(data_string)

    except Exception as e: 
        print(e)
        print(data)