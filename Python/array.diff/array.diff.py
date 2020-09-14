def array_diff(a, b):
    if b == None:
        pass
    else:
        for i in b:
            while i in a:
                a.remove(i)
        return a;
