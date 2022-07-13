##   4

def sum_of_multiples(num,factor_list):
    sum1=0
    n=1
    while n<num:
        for i in factor_list:
            if n%i==0:
               sum1+=n
               print(n)
               break
        n+=1
    return sum1

num = int(input("Enter a no. "))
factor_list = [3,4,5]
print("sum of multiples of ",factor_list," is : ",sum_of_multiples(num,factor_list))
