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
        pass

def options_page():
    print("BOOK FLIGHT")
    print("ADD AIRLINES")
    print("EXIT\n")
    
    choice = input("").lower()
    
    if choice =='book' or '1':
        return 'book'
    elif choice =='add' or '2':
        return 'add'
    elif choice == 'exit' or '3':
        return 'exit'
    
def password(user):
    if user == 'tst123':
        return True
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
    