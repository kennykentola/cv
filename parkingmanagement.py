import random
import time
from datetime import datetime

CAR = 1
SCOOTER = 2

class Vehicle:
    def __init__(self, num, row, col, v_type):
        self.num = num
        self.row = row
        self.col = col
        self.type = v_type
        self.at = datetime.now()

car = [[None for _ in range(10)] for _ in range(2)]
scooter = [[None for _ in range(10)] for _ in range(2)]
parkinfo = [[0 for _ in range(10)] for _ in range(4)]
vehcount = 0
carcount = 0
scootercount = 0

def display():
    print("Cars ->")
    for r in range(4):
        if r == 2:
            print("Scooters ->")
        for c in range(10):
            print(parkinfo[r][c], end='\t')
        print()

def changecol(v):
    v.col -= 1

def add(t, num, row, col):
    global vehcount, carcount, scootercount
    v = Vehicle(num, row, col, t)
    
    if t == CAR:
        carcount += 1
    else:
        scootercount += 1
    
    vehcount += 1
    parkinfo[row][col] = num
    insert_record(num, t, row, col, datetime.now())
    backup_write(t)
    r = random.randint(0, 19)
    if r < 5:
        print("\a")
        print("\a")
        fine_sheet(num, t, row, col, datetime.now())

    return v

def add_on_start(t, num, row, col):
    v = Vehicle(num, row, col, t)

    if t == CAR:
        carcount += 1
    else:
        scootercount += 1

    vehcount += 1
    parkinfo[row][col] = num
    return v

def insert_record(veh, v_type, row, col, dt):
    with open("arival.dat", "a") as fptr:
        fptr.write("\n")
        fptr.write(f"{veh} {v_type} {row} {col} ")
        fptr.write(f"{dt.day}/{dt.month}/{dt.year} ")
        fptr.write(f"{dt.hour}:{dt.minute}:{dt.second} ")

def insert_record2(veh, dt):
    with open("depart.dat", "a") as fptr:
        fptr.write("\n")
        fptr.write(f"{veh} ")
        fptr.write(f"{dt.day}/{dt.month}/{dt.year} ")
        fptr.write(f"{dt.hour}:{dt.minute}:{dt.second} ")

def get_arrival_time(num):
    veh, v_type, row, col = 0, 0, 0, 0
    at, dt = None, None

    with open("arival.dat", "r") as fptr:
        while True:
            line = fptr.readline().strip()
            if not line:
                break

            veh, v_type, row, col, date_str, time_str = line.split()
            veh, v_type, row, col = int(veh), int(v_type), int(row), int(col)
            day, mon, year = map(int, date_str.split('/'))
            hour, minute, sec = map(int, time_str.split(':'))
            at = datetime(year, mon, day, hour, minute, sec)

            if veh == num:
                break

    with open("depart.dat", "r") as fptr:
        while True:
            line = fptr.readline().strip()
            if not line:
                break

            veh2, date_str2, time_str2 = line.split()
            veh2 = int(veh2)
            day2, mon2, year2 = map(int, date_str2.split('/'))
            hour2, minute2, sec2 = map(int, time_str2.split(':'))
            dt = datetime(year2, mon2, day2, hour2, minute2, sec2)

            if veh2 == num:
                break

    t_sec1 = sec2 + minute2 * 60 + hour2 * 60 * 60
    t_sec2 = sec + minute * 60 + hour * 60 * 60
    t_sec3 = t_sec1 - t_sec2
    secnd = t_sec3 % 60
    temp1 = t_sec3 - secnd
    temp2 = temp1 // 60
    minute = temp2 % 60
    temp4 = temp2 - minute
    hours = temp4 // 60

    print(f"you have parked your vehicle for {hours}:{minute}:{secnd}")

def randint():
    return random.randint(0, 19)

def finesheet(veh, v_type, row, col, dt):
    with open("finesheet.dat", "a") as fptr:
        fptr.write("\n")
        fptr.write(f"{veh} {v_type} {row} {col} ")
        fptr.write(f"{dt.day}/{dt.month}/{dt.year} ")
        fptr.write(f"{dt.hour}:{dt.minute}:{dt.second} ")
        fptr.write("50 ")

def historyrec(val):
    filename = ""
    if val == 1:
        filename = "arival.dat"
    elif val == 2:
        filename = "depart.dat"
    elif val == 3:
        filename = "finesheet.dat"
    else:
        print("Invalid input")
        return

    with open(filename, "r") as fptr:
        print(fptr.read())

