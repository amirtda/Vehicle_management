
from exception.vehicle_not_found import VehicleNotFoundException
from model.vehicle import Vehicle
from repository.vehicle_repository import VehicleRepository  # if 'app' is not present



def display_menu():
    print("\nVehicle Management System")
    print("1. Add Vehicle")
    print("2. Update Owner")
    print("3. Delete Vehicle")
    print("4. List All Vehicles")
    print("5. Search Vehicles")
    print("6. Filter by Type")
    print("7. Exit")


def get_vehicle_details():
    reg = input("Enter registration number: ")
    model = input("Enter model: ")
    v_type = input("Enter vehicle type: ")
    owner = input("Enter owner name: ")
    return Vehicle(0, reg, model, v_type, owner)


def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-7): ")

        try:
            with VehicleRepository() as repo:
                if choice == '1':
                    vehicle = get_vehicle_details()
                    repo.add_vehicle(vehicle)
                    print("Vehicle added successfully!")

                elif choice == '2':
                    vehicle_id = int(input("Enter vehicle ID: "))
                    new_owner = input("Enter new owner name: ")
                    repo.update_owner(vehicle_id, new_owner)
                    print("Owner updated successfully!")

                elif choice == '3':
                    vehicle_id = int(input("Enter vehicle ID to delete: "))
                    repo.delete_vehicle(vehicle_id)
                    print("Vehicle deleted successfully!")

                elif choice == '4':
                    vehicles = repo.get_all_vehicles()
                    if not vehicles:
                        print("No vehicles found in the database.")
                    else:
                        for v in vehicles:
                            print(v)

                elif choice == '5':
                    search_term = input(
                        "Enter search term (registration or model): ")
                    results = repo.search_vehicles(search_term)
                    print(f"Found {len(results)} matching vehicles:")
                    for v in results:
                        print(v)

                elif choice == '6':
                    v_type = input("Enter vehicle type to filter: ")
                    results = repo.filter_by_type(v_type)
                    if not results:
                        print(f"No vehicles found of type '{v_type}'")
                    else:
                        print(f"Vehicles of type '{v_type}':")
                        for v in results:
                            print(v)

                elif choice == '7':
                    print("Exiting application...")
                    break

                else:
                    print("Invalid choice! Please enter 1-7")

        except VehicleNotFoundException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Invalid input format. Please enter numbers for IDs.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
