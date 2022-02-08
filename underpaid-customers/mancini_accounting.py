#Read through accounting.py and understand what it does.



#Add comments explaining what your code does.

#Read over our solution and compare it to your own.

#accounting.py lists out the names of the new customers, how many melons they bough, and what they paid
#it then compares the amount paid to the total cost for the melons (expected to pay)
#it prints a statement for customers that overpaid in the format
#_________- paid $______, expected $________
#Sean paid $9.50, expected $9.00

#Create a function that takes in a text file of customer orders 
#and parses it to produce information on customers that under/over paid

#start by opening the file:
the_file=open("customer-orders.txt")

#create a function called get_incorrect_payments
#it takes in 1 argument 'text_file'
def get_incorrect_payments(the_file)


    #create a for loop
    #loop through each line
    #line.rstrip() removes any blank spaces
    #line.rstrip() breaks up the line into a list using the '|' symbol
    for line in the_file:
        line = line.rstrip()
        line = line.split('|')

        #example: ['965', 'Irene Ward', '14', '1.85']
        name = line[1]  #the name of the customer
        melons = line[2] #the number of melons that the customer bought
        paid = line[3] #the amount of money the customer paid

        #We need to compare the actual cost to the amount paid by the customer
        #each melon costs 1 dollar

        if float(melons) != float(paid):
            print(f'{name} paid ${paid} for {melons} melons ')



     
