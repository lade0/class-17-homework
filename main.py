try:
    step1=int(input("enter your age and don't lie"))
    result=step1
    print("your age is:",result)
    if result%2==0:
        print(result,"is an even number")
    else:
        print(result,"is an odd number")
except ValueError:
    print("enter something valid")
    