import json
import csv

# Imports for option number 5 (custom)
data = [{"Flight ID": "FL123", "Destination": "New York", "Count of seats": 8}]
seats = {"FL123": [{"Place": "A1", "Name": "Vlad"}, {"Place": "A2", "Name": "Dalv"}, {"Place": "A3", "Name": "Moshe"},
                   {"Place": "A4", "Name": ""}, {"Place": "A5", "Name": ""}, {"Place": "A6", "Name": ""},
                   {"Place": "A7", "Name": ""}, {"Place": "A8", "Name": ""}]}


def print_menu():
    print("=" * 20)
    print("1. Add a new flight",
          "\n2. Book a ticket",
          "\n3. Cancel a booking",
          "\n4. View flight details"
          "\n5. Save results (data -> file.json, seats -> file.csv)",
          "\n6. Exit")
    print("=" * 20)


def choice_1(data_input, seats_input):
    flight_id = str(input("Enter Flight ID: "))
    seats_input[flight_id] = []
    destination = str(input("Enter Destination: "))
    while True:
        try:
            count_of_seats = int(input("Enter Count of seats: "))
            break
        except ValueError:
            continue
    for n in range(count_of_seats):
        temp = {"Place": "A" + str(n + 1), "Name": ""}
        seats_input[flight_id].append(temp)
    new_flight = {"Flight ID": flight_id, "Destination": destination, "Count of seats": count_of_seats}
    data_input.append(new_flight)
    print("Successfully!")
    return data_input, seats_input


def choice_2(data_input, seats_input):
    for a, i in enumerate(data_input): print(f" {a + 1}) Flight ID: {i["Flight ID"]}")
    while True:
        flight_ID = str(input("Enter Flight ID:"))
        if flight_ID not in seats_input:
            print("Try again!")
        else:
            break
    for i in seats_input[flight_ID]:
        if i["Name"] == "":
            print(f"Place for order: {i["Place"]}")

    while True:
        place = str(input("Enter seat number: "))
        flag = False
        for i in seats_input[flight_ID]:
            if i["Name"] != "" and i["Place"] == place:
                print("This place is order")
            elif i["Name"] == "" and i["Place"] == place:
                flag = True
        if flag == True:
            break
    name = str(input("Your name: "))
    for i in seats_input[flight_ID]:
        if i["Place"] == place:
            i["Name"] = name
    print(f"Ticket booked successfully! Your seat: {place} and your name: {name}")


def choice_3(seats_input):
    flag = True
    count = 0
    print(seats_input.keys())
    while True:
        flight_ID = str(input("Enter Flight ID:"))
        if flight_ID not in seats_input:
            print("Try again!")
        else:
            break
    for place in seats_input[flight_ID]:
        if place["Name"] != "":
            count += 1
            print(f"Place: {place["Place"]} | Name: {place["Name"]}")
    if count == 0:
        print("All places are free!")
        flag = False
    while flag:
        seat = str(input("Enter seat number: "))
        for place in seats_input[flight_ID]:
            if seat == place["Place"]:
                place["Name"] = ""
                print("Successfully!")
                flag = False
        if flag == True: print("Seat not found, try again")


def choice_4(data):
    for a, i in enumerate(data): print(f" {a + 1}) Flight ID: {i["Flight ID"]}")
    flag = True
    while flag:
        choice = str(input("Flight ID or exit:"))
        for i in data:
            if choice.lower() == "exit":
                flag = False
                break
            elif choice == i["Flight ID"]:
                flag = False
                break
            elif choice != i["Flight ID"]:
                flag = True
        print("Try again or enter Exit")
    for i in data:
        if i["Flight ID"] == choice:
            print("=" * 20)
            print("Flight ID: ", i["Flight ID"],
                  "\nDestination: ", i["Destination"],
                  "\nSeats:")
            for j in seats[choice]:
                print(f" Place: {j["Place"]} Name: {j["Name"]}")
            print("=" * 20)
    a = input("Press \"|Enter|\" Program is waiting...")


def choice_5(data_input, seats_input):
    file_name_for_data = str(input("Enter file name for data: "))
    file_name_for_data += ".json"
    with open(file_name_for_data, "w") as file_json:
        json.dump(data_input, file_json)
    file_name_for_seats = str(input("Enter file name for seats: "))
    file_name_for_seats += ".csv"
    seats_for_csv = [['ID', 'Seat', 'Name']]
    for id, seat in seats_input.items():  #turn dictionary in array for csv.
        print(id, seat)
        for s in seat:
            name = s["Name"]
            if name == "":
                name = "Place for order"
            seats_for_csv.append([id, s["Place"], name])
    with open(file_name_for_seats, "w", newline="") as file_csv:
        writer = csv.writer(file_csv)
        for d in seats_for_csv:
            writer.writerow(d)

    print(f"Successfully! Data saved in {file_name_for_data} and seats saved in {file_name_for_seats}")


""" |Code| """

while True:
    print_menu()
    while True:
        try:
            choice = int(input("Enter option: "))
        except ValueError:
            continue
        if choice < 1 or choice > 6:
            print("Enter number between 1 and 5")
            continue
        else:
            break
    if choice == 1:
        choice_1(data, seats)
    elif choice == 2:
        choice_2(data, seats)
    elif choice == 3:
        choice_3(seats)
    elif choice == 4:
        choice_4(data)
    elif choice == 5:
        choice_5(data, seats)
    elif choice == 6:
        a = str(input("Do you want to save actual data? yes/no: "))
        if a.lower() == "yes":
            choice_5(data, seats)
        elif a.lower() == "no":
            print("Goodbye!")
            break
