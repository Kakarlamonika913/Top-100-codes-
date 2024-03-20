def GiveAllSubsets(input_data):
    mainlist=[]
    for i in range(2**len(input_data)):
        sublist=[]
        for j in range(len(input_data)):
            if(1<<j&i==0):
                sublist.append(input_data[j])
                mainlist.append(sublist)
    return mainlist 