def backup_write():
    with open("backupwr.dat", "w") as fptr:
        for r in range(4):
            for c in range(10):
                fptr.write(f"\n{parkinfo[r][c]} {r} {c} {vehcount} {carcount} {scootercount} ")

def backup_read():
    park = [[0 for _ in range(10)] for _ in range(4)]
    with open("backupwr.dat", "r") as fptr:
        for r in range(4):
            for c in range(10):
                line = fptr.readline().strip()
                park[r][c], rr, cc, veh, carrr, scoot = map(int, line.split())
                if park[r][c] != 0:
                    if r == 0 or r == 1:
                        car[r][c] = add_on_start(1, park[r][c], r, c)
                    else:
                        scooter[r][c] = add_on_start(2, park[r][c], r, c)
    return park

def get_free_row_col(v_type):
    from_row, to_row = 0, 2
    if v_type == SCOOTER:
        from_row += 2
        to_row += 2
    
    for r in range(from_row, to_row):
        for c in range(10):
            if parkinfo[r][c] == 0:
                return r, c
    return -1, -1

def get_rc_by_info(v_type, num):
    from_row, to_row = 0, 2
    if v_type == SCOOTER:
        from_row += 2
        to_row += 2

    for r in range(from_row, to_row):
        for c in range(10):
            if parkinfo[r][c] == num:
                return r, c
    return -1, -1

def main():
    global vehcount, carcount, scootercount

    carparking = backup_read()

    while True:
        print("\nCar Parking")
        print("1. Arrival of a vehicle")
        print("2. Total no. of vehicles parked")
        print("3. Total no. of cars parked")
        print("4. Total no. of scooters parked")
        print("5. Display order in which vehicles are parked")
        print("6. Departure of vehicle")
        print("7. Check History")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nAdd:")
            v_type = 0

            while v_type != CAR and v_type != SCOOTER:
                v_type = int(input("Enter vehicle type (1 for Car / 2 for Scooter): "))
                if v_type != CAR and v_type != SCOOTER:
                    print("\nInvalid vehicle type.")
            
            number = int(input("Enter vehicle number: "))

            if v_type == CAR or v_type == SCOOTER:
                row, col = get_free_row_col(v_type)

                if row != -1 and col != -1:
                    if v_type == CAR:
                        car[row][col] = add(v_type, number, row, col)
                    else:
                        scooter[row - 2][col] = add(v_type, number, row, col)
                else:
                    if v_type == CAR:
                        print("\nNo parking slot free to park a car")
                    else:
                        print("\nNo parking slot free to park a scooter")
            else:
                print("Invalid type")

        elif choice == 2:
            print(f"Total vehicles parked: {vehcount}")

        elif choice == 3:
            print(f"Total cars parked: {carcount}")

        elif choice == 4:
            print(f"Total scooters parked: {scootercount}")

        elif choice == 5:
            print("Display")
            display()

        elif choice == 6:
            print("Departure")
            v_type = 0

            while v_type != CAR and v_type != SCOOTER:
                v_type = int(input("Enter vehicle type (1 for Car / 2 for Scooter): "))
                if v_type != CAR and v_type != SCOOTER:
                    print("\nInvalid vehicle type.")
            
            number = int(input("Enter number: "))

            if v_type == CAR or v_type == SCOOTER:
                row, col = get_rc_by_info(v_type, number)
                if row != -1 and col != -1:
                    insert_record2(number, datetime.now())
                    get_arrival_time(number)
                    if v_type == CAR:
                        del car[row][col]
                        for i in range(col, 9):
                            car[row][i] = car[row][i + 1]
                        car[row][i] = None
                    else:
                        row = row - 2
                        if row >= 0:
                            del scooter[row][col]
                            for i in range(col, 9):
                                scooter[row][i] = scooter[row][i + 1]
                            scooter[row][i] = None
                else:
                    if v_type == CAR:
                        print("\nInvalid car number, or a car with such number has not been parked here.")
                    else:
                        print("\nInvalid scooter number, or a scooter with such number has not been parked here.")
            else:
                print("Invalid type")

        elif choice == 7:
            print("RECORD TABLES")
            print("Press 1 for Arrival history")
            print("Press 2 for Departure history")
            print("Press 3 for Fine Sheet")
            opt = int(input("Enter your choice: "))
            historyrec(opt)

        elif choice == 8:
            for row in range(2):
                for col in range(10):
                    if car[row][col] is not None:
                        del car[row][col]
                    if scooter[row][col] is not None:
                        del scooter[row][col]
            backup_write()
            break

if __name__ == "__main__":
    main()
