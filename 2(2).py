##   2
# Solution 2 : by simple loops

try:
    num = int(input("Enter a no. "))
    if num<1:
        raise ValueError
    sum1=0 
    sum2=0
    for i in range(1,num+1):
        sum1+=i
        sum2+=i**2
    diff_of_sums=(sum1**2)-sum2
    print("Difference of square of the sum & sum of the squares of the first ",num," natural numbers is : ",diff_of_sums)
except ValueError:
    print("Invalid input for a natural no. Please enter a valid natural no.")

