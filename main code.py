print("welcome to ATC how may I help you")
print("1: for landing")
print("2: for takeoff")
a=int(input("enter your choice"))
if a==1:
    print("are you close to any of these airports")
    l=["Chennai","Hyderabad","Delhi","  Bengaluru","Mumbai","Kochi","Kolkata","Ahmedabad"]
    for i in range(0,len(l)):
        print(i+1,":",l[i])
    b=int(input("enter your choice"))
    f=int(input("enter the distance that can be covered by the fuel in the aircraft in KM"))
    if b==8:
        import Ahmedabad
        print(Ahmedabad.landing(f))
    elif b==6:
        import Kochi
        print(Kochi.landing(f))
    elif b==2:
        import hyderabad
        print(hyderabad.landing(f))
    elif b==5:
        import mumbai
        print(mumbai.landing(f))    
    elif b==3:
        import delhi
        print(delhi.landing(f))
    elif b==1:
        import chennai
        print(chennai.landing(f))
    elif b==4:
        import bengaluru
        print(bengaluru.landing(f))
    elif b==7:
        import Kolkata
        print(Kolkata.landing(f))
    else:
        print("wrong choice")
elif a==2:
    print("are you at any of these airports")
    l=["Chennai","Hyderabad","Delhi","bengaluru","mumbai","kochi","kolkata","Ahmedabad"]
    for i in range(0,len(l)):
        print(i+1,":",l[i])
    b=int(input("enter your choice"))
    f=int(input("enter the distance that can be covered by the fuel in the aircraft"))
    if b==8:
        import Ahmedabad
        print(Ahmedabad.takeoff(f))
    elif b==6:
        import Kochi
        print(Kochi.takeoff(f))
    elif b==2:
        import hyderabad
        print(hyderabad.takeoff(f))
    elif b==5:
        import mumbai
        print(mumbai.takeoff(f))    
    elif b==3:
        import delhi
        print(delhi.takeoff(f))
    elif b==1:
        import chennai
        print(chennai.takeoff(f))
    elif b==4:
        import bengaluru
        print(bengaluru.takeoff(f))
    elif b==7:
        import Kolkata
        print(Kolkata.takeoff(f))
    else:
        print("wrong choice")
else:
    print("sorry wrong answer")


