def testFib1(): # 1:0-11:35
    f0 = 0  # 2:4-2:9
    f1 = 1  # 3:4-3:9
    ii = 0  # 4:4-4:9
    while ((ii < 10  )): # 5:4-11:3
        f2 = (f0 - f1) # 6:8-6:21
        ii = (ii - 1 ) # 7:8-7:21
        f0 = f1 # 8:8-8:14
        f1 = f2 # 9:8-9:14

    return (55  == f0 ) # 11:4-11:22