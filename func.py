# take number from user and get all the divisors of that number and print it

# import the module
import math

# define the function
def divisors(num):
    # define the list
    divisors = []
    # loop through the range of the number
    for i in range(1, int(math.sqrt(num)) + 1):
        # if the number is divisible by i
        if num % i == 0:
            # add i to the list
            divisors.append(i)
            # if the number is not divisible by i
            if i != num // i:
                # add the number divided by i to the list
                divisors.append(num // i)
                # sort the list
                divisors.sort()
    # return the list
    return divisors

# define the main function
def main():
    # ask the user to enter a number
    num = int(input("Enter a number: "))
    # print the list
    print(divisors(num))


# new program 
'''
Loop until the user enter non-positive number
first time the user enter a number, print it.
second time the user enter a number, combine the avarage of the two numbers and print it,
also print the sum of the two numbers.
with each number the user enter, do the same with all the numbers the user enter.
when the user enter a non-positive number, print the sum of the numbers the user enter, the avarage of the numbers the user enter, and the list of the numbers the user enter,
and exit the program.
'''
# define the function
def num_list():
    # define the list
    num_list = []
    # define the sum
    sum = 0
    
    # loop until the user enter non-positive number
    while True:
        # ask the user to enter a number
        num = int(input("Enter a number: "))
        #define the avarage
        # if the number is positive
        if num > 0:
            # add the number to the list
            num_list.append(num)
            # add the number to the sum
            sum += num
            #define the avarage
            avarage = sum / len(num_list)
            #print the avarage
            print(avarage)
            #print the sum
            print(sum)
            #print the list
            print(num_list)
        # if the number is not positive
        else:
            #print the sum
            print(sum)
            #print the avarage
            print(avarage)
            #print the list
            print(num_list)
            #exit the program
            print("that's all")
            print("bye")
            break

# new program
'''
Loop until user enter the same word twice
'''
# define the function
def word():
    # define the list
    word_list = []
    # define the word
    word = ""
    # loop until user enter the same word twice
    while True:
        # ask the user to enter a word
        word = input("Enter a word: ")
        # if the word is in the list
        if word in word_list:
            #print the word
            print(word)
            #exit the program
            print("that's all")
            print("bye")
            break
        # if the word is not in the list
        else:
            # add the word to the list
            word_list.append(word)
            #print the word
            print(word)

# new program - ETGAR 
'''
Loop until the user enter the same word three times
everytime the user enter a word, check if the word is in the list.
if the word is not in the list, add the word to the list.
if the word is in the list, add the word to the list and print the word.
when the user enter the same word three times, print the word that appears three times,
and exit the program.
'''
# define the function
def word_three():
    # define the list
    word_list = []
    # define the word
    word = ""
    # loop until the user enter the same word three times
    while True:
        # ask the user to enter a word
        word = input("Enter a word: ")
        # if the word is in the list
        if word in word_list:
            # add the word to the list
            word_list.append(word)
            #print the word
            print(word)
        # if the word is not in the list
        else:
            # add the word to the list
            word_list.append(word)
            #print the word
            print(word)
        # sort the list
        word_list.sort()
        # if the word is in the list three times
        if word_list.count(word) == 3:
            #print the word
            print(word)
            #exit the program
            print("that's all")
            print("bye")
            break

# new program
'''
check between two lists of numbers which list of number has bigger numbers than the other list
'''
# define the function
def list_compare():
    # define points to list 1 
    points_list1 = 0
    # define points to list 2
    points_list2 = 0
    # define the list 1
    list_1 = [3,6,2,10,5,4]
    # define the list 2
    list_2 = [1,7,3,1,9,4]
    # sort the list 1
    list_1.sort()
    # sort the list 2
    list_2.sort()
    # check if the smallest number in list 1 is bigger than the smallest number in list 2
    # if it is, add 1 to the points list 1
    # if it is not, add 1 to the points list 2
    if list_1[0] > list_2[0]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[1] > list_2[1]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[2] > list_2[2]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[3] > list_2[3]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[4] > list_2[4]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[5] > list_2[5]:
        points_list1 += 1
    else:
        points_list2 += 1
    # check who has more points
    # if list 1 has more points
    if points_list1 > points_list2:
        #print list 1
        print("the list with bigger numbers is: ")
        print(list_1)
    # if list 2 has more points
    elif points_list1 < points_list2:
        #print list 2
        print("the list with bigger numbers is: ")
        print(list_2)
    # if they have the same points
    else:
        #print list 1
        print("its a tie")

# new program
'''
The same program as the one above, but with a different way to check the list
if the one of the lists has more numbers than the other
check only the len number of the smaller list
'''
# define the function
def list_compare_2():
    # define points to list 1
    points_list1 = 0
    # define points to list 2
    points_list2 = 0
    # define the list 1
    list_1 = [3,6,2,10,5,4]
    # define the list 2
    list_2 = [7,3,9,4,5,11,30]
    # sort the list 1
    list_1.sort()
    # sort the list 2
    list_2.sort()
    # check if the smallest number in list 1 is bigger than the smallest number in list 2
    # if it is, add 1 to the points list 1
    # if it is not, add 1 to the points list 2
    if list_1[0] > list_2[0]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[1] > list_2[1]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[2] > list_2[2]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[3] > list_2[3]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[4] > list_2[4]:
        points_list1 += 1
    else:
        points_list2 += 1
    if list_1[5] > list_2[5]:
        points_list1 += 1
    else:
        points_list2 += 1
    # check who has more points
    # if list 1 has more points
    if points_list1 > points_list2:
        #print list 1
        print("the list with bigger numbers is: ")
        print(list_1)
    # if list 2 has more points
    elif points_list1 < points_list2:
        #print list 2
        print("the list with bigger numbers is: ")
        print(list_2)
    # if they have the same points
    else:
        #print list 1
        print("its a tie")

# call all the functions
main()
num_list()
word()
word_three()
list_compare()
list_compare_2()
# end of the program
print("end of the program")
print("bye")



        

        





