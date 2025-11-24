expense_book = [] 

running = True

while running:
    print("\n" + "="*40)
    print("  INFINITE EXPENSE MANAGER")
    print("="*40)
    print("1. Add New Expense")
    print("2. View Expenses (Filter by Month)")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")


    if choice == '1':
        print("\n---  Add New Entry ---")
        month = input("Enter Month (e.g., January): ").strip().title()
        week  = input("Enter Week (e.g., Week 1): ").strip().title()
        day   = input("Enter Day (e.g., Monday): ").strip().title()
        item  = input("What did you buy? (Item Name): ").strip().title()
        
        try:
            cost = float(input(f"How much was the {item}? "))
            entry = {
                "month": month,
                "week": week,
                "day": day,
                "item": item,
                "cost": cost
            }
            expense_book.append(entry)
            print(f" Saved: {item} for {cost} in {month}, {week}.")
            
        except ValueError:
            print(" Error: Cost must be a number.")
    elif choice == '2':
        if not expense_book:
            print("\nYour expense book is empty.")
        else:
            print("\n--- View Report ---")
            search_month = input("Which Month do you want to calculate? (Enter 'All' for everything): ").strip().title()
            
            print(f"\nRunning Report for: {search_month}")
            print(f"{'Day':<10} | {'Week':<10} | {'Item':<15} | {'Cost'}")
            print("-" * 50)
            
            total_spent = 0
            found_count = 0
            for entry in expense_book:
                if entry['month'] == search_month or search_month == 'All':
                    
                    print(f"{entry['day']:<10} | {entry['week']:<10} | {entry['item']:<15} | {entry['cost']}")
                    total_spent = total_spent + entry['cost']
                    found_count = found_count + 1
            
            print("-" * 50)
            if found_count == 0:
                print(f"No expenses found for {search_month}.")
            else:
                print(f"TOTAL SPENT in {search_month}: {total_spent}")
    elif choice == '3':
        print("Exiting... Don't spend too much! Bye.")
        running = False
        
    else:
        print("Invalid choice. Please try again.")