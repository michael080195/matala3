def ReadFile():
    file_path= input('enter a file path:')
    handle=open(file_path, encoding='utf-8')
    dictionery(handle)
               
def dictionery(handle:str):
    idList=list()
    fileList=list()
    Data=dict()
    counter=-1
    for line in handle:
        counter+=1
        if counter==1:
            nameStart=line.find(' "')
            nameEnd=line.find('" ',nameStart)
            chat_name=line[nameStart+1:nameEnd]
            creatAnd=line.find(',')
            creation_date=line[0:creatAnd-1]
        try:
            float(line[0])
            endDate=line.find('-')
            startNum=line.find('-')
            endNum=line.find(':',startNum)
            num=line[startNum+1:endNum].rstrip()
            if endNum != -1:
                if num not in idList:
                    idList.append(num)
                    index=idList.index(num)
                    fileList.append({"datetime":line[0:endDate],"id":index, "text":line[endNum:].rsplit()},)        
        
        except:
            continue
    Data = {'chat_name': chat_name , 'creation_date':creation_date , 'num_of_purtic':len(idList) , 'creator':idList[0] }
    fileList.append(Data)
    import json
    noya_birthday_party=json.dumps(fileList)
    print(fileList)