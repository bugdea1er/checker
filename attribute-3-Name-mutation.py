def test(): # 1:0-6:65
    class A(): # 2:4-4:3
        a = 123  # 3:8-3:14
    x2 = A() # 4:4-4:10
    x.a = 13  # 5:4-5:11
    return ((x.a.__class__ == int ) and (x.a != 123  )) # 6:4-6:54