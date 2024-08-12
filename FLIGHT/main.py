from flight import Flight
from page import starting_page, options_page

def main():
    result_start = starting_page()
    if result_start == True:
        print("\n\n\n\n\n\n\n\n")
        airline = {
            'Cebu Pacific': 30,
            'Emirates': 2,
            'Jet Blue': 27
        }
        
        print(airline)
        airline_names = input("name of airline: ")
        airline_name = airline.get(airline_names, None)
        if airline_name == None:
            print(None)
            return
        f = Flight(airline_name)
        
        print("name of the passenger\n")
        while f.counter() > 0:
            
            name = input("")
            if name == 'exit':
                return
            f.add_passenger(name)
            print(f"remaning seat: {f.counter()}")

            
        
        
        
        
        

if __name__ == "__main__":
    main()