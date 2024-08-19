from flight import Flight
from page import starting_page, options_page, password, get_int


airline = {
        'Cebu Pacific': 30,
        'Emirates': 2,
        'Jet Blue': 27
    }
def main():
        result_start = starting_page()
        if not result_start:
            print("exiting app")
            return
        print("\n\n\n\n\n\n\n\n")
    
        while True:
            
            option=options_page()
            if option == 'book':

                while True:
                    print(f"Available airline: {',' .join(airline.keys())}")
                    airline_names = input("Name of airline (or type 'exit' to quit): ")
                    if airline_names.lower() == 'exit':
                        break

                    airline_name = airline.get(airline_names, None)
                    if airline_name is None:
                        print("Airline not found. Please try again.")
                        continue
                    
                    f = Flight(airline_name)
                    print("Enter the name of the passenger (or type 'exit' to quit):\n")

                    while f.counter() > 0:
                        name = input("Passenger name: ")
                        if name.lower() == 'exit':
                            break

                        f.add_passenger(name)
                        print(f"Remaining seats: {f.counter()}")
                        airline[airline_names] = f.counter()
                    print("Flight is fully booked!")
                    break
                    
            elif option == 'add':
                    admin_password = input('Admin password: ')
                    if password(admin_password):
                        airline_n = input("Name of the airline: ")
                        airline_seat = get_int("How many seats: ")
                        
                        airline[airline_n] = airline_seat
                        print(f'The airline {airline_n} has been added.')
                    else:
                        print("Wrong password. Access denied.")
            elif option== 'exit':
                return      
            
if __name__ == "__main__":
    main()
