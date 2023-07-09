def enumerate_tst(list, start=0):
    for i in range(len(list)):
        yield (i+start,list[i])

