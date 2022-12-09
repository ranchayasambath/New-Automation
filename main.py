# import re
# numbers = [-2,-1,0,1,2]
# def extract_positive(numbers):
#     positive_numbers = []
#     for number in numbers:
#         if number > 0:
#             positive_numbers.append(number)
#     return positive_numbers
# extract_positive(numbers)
# numbers = [-2,-1,0,1,2]
# positive_numbers = filter(lambda n: n>0, numbers)
# positive_numbers
# list(positive_numbers)
# def is_positive(n):
#     return n > 0
# list(filter(is_positive, numbers))
# def identity(x):
#     return x
# identity(42)
# load_fp = input('Enter your damn file path(use foward slash), brad: ')
# filepath = 'C:/Users/ranch/Downloads/jack.txt'
            # print(sum(nums))
# for element in mylines:
#     print(element)

# try:
    # num = float(num)
#     if num == 'logical reads':
#         num = " " + num
#     print(num)
# except ValueError:
#     print('The provided value is not a number')
# num = 0 
# while True:
#     try:
#         num = int(input("Enter your favorite integer: "))
#     except ValueError:
#         print("Please enter a valid integer")
#         continue
#     else:
#         print(f'You entered: {num}')
#         break

# import re
# with open('C:/Users/J/Downloads/jack.txt', 'rt') as fp:
#     line = fp.readline()
#     while line:
#         match= re.search(r'(?<=logical reads )[^,]*',line)
#         if match is not None:
#             nums = int(match.group(0))
#             list_nums = [nums]
#             print(sum(list_nums))    
#         line = fp.readline()

# --------- close -------------
# path = 'C:/Users/J/Downloads/jack.txt'
# with open(path) as fp:
#     for line in fp:
#         match= re.search(r'(?<=logical reads )[^,]*',line)
#         if match is not None:
#             nums = int(match.group(0)) 
#             print(nums)
# --------------------------------------------------
import re
import np
usrInput = input("Stop asking me to calculate, Enter dir path: ")
# text = open('C:/Users/ranch/Downloads/jack.txt')
text = open(usrInput)
final = []
for line in text:
    line = line.strip()
    match = re.findall('(?<=logical reads )[^,]*',line)

    if len(match) > 0:
         lineVal = sum(map(int, match))
         final.append(lineVal)
        #  print("line sum = {0}".format(lineVal))
print("Final sum = {0}".format(np.sum(final)))
input("Press enter to close program")
# -------------------------------------------------------
