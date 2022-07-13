##    3
def prime(n):
    try:
        if n<1:
            raise ValueError("there is no zeroth prime")
        num=2
        count=1
        while True:
            if count==n:
                break
            num+=1
            a=2
            while a<num:
                if num%a==0:
                    break
                a+=1
            else:
                count+=1
    except ValueError as e:
        print(e)
    else:
        print("The ",n,"th prime no. is : ",num)
            
n=int(input("Enter a no. "))
prime(n)
