import json
import pickle

# File names
JSON_DB = 'flights.json'
BINARY_DB = 'flights.dat'

def load_json_db():
    try:
        with open(JSON_DB, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json_db(data):
    with open(JSON_DB, 'w') as f:
        json.dump(data, f, indent=2)

def load_binary_db():
    try:
        with open(BINARY_DB, 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

def save_binary_db(data):
    with open(BINARY_DB, 'wb') as f:
        pickle.dump(data, f)

def get_flight_input():
    return {
        "id": input("Flight ID: "),
        "number": input("Flight Number: "),
        "airline_name": input("Airline Name: "),
        "seats": int(input("Seats: ")),
        "price": float(input("Price: ")),
        "source": input("Source: "),
        "destination": input("Destination: ")
    }

def add_flight(db_type):
    flight = get_flight_input()
    if db_type == 'json':
        flights = load_json_db()
        flights.append(flight)
        save_json_db(flights)
    else:
        flights = load_binary_db()
        flights.append(flight)
        save_binary_db(flights)
    print("Flight added!")

def view_flights(db_type):
    if db_type == 'json':
        flights = load_json_db()
    else:
        flights = load_binary_db()
    if not flights:
        print("No flights found.")
        return
    print("\nFlights:")
    for f in flights:
        print(f)

def main():
    print("Select DB type:")
    print("1. JSON DB")
    print("2. Binary DB")
    db_choice = input("Enter 1 or 2: ").strip()
    db_type = 'json' if db_choice == '1' else 'binary'
    while True:
        print("\n1. Add Flight\n2. View All Flights\n3. Exit")
        choice = input("Select option: ").strip()
        if choice == '1':
            add_flight(db_type)
        elif choice == '2':
            view_flights(db_type)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()