def filter(func,list):
    result=[]
    for item in list:
        if func(item):
           yield (item)