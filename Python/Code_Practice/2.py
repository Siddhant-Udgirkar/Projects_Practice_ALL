"""
Find the sum of the positions of a digit in a particular number
"""


number= int(input("Enter a number: "))
digit= int(input("Enter a digit to find the sum of positions: "))
sum_pos=0
str_number= str(number)
str_digit= str(digit)

for i in range(len(str_number)):
    if str_number[i]==str_digit:
        sum_pos=sum_pos+i

print(sum_pos)
