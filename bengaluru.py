# Air traffic control system for bengaluru airport
def landing(f):
    ws=int(input("enter wind speed"))
    n =40
    if n>0 and f<250 and ws>30 and ws<40:
        a="you can land safely"
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
