def repeat(xs, n):
    r = []
    if n < 0:
        return ValueError
    for i in range(n):
        for m in xs:
            r += m
    print(r)
    
repeat([1, 2, 3], 3)