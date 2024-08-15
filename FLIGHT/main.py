from flight import Flight
from page import starting_page, options_page

def main():
    result_start = starting_page()
    if result_start:
        print("\n\n\n\n\n\n\n\n")
        airline = {
            'Cebu Pacific': 30,
            'Emirates': 2,
            'Jet Blue': 27
        }
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
                    return

                f.add_passenger(name)
                print(f"Remaining seats: {f.counter()}")

            print("Flight is fully booked!")
            break  # Ends the loop after a flight is fully booked.

if __name__ == "__main__":
    main()
