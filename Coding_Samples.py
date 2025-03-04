def sum_of_digits_of_a_number(num):
    str_num=str(num)
    list_digits= list(str_num)
    sum_digits=0
    for i in list_digits:
        sum_digits=sum_digits+int(i)
    print(sum_digits)

# sum_of_digits_of_a_number(123)

def leap_year(year):
    if year%4==0:
        print("Leap year")
    else:
        print("Not a leap year")

# leap_year(2100)

def prime_num(num):
    for i in range(2, num):
        if num%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime Number")

# prime_num(2)

def prime_number_within_range(start_range, end_range):
    for num in range(start_range, end_range+1):
        for div in range(2, num):
            if num%div==0:
                print(f"{num} is a not a prime number")
                break
        else:
            print(f"{num} is a prime number")

# prime_number_within_range(1, 10)


def prime_nos_in_given_range(start, end):
    is_prime=True
    for num in range(start, end+1):
        for denominator in range(2, num):
            if num%denominator==0:
                is_prime=False
                print(f"{num} is NOT Prime")
                break
            else:
                is_prime=True
                break
        if is_prime:
            print(f"{num} is Prime")

# prime_nos_in_given_range(1,11)



def sum_of_digits_of_a_number(num):
    sum_digits=0
    print(num, num/10, num%10, num//10, int(num/10))
    while num>0:
        sum_digits=sum_digits+num%10
        num=num//10
    print(sum_digits)

# sum_of_digits_of_a_number(1234)


# def demo():
#     list_1=[[]]*3
#     print(list_1)
#     list_1[0][0].append(33)
#     print(list_1)
#
# demo()

def reverse_a_number(num):
    rev_number=0
    while num>0:
        rev_number= rev_number*10 + num%10
        num=num//10
    print(rev_number)

# reverse_a_number(1234)

def palindrome_number(num):
    if num==int(str(num)[::-1]):
        print(f"{num} is palindrome number")
    else:
        print(f"{num} not a palindrome number")

# palindrome_number(221122)


def armstrong_number(num):
    str_num=str(num)
    len_num=len(str_num)
    armstrong=0
    for i in str_num:
        armstrong=armstrong+(int(i)**len_num)

    if armstrong==num:
        print(f"{num} is Armstrong number")
    else:
        print(f"{num} is NOT Armstrong number")

# armstrong_number(371)
# armstrong_number(1634)


def armstrong_number_in_a_given_range(start, end):
    for num in range(start, end+1):
        original_num=num
        len_num=len(str(num))
        armstrong = 0
        while num>0:
            digit= num%10
            armstrong+=digit**len_num
            num//=10
        if armstrong==original_num:
            print(f"{original_num} is Armstrong")
            continue

# armstrong_number_in_a_given_range(1,400)
