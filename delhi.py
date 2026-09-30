# Air traffic control system for DELHI airport
def landing(f):
    ws=int(input("enter wind speed in knots"))
    n = 78
    if n>0 and f<250 and ws>30 and ws<40:
        b="you can land safely"
        n=n-1
    else:
        b="sorry try anywhere else"
    return(b)
def takeoff(f):
    ws=int(input("enter wind speed in knots"))
    if f>500 and ws>30 and ws<40:
        a="you can take off safely"
    else:
        a="sorry try after sometime"
    return(a)
