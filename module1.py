a=10
print("a 1",a)

def myfunction():
    a=20
    b=34
    def f1():
        print("in f1",a)
        print("In function f1")
        def f2():
            nonlocal a
            print("This is f2")
            print("nested inside")
        f2()
        c=12
    f1()
    print("In function :",a)
   

print("a 2",a)
myfunction()
#f1()
print("after call",a)
print("local b:",b)

