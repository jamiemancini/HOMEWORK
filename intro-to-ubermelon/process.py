
#program starts by opening up the txt file using the built in function open()
#and names it to the variable log_file
log_file = open("um-server-01.txt")

#I checked the type of log_file and I don't really understand what it is
#print(type(log_file))
#<class '_io.TextIOWrapper'>

#this is creating a function called sales_reports
#which takes in 1 argument: log_file
def sales_reports(log_file):

    #this creates a for loop that is going through every line of the log_file
    for line in log_file:

        #the built-in .rstrip method will remove any trailing characters
        #from each line
        line = line.rstrip()

        #this is slicing the list and only keeping the first 3 letters of the string
        # in this case the first 3 elements are the day of the week 
        day = line[0:3]
        

        #if day matches the string 'Mon'
        #then it will print out the line
        if day == "Mon":
            print(line)


print("We will run the function sales_report using the log_file as the parameter")
sales_reports(log_file)


