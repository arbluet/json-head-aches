import datetime, json
def jeeves(request):
    message=''
    if request.get('type')=='maintenance':
        message='Thank you tenant at Unit'+str(request[unit])+', your request for maintenance to deal with '+'"'+str(request[issue])+'"'+' has been received #2 input'
    elif request.get('type')=='purchase':
        message='Thank you tenant at Unit'+str(request[unit])+'your request to purchase a'+str(request[commodity])+ ' has been received'
    elif request.get('type')=='reservation':

        startTime=request[date].split(" ")[1]
        startTime=startTime.split('')
        time=0;
        num=[]
        for item in startTime:
            if isdigit(item):
                num.append(item)

                for index in range(len(num)):
                    time+=num[index]*10**(len(num)-index)
                    endTime=0
                    daySplit=''.join(startTime[-2:])
                    if time+int(request[duration].split(' ')[0])>12:
                        endTime=time+int(request[duration].split(' ')[0])-12
                        if daySplit=='AM':
                            endTime=str(endTime)+'PM'
                        else:
                            endTime=str(endTime)+'AM'
                    else:
                        endTime=endTime+int(request[duration].split(' ')[0])
                        endTime=str(endTime)+daySplit
    message='Thank you tenant at Unit'+str(request.get(unit)+'your request to reserve our '+str(request[location])+' on '+str(request[date].split(' ')[0])+' from '+str(request[date].split(' ')[1])+' to '+endTime+' has been received'
print message
return message
    elif request.get('type')=='complaint':
        message='Thank you tenant at Unit'+str(request[unit])+' we will have someone follow up on '+'"'+request[issue]+'"'+' in regards to our '+request[location]'.'
            return message
