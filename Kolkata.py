def takeoff(f):
    ws=int(input("enter wind speed in knots"))
    if f>500 and ws > 30 and ws < 40:
        b="you can take off safely"
    else:
        b="sorry try after sometime"
    return(b)
def landing(f):
    ws=int(input("enter wind speed"))
    n =24
    if n>0 and f<250 and ws>30 and ws<40:
        print("you can land safely")
        n=n-1
    else:
         a="sorry try anywhere else"
    return(a)
