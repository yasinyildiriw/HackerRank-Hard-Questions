#https://www.hackerrank.com/challenges/validating-postalcode/problem

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


#before i learn re functions this was my solution

# def find_the_repetitives(sayi):
#     n = 0
#     k = 0
#     while n<6:
#         if sayi[n] == sayi[n+2]:
#             k += 1
#         if n == 4:
#             return k
#         n += 1
# number = input()
# 
# if len(number) == 7:
#     iterative = find_the_repetitives(number)
#     if iterative>=1:
#         print(False)
#     else:
#         print(True)
