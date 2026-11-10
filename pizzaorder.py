print("Welcome to Pizza Hut\n")

bill = 0
print("Select base size:")
print("Small Pizza (S): ₹15")
print("Medium Pizza (M): ₹20")
print("Large Pizza (L): ₹25\n")

while 1:
    size = input("Enter the size: ").lower()

    if size in ('s', 'small'):
        print("Entered size is Small\n")
        bill += 15
        break

    elif size in ('m', 'medium'):
        print("Entered size is Medium\n")
        bill += 20
        break

    elif size in ('l', 'large'):
        print("Entered size is Large\n")
        bill += 25
        break

    else:
        print("You typed the wrong input! Please try again\n")

print(f"Bill: {bill}")

print("\nToppings?\n")
if size == 's':
    choice1 = input("Pepperoni (+ ₹2): Y or N ?").lower()
    if choice1 in ('y', 'yes'):
        print("\nPepperoni added!\n")
        bill = bill + 2

if size == 'm' or size == 'l':
    while True:

        choice1 = input("Pepperoni (+ ₹5): Y or N ? ").lower()
        if choice1 in ('y', 'yes'):
            print("\nPepperoni added!\n")
            bill = bill + 5
        elif choice1 in ('n', 'no'):
            choice2=input(("You typed no. Do you wish to reconsider your choice? (Y or N): ")).lower()
            if choice2 in ('y', 'yes'):
                while True:
                    ctr=0
                    choice1 = input("Pepperoni (+ ₹5): Y or N ? ").lower()
                    if choice1 in ('y', 'yes'):
                        print("\nPepperoni added!\n")
                        bill = bill + 5
                        break
                    elif choice1 in ('n','no'):
 
print(f"Bill: {bill}")

cheese = input("\nCheese? (+ ₹2): Y or N ? ")
if cheese in ('y', 'yes'):
    print("\nCheese added!\n")
    bill = bill + 2

print(f"Total Bill: ₹{bill}")
    