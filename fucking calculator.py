number = None 
operator = None 
result = None 
wait_for_number = True 
list_of_operator = ['+', '-', '/', '*', '=']


while True:
    while wait_for_number == True:
        try:
            number = float(input("Enter your number: "))
            if result == None:
                result = number 
                wait_for_number = False 
            else:
                if operator == '+':
                    result += number 
                    operator = None
                elif operator == '-':
                    result -= number 
                    operator = None
                elif operator == '*':
                    result *= number 
                    operator = None
                elif operator == '/':
                    result /= number 
                    operator = None
                wait_for_number = False
        except ValueError: 
            print ("Your value is not number!")
    else: 
        new_opearator = input("Enter operator: ")
        if new_opearator in list_of_operator:
            operator = new_opearator  
            wait_for_number = True
        else: 
            print("Invalid operator")
    if operator == '=' or number == '=':
        print(result)
        break



