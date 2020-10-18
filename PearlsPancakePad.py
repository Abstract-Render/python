price_of_food_items = [3.25,4.00,2.50,1.25,3.99,1.25,2.00]
menu_of_food_items = "1) eggs $3.25 \n2)bacon $4.00 \n3) pancakes$2.50 \n4) orange juice$1.25 \n5) oatmeal $3.99 \n6) milk$1.25 \n7) donut $2.00"
tip_values = [.1,.15,.2,.25]
daily_total = []
def get_table_number():
    table_number = int(input("Enter your table number: "))
    return table_number

def get_number_of_diners_at_table():
    number_of_diners = 0
    while number_of_diners not in range(1,5):
        number_of_diners = int(input("Enter the number of people dining: (1-4)"))
    return number_of_diners

def display_menu_of_food_items(menu_of_food_items):
    print(menu_of_food_items)

def get_menu_item():
    menu_item = 0
    if menu_item not in range(1,8):
        menu_item = int(input("Enter a menu item number"))
    return menu_item
def get_diner_order():
    total_cost = 0.0
    display_menu_of_food_items(menu_of_food_items)
    while input("‘Do you want to order an item? Answer y or n") == 'y':
        menu_item = get_menu_item()
        price = price_of_food_items[(menu_item-1)]
        total_cost += price
    return total_cost
def calculate_table_total(table_total):
    
    return table_total + (table_total * .08) 
def display_diners_totals(total_before_tax, total_after_tax):
    print("Your total before tax is: "+str(total_before_tax)+" your total after tax is "+ str(total_after_tax))
def display_table_total_info(table_total):
  
    print("1) 10% tip: {}\n" "2) 15% tip: {}\n3) 20% tip: {}\n4) 25% tip: {}".format(tip_values[0]*table_total,tip_values[1]*table_total,tip_values[2]*table_total,tip_values[3]*table_total))
    tip_percent = int(input("Enter a tip option."))
    total_plus_tip = 0
    if tip_percent <= int(len(tip_values)) and tip_percent >= 1:
        total_plus_tip  = tip_values[(tip_percent-1)] * table_total + table_total
    else:
        print("No tip was added")

    return total_plus_tip
def get_table_order(num_diners):
    total_before_tax = 0.0
    grand_total = 0.0
    i = 1
    while i <= num_diners:
        total_before_tax += get_diner_order()
        i += 1
        table_total_after_tax =  calculate_table_total(total_before_tax)
        display_diners_totals(total_before_tax,table_total_after_tax)
        grand_total = display_table_total_info(total_before_tax)
    return grand_total
#its not adding the totals per table for the day may need a class
def main():
    
    table_number = get_table_number()
    table_total = get_table_order(get_number_of_diners_at_table())
    daily_total.append(table_total)
    print("For table : " + str(table_number))
    while  input("Would you like to continue serving a table for today? y/n") == 'y':
        main()
    else:
        print("You are about to close the program. Daily total: ") 
        print(daily_total)
    return sum(daily_total)
        
day_money = main()
print("Your net daily total is "+ str(day_money))

