#printing title of the project
print("It's a Calculator")

#taking input from the user to know the operation to perform and values
#taken while loop to repeat the same action which is to ask the input values
while True:
    operation=input("Operation to perform +, -, *, /, %, //, **: ")
    first_value=eval(input("Enter the first number: "))
    second_value=eval(input("Enter the second number: "))


#making condition based on operations to perform

    if operation == '+':
        print("Addition of",first_value,operation,second_value,"=",first_value+second_value,"\n")

    elif operation == '-':
        print("Subtraction of",first_value,operation,second_value,"=",first_value-second_value,"\n")

    elif operation == '*':
        print("Multiplication of",first_value,operation,second_value,"=",first_value*second_value,"\n")
            
    elif operation == '/':
        print("Division of",first_value,operation,second_value,"=",first_value/second_value,"\n")
            
    elif operation == '%':
        print("Percentage of",first_value,operation,second_value,"=",first_value%second_value,"\n")
            
    elif operation == '//':
        print("Modules of",first_value,operation,second_value,"=",first_value//second_value,"\n")
        
    elif operation == '**':
        print(first_value,operation,second_value,"=",first_value**second_value,"\n")


    print("I hope you are statisfied with our application\nif yes, please rate our application \n\n")

