
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost()
    '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity()
    '''
    Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
         return   f"""
    ***********************************\n
    Country: {self.country} \n
    Code: {self.code}\n
    Product: {self.product} \n
    Cost: {self.cost}\n  
    Quantity: {self.quantity}\n      
    ***********************************"""
    '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    with open("inventory.txt", "r+") as f:
        shoe_file = f.readlines()
        try:
            for shoe in shoe_file[1:]:
                shoe.strip("\n")
                shoe_details = shoe.split(",")
                shoe_object = Shoe (shoe_details[0], shoe_details[1], shoe_details[2],shoe_details[3],shoe_details[4])
                shoe_list.append(shoe_object)  
        except Exception as e:
            print(e)
            print("error generating shoe_list!")

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    country_of_shoe = input("Which country is the shoe made of? ")
    code_of_shoe = input ("Please input the code for the shoe: ")
    product_of_shoe = input ("Please input the product name of the shoe: ")
    cost_of_shoe = input ("Please input the cost of the shoe: ")
    quantity_of_shoe = input ("Please input the quantity of the shoe: ")
    shoe_object = Shoe(country_of_shoe, code_of_shoe, product_of_shoe, cost_of_shoe, quantity_of_shoe)
    shoe_list.append(shoe_object)
    with open("inventory.txt","a") as f:
        f.write(f"\n{country_of_shoe},{code_of_shoe},{product_of_shoe},{cost_of_shoe},{quantity_of_shoe}")

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    for shoe in shoe_list:
        print( f"""
    ***********************************\n
    Country: {shoe.country} \n
    Code: {shoe.code}\n
    Product: {shoe.product} \n
    Cost: {shoe.cost}\n  
    Quantity: {shoe.quantity}\n      
    ***********************************""")
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    idx = 0
    for position, shoe in enumerate (shoe_list):        
        if int(shoe.quantity) < int(shoe_list[idx].quantity):
            idx = position
    print( f"""
    ***********************************
    Country: {shoe_list[idx].country} 
    Code: {shoe_list[idx].code}
    Product: {shoe_list[idx].product}
    Cost: {shoe_list[idx].cost}
    Quantity: {shoe_list[idx].quantity}   
    ***********************************""")
    user_choice = input("Would you like to re-stock? Y/N: ")
    if user_choice == "Y":
        desired_quantity = input("Please input the desired quantity to stock to: ") 
        shoe_list[idx].quantity = desired_quantity+'\n'
    with open("inventory.txt","w") as f:
        heading = 'Country,Code,Product,Cost,Quantity\n'
        f.write(heading)
        for shoe in shoe_list:
            f.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}')
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    shoe_code = input("Please enter the code of shoe you would like to search: ")
    for shoe in shoe_list:
        if shoe_code == shoe.code:
            print( f"""
    ***********************************\n
    Country: {shoe.country} \n
    Code: {shoe.code}\n
    Product: {shoe.product} \n
    Cost: {shoe.cost}\n  
    Quantity: {shoe.quantity}\n      
    ***********************************""")
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    print("------Total Value per product-------:")
    for shoe in shoe_list:
        shoe_cost= int(shoe.cost)
        shoe_quantity = int(shoe.quantity)
        shoe_value = shoe_cost * shoe_quantity
        print(shoe_value)
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    idx = 0
    for position, shoe in enumerate (shoe_list):        
        if int(shoe.quantity) > int(shoe_list[idx].quantity):
            idx = position
    print(f"{shoe_list[idx].product} is now for Sale!!!")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:    
    read_shoes_data()  
    user_choice = input("""What would you like to do? 
----------------------------------------------------------
    1:view_all_shoes\n
    2:search_shoe\n
    3:shoe_on_sale\n
    4:calculate_value\n
    5:re_stock\n
    6:capture_shoes\n
    7:exit\n
    -----------------------------------------------------------\n""")
    if user_choice == "1": 
        view_all()
    elif user_choice == "2": 
        search_shoe()
    elif user_choice == "3":  
        highest_qty()
    elif user_choice == "4": 
        value_per_item()
    elif user_choice == "5": 
        re_stock()
    elif user_choice == "6":
        capture_shoes()
    elif user_choice == "7":
        exit()
    else:
        print("Invalid choice! Please enter again!")      