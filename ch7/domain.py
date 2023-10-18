b = [1,2,3]

def func(a):
    global b
    print(a)
    print(b)
    b=4
func(2)
print(b)