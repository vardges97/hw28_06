def zip_tst(iterables):

    minln = min(len(item) for item in iterables)
    for i in range (minln):
        items = tuple(item[i] for item in iterables)
        yield items