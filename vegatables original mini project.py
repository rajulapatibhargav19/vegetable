
cart = ['brinjal', 'beans', 'tamoto','beatroot','carrot']
quantity = [125, 150, 100, 123, 145, ]
sell_price = [49, 44, 25, 47, 43]
cost_price = [28, 18, 13, 23,  27]
customer_name = []
customer_cart=[]
mobile_number = []
total_sales = 0
total_profit = 0
customer_data = []
cust_bill=[]
itemized_veg=[]
itemized_profit=[]
user_name = 'bhargav'
password1 = '00000'
while True:
    print('1.owner')
    print('2.coustomer')
    print('3.exist')
    n = input('enter your id:')
    if n == '1':#owner block
        while True:
            owner = input('Enter the username: ')
            password = input('Enter the password: ')
            if user_name == owner and password1 == password:
                print('\n', '*' * 10, 'Available Vegetables', '*' * 10)
                for v, q, r,c in zip(cart, quantity, sell_price,cost_price):
                    print(v,',', 'Quantity =', q, 'kg, 1kg sell Price = Rs', r,'kg, 1kg cost Price = Rs',c)
                    print()
                while True:
                    print('1. Add')
                    print('2. Remove')
                    print('3. Modify')
                    print('4. View')
                    print('5. View customer details')
                    print('6. View report')
                    print('7. Itemized profit')
                    print('8. Exit')
                    ch = input('Choose one option: ')                    
                    if ch == '1':  # Add an element to the owner_cart
                        vegetable = input('Which vegetable? : ')
                        if vegetable in cart:
                            print('vegetable already available')
                        else:
                            kg = float(input('How many kgs of the vegetable available?: '))
                            c_rs = float(input('enter cost price of 1kg per vegetable : '))
                            s_rs=float(input('enter selling price of 1kg per vegetable:'))
                            cart.append(vegetable)
                            quantity.append(kg)
                            cost_price.append(c_rs)
                            sell_price.append(s_rs)
                            print(vegetable, 'is added to cart')
                    elif ch == '2':  # Remove an element from the owner_cart
                        vegetable = input('Which vegetable do you want to remove?: ')
                        if vegetable in cart:
                            idx = cart.index(vegetable)
                            cart.pop(idx)
                            quantity.pop(idx)
                            cost_price.pop(idx)
                            sell_price.pop(idx)
                            print(vegetable, 'is removed from the cart')
                        else:
                            print(vegetable, 'is not available')
                    elif ch == '3':  # Modify owner_cart
                        vegetable = input('Enter which vegetable details you want to change: ')
                        if vegetable in cart:
                            idx = cart.index(vegetable)
                            print('Current details:', vegetable, '-','quantity is:', quantity[idx],'kg',',' ,'1kg sellingprice is : Rs', sell_price[idx],',','1kg costprice is : Rs',cost_price[idx])
                            new_kg = float(input('Enter the new quantity (kg): '))
                            new_sell_price = float(input('Enter the new sell price/per kg: '))
                            new_cost_price=float(input('Enter the new cost price/kg:'))
                            quantity[idx] = new_kg
                            cost_price[idx]=new_cost_price
                            sell_price[idx] = new_sell_price
                            print(vegetable, 'updated to :','quantity is:','kg',',', new_kg,'kg',',' ,'sellingprice 1kg is : Rs', new_sell_price,',','costprice 1kg is : Rs',new_cost_price)
                    elif ch == '4':  # View entire owner_cart
                        print('*' * 10, 'CART', '*' * 10)
                        for v, q, c,s in zip(cart, quantity, cost_price,sell_price):
                            print(v,'-', 'quantity is:', q,'kg',',' ,'1kg sellingprice is: Rs',s,',','1kg costprice is:Rs',c)
                        print('*' * 26)
                    elif ch == '5':  # view last customers details
                        if customer_cart:
                            print('*'*10,'last customer details','*'*10)
                            print('Item        Quantity   Price (per kg)  Total')
                            total_amount = 0
                            for i in range(len(customer_cart)):
                                item = customer_cart[i]
                                qty = customer_cart_qty[i]
                                idx = cart.index(item)
                                item_total = qty * sell_price[idx]
                                total_amount += item_total
                                print(item, qty, "Rs.", sell_price[idx], "Rs.", item_total)
                            print('-' * 10)
                            print('Total amount to pay: Rs.', total_amount)
                            print('Customer Name:', customer_name[-1])
                            print('Phone Number:', mobile_number[-1])
                        else:
                            print('There is no sales today')

                    elif ch == '6':  # View total_customers visted,total_sales,total_profit
                        print('*' * 10, 'DAILY SALES REPORT', '*' * 10)
                        if not customer_data:
                            print("No sales made today.")
                        else:
                            
                            print("Total Customers Served:", len(customer_data))
                            print("-" * 50)
                            print("Customer Name    Phone Number    Total Bill")
                            for data in customer_data:
                                cust_name, cust_phone, total_amount1, cust_bill2, cust_cart, cust_qty = data
                                cost_price_total = sum(q * cost_price[cart.index(f)] for f, q in zip(cust_cart, cust_qty))
                                profit = total_amount1 - cost_price_total
                                print("profit:",profit)
                             

                                total_sales += cust_bill2
                                total_profit=total_profit + profit
                                
                                print(cust_name.ljust(15), cust_phone.ljust(15), "Rs.", str(cust_bill2).ljust(15))
                            print('Total sales',total_sales)
                            print('Total profit',total_profit)
                    elif ch=='7':  #Itemized profit
                            for j,k in zip(itemized_veg,itemized_profit):
                                print('The itemized profit of',j,':','is Rs',k)

                    elif ch == '8':
                        break
                    else:
                        print('Choose the correct option')

            else:
                print('Please enter the correct username or password')
            break

    elif n == '2':                                          #customer_block
        print('*' * 10, 'WELCOME TO VEGETABLE STORE', '*' * 10)
        print('\n', '*' * 10, 'Available Vegetables', '*' * 10)
        for v, q, r in zip(cart, quantity, sell_price):
            print(v,',', 'Quantity =', q, 'kg, 1kg Price = Rs', r)
            print()

        customer_cart = []
        customer_cart_qty = []
        total_amount=0
       
        
        while True:
            end_shopping = input('Do you want to continue shopping?(yes/no):')
            if end_shopping == 'yes':
                while True:
                    print("1. Add Item to Cart")
                    print("2. Remove Item from Cart")
                    print("3. Update Cart")
                    print("4. View Cart")
                    print("5. Print Bill")
                    print("6. Exit")
                    ch =input('Enter the option: ')

                    if ch == '1':    #adding to customer cart
                        item = input('Which vegetable do you want to buy? ')
                        if item in customer_cart:
                            print('The vegetable is already in your cart.')
                        else:
                            if item in cart:
                                idx = cart.index(item)
                                qty = float(input(f"How many kgs of {item} do you want? "))
                                if qty <= quantity[idx]:
                                    amount = qty * sell_price[idx]
                                    quantity[idx] -= qty
                                    if item not in customer_cart:
                                        customer_cart.append(item)
                                        customer_cart_qty.append(qty)
                                    else:
                                        item_idx = customer_cart.index(item)
                                        customer_cart_qty[item_idx] += qty
                                    print(qty, 'kg of', item, 'added to your cart.')
                                else:
                                    print('Sorry, only', quantity[idx], 'kg of', item, 'is available.')
                            else:
                                print('Sorry', item, 'is not available')
                    elif ch == '2':  # Remove an element from the customer_cart
                            vegetable = input('Which vegetable do you want to remove?: ')
                            if vegetable in cart:
                                idx = customer_cart.index(vegetable)
                                customer_cart.pop(idx)
                                customer_cart_qty.pop(idx)
                                print(vegetable, 'is removed from yout cart')
                            else:
                                print(vegetable, 'is not available')

                    elif ch == '3':  # Modify customer_cart
                        vegetable = input('Enter which vegetable details you want to change: ')
                        if vegetable in customer_cart:
                            idx = customer_cart.index(vegetable)
                            main_idx = cart.index(vegetable)
                            print('Current details:', vegetable, '-', customer_cart_qty[idx], 'kg')
                            new_kg = float(input('Enter the new quantity (kg): '))
                            diff = new_kg - customer_cart_qty[idx]

                            if diff <= quantity[main_idx]:
                                quantity[main_idx] -= diff
                                customer_cart_qty[idx] = new_kg
                                print(vegetable, 'updated to:', new_kg, 'kg')
                            else:
                                print('Not enough stock available to increase the quantity. Available:', quantity[main_idx], 'kg')
                        else:
                            print(vegetable, 'is not in your cart.')



                    elif ch == '4':  # View entire cuastomer_cart
                        print('*' * 10, 'CART', '*' * 10)
                        for v, q, r in zip(customer_cart, customer_cart_qty, sell_price):
                            print(v, 'quantity', q, 'kg', '1kg price', 'Rs', r)
                        print('*' * 26)


                    elif ch == '5': #printing bill to customer by taking the details
                        if customer_cart:
                            customerdetails = input('Enter your name: ')
                            customerphno = input('Enter phone number: ')
                            if customerdetails.isalpha() and customerphno.isdigit():
                                if customerphno[0]=='9' or customerphno[0]=='8' or customerphno[0]=='7' or customerphno[0]=='6':
                                    if int(len(customerphno)) == 10:
                                        customer_name.append(customerdetails)
                                        mobile_number.append(customerphno)
                                        print('*' * 10, 'FINAL BILL', '*' * 10)
                                        print('Item',' '*5,'Quantity',' '*5,'Price (per kg)',' '*5,'Total')
                                        owner_total_profit = 0
                                        total_amount1=0
                                        cust_bill2=0
                                        for i in range(len(customer_cart)):
                                            f = customer_cart[i]                                
                                            q = customer_cart_qty[i]
                                            idx = cart.index(f)
                                            item_total = q * sell_price[idx]
                                            item_profit = item_total - (q * cost_price[idx])
                                            if f not in itemized_veg:
                                                itemized_veg.append(f)
                                                itemized_profit.append(item_profit)
                                            else:
                                                ind=itemized_veg.index(f)
                                                itemized_profit[ind]=itemized_profit[ind]+item_total
                                                
                                            total_amount1 =total_amount1+item_total
                                            cust_bill2=cust_bill2+total_amount1
                                            print(f,' '*5, q,"kg",' '*5,"Rs.",sell_price[idx],' '*5,"Rs.", ''*5,item_total)
                                                                        
                                        print('Total amount to pay: Rs.', total_amount1)
                                        customer_data.append([customerdetails, customerphno, total_amount1, cust_bill2, customer_cart.copy(), customer_cart_qty.copy()])
                                        print('Thank you for shopping with us!')
                                else:
                                    print('Invalid phone number.')
                            else:
                                print("Invalid name or mobile number")
                        else:
                            print('Your cart is empty. Please add items first.')
                    elif ch=='6':                        
                        break
                    else:
                        print('Invalid option, please try again.')
                        break
            else:
                print('*'*5,'THANKS FOR SHOPPING','*'*5)
                break
    elif n=='3':
        owner = input('Enter the username: ')
        password = input('Enter the password: ')
        if user_name == owner and password1 == password:
            print('*'*10,'Shop closed','*'*10)
        break
