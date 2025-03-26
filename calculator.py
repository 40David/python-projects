def add(a,b):
    sum=a+b
    print(f"the solution is {sum}")
def sub(a,b):
    diff=a-b
    print(f"the solution is {diff}")
def multi(a,b):
    produ=a*b
    print(f"the solution is {produ}")
def div(a,b):
    l=a/b
    print(f"the solution is {l}")
a=int(input("a="))
b=int(input("b="))
mode=str(input("mode="))
if mode=="+":
    add(a,b)
elif mode=="-":
    sub(a,b)
elif mode=="*":
    multi(a,b)
elif mode=="/":
    div(a,b)
else:
    print("oprtation not found")