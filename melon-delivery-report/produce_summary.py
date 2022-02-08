print("Day 1")

#built in function open() opens the txt file
the_file = open("um-deliveries-day-1.txt")

#this starts a for loop that is going through each line
#line.rstrip strips the empty spaces from the line
#line.split('|') creates a list called words 
#the list words has every section seperated by the '|' as an element in the list

for line in the_file:
    line = line.rstrip()
    words = line.split('|')


    #the following separates each part of the words list into variables
    #melon is the first element in the words list [0] means index 0
    #melon states the name of the melon
    #similarly count states the number of melons
    #amount states the price
    #melon, count and amount are all strings

    melon = words[0]
    count = words[1]
    amount = words[2]


    #the program will output the following print statement
    #f' is used for formating the variables into the print statement
    print(f"Delivered {count} {melon}s for total of ${amount}")

#the following command closes the file
the_file.close()

#Example of a print statemenet
#Delivered 18 Scaly Bark Watermelons for total of $72.00

#the following lines of code do the same thing using the txt file for day2 and day3
print("Day 2")
the_file = open("um-deliveries-day-2.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
