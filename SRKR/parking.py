from collections import deque
from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, license_plate, entry_time, level):
        self.license_plate = license_plate
        self.entry_time = entry_time
        self.exit_time = None
        self.level = level

    def set_exit_time(self):
        self.exit_time = datetime.now()

    def get_duration_hours(self):
        if not self.exit_time:
            return 0
        duration = self.exit_time - self.entry_time
        return max(1, int(duration.total_seconds() // 3600))  # Minimum 1 hour

    def __str__(self):
        return f"Vehicle {self.license_plate} | Level: {self.level} | Entry: {self.entry_time.strftime('%Y-%m-%d %H:%M:%S')}"

class ParkingSlot:
    def __init__(self, slot_id, level):
        self.slot_id = slot_id
        self.level = level
        self.is_occupied = False
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self):
        v = self.vehicle
        self.vehicle = None
        self.is_occupied = False
        return v

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Available"
        return f"Slot {self.slot_id} [Level {self.level}] - {status}"

class ParkingLot:
    def __init__(self, levels, slots_per_level, hourly_rate=10):
        self.levels = levels
        self.slots_per_level = slots_per_level
        self.hourly_rate = hourly_rate
        self.slots = {level: [ParkingSlot(f"{level}-{i+1}", level) for i in range(slots_per_level)] for level in range(1, levels + 1)}
        self.entry_queue = deque()
        self.exit_stacks = {level: [] for level in range(1, levels + 1)}
        self.parked_vehicles = {}

    def park_vehicle(self, license_plate):
        now = datetime.now()
        for level in range(1, self.levels + 1):
            for slot in self.slots[level]:
                if not slot.is_occupied:
                    vehicle = Vehicle(license_plate, now, level)
                    slot.assign_vehicle(vehicle)
                    self.entry_queue.append(vehicle)
                    self.exit_stacks[level].append(vehicle)
                    self.parked_vehicles[license_plate] = (vehicle, slot)
                    print(f"Vehicle {license_plate} parked at Slot {slot.slot_id} (Level {level})")
                    return
        print("No available slots!")

    def vehicle_exit(self, license_plate):
        if license_plate not in self.parked_vehicles:
            print("Vehicle not found!")
            return

        vehicle, slot = self.parked_vehicles.pop(license_plate)
        vehicle.set_exit_time()
        slot.remove_vehicle()
        fee = vehicle.get_duration_hours() * self.hourly_rate
        self.exit_stacks[vehicle.level] = [v for v in self.exit_stacks[vehicle.level] if v.license_plate != license_plate]
        self.entry_queue = deque([v for v in self.entry_queue if v.license_plate != license_plate])

        print(f"Vehicle {license_plate} exited from Level {vehicle.level}")
        print(f"Parking Duration: {vehicle.get_duration_hours()} hour(s)")
        print(f"Total Fee: ${fee}")

    def view_available_slots(self):
        print("\nAvailable Slots:")
        for level in range(1, self.levels + 1):
            available = [slot for slot in self.slots[level] if not slot.is_occupied]
            print(f"Level {level}: {len(available)} slots available")
            for slot in available:
                print(f"  - {slot.slot_id}")

    def display_parked_vehicles(self):
        print("\nCurrently Parked Vehicles:")
        if not self.parked_vehicles:
            print("No vehicles parked.")
            return
        for vehicle, slot in self.parked_vehicles.values():
            print(f"{vehicle} | Slot: {slot.slot_id}")

    def view_exit_stack(self, level):
        print(f"\nExit Stack for Level {level}:")
        if level not in self.exit_stacks:
            print("Invalid level.")
            return
        for vehicle in reversed(self.exit_stacks[level]):
            print(f" - {vehicle.license_plate} (Parked at {vehicle.entry_time.strftime('%H:%M:%S')})")

    def view_entry_queue(self):
        print("\nEntry Queue:")
        for vehicle in self.entry_queue:
            print(f" - {vehicle.license_plate} (Entry: {vehicle.entry_time.strftime('%H:%M:%S')})")


def print_menu():
    print("\n--- Parking Lot Menu ---")
    print("1. Park Vehicle")
    print("2. Vehicle Exit")
    print("3. View Available Slots")
    print("4. Display All Parked Vehicles")
    print("5. View Exit Stack by Level")
    print("6. View Entry Queue")
    print("7. Exit System")

def run_parking_system():
    levels = int(input("Enter number of levels: "))
    slots_per_level = int(input("Enter slots per level: "))
    lot = ParkingLot(levels, slots_per_level)

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            plate = input("Enter vehicle license plate: ")
            lot.park_vehicle(plate)

        elif choice == "2":
            plate = input("Enter vehicle license plate to exit: ")
            lot.vehicle_exit(plate)

        elif choice == "3":
            lot.view_available_slots()

        elif choice == "4":
            lot.display_parked_vehicles()

        elif choice == "5":
            level = int(input("Enter level number: "))
            lot.view_exit_stack(level)

        elif choice == "6":
            lot.view_entry_queue()

        elif choice == "7":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")

run_parking_system()
