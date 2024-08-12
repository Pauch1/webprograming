def starting_page():
    print('\t\tENTER')
    print('\t\tEXIT')
    print("\n")

    
    choice = input("\t\t").lower()
    if choice == 'enter':
        return True
    elif choice == ' exit':
        return False
    else:
        return None

def options_page():
    print("BOOK FLIGHT")
    print("ADD AIRLINES")
    print("EXIT\n")
    
    choice = input("").lower()
    
    if choice =='book flight':
        return 'book'
    elif choice =='add airlines':
        return 'add'
    else:
        return False