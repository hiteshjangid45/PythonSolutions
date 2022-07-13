##  1
def num_to_string(num):
    str1=""
    if num%3==0:
        str1+="Pling"
    if num%5==0:
        str1+="Plang"
    if num%7==0:
        str1+="Plong"
    if not str1:
        str1+=str(num)
    return str1

num = int(input("Enter a No. "))
print("Converted String : ",num_to_string(num))
