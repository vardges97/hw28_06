def counter():
    count = 0

    def inner_counter():
        nonlocal count
        count+=1
        return count

    return inner_counter()