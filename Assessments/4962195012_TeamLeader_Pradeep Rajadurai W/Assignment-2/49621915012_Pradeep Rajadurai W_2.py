while(True):
    print("\nCalculator:\n1.Add\n2.Subtract\n3.Multiplication\n4.Division\n5.Exit\n")
    print("Enter the choice...")
    n=int(input())
    if(n==5):
        break
    n1=int(input("Enter the First number\t:"))
    n2=int(input("Enter the second number\t:"))
    if(n==1):
        print("Answer : ",n1+n2)
    elif(n==2):
        print("Answer : ",n1-n2)
    elif(n==3):
        print("Answer : ",n1*n2)
    elif(n==4):
        print("Answer : ",n1/n2)
    else:
        break
