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
mylines = []
with open('C:/Users/ranch/Downloads/jack.txt', 'rt') as fp:
    for line in fp:
        mylines.append(line.rstrip('\n'))
for element in mylines:
    print(element)
    # line = fp.readline()
    # cnt = 1
    # while line:
    #     print("Line{}:{}".format(cnt,line.strip()))
    #     line = fp.readline()
    #     cnt += 1

# num = input('Enter the data: ')

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
