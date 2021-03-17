#def print_param(*param):
#    print(param)

#print_param('Testing')
#print_param(1,2,3,4,5,6)

def print_params(x,y,z=10,*param,**params):
    print(x,y,z)
    print(param)
    print(params)

print_params(1,2)
