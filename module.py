myvar=200
def myfunction1(x):
    """this is multiline doc string
        for myfuntion1"""
    print("module name :",__name__)
    x=x+10
    print("x:",x)
    return x

def myfunction2(n,p):
    for i in range(1,p+1):
        print(n,"*",i,"=",(n*i))




if __name__=="__main__":
    myfunction1(20)
    myfunction2(7,10)

