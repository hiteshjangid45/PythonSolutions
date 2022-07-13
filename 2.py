##   2

# Solution 1 : by using A.P. formula

try:
    num = int(input("Enter a no. "))
    if num<1:
        raise ValueError
    sum1=(num*(num+1))//2
    sum2=(num*(num+1)*(2*num+1))//6
    diff_of_sums=(sum1**2)-sum2
    print("Difference of square of the sum & sum of the squares of the first ",num," natural numbers is : ",diff_of_sums)
except ValueError:
    print("Invalid input for a natural no. Please enter a valid natural no.")
