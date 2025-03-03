def sum_of_digits_of_a_number(num):
    str_num=str(num)
    list_digits= list(str_num)
    sum_digits=0
    for i in list_digits:
        sum_digits=sum_digits+int(i)
    print(sum_digits)

sum_of_digits_of_a_number(123)