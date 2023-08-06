num_staff = 50

for i in range(1, num_staff+1):
    basic_salary = float(input(f"Enter basic salary for staff {i}: "))
    years_of_service = 0

    if i % 10 == 0:
        years_of_service = int(input(f"Enter years of service for staff {i}: "))

    transport_allowance = 0.1 * basic_salary
    housing_allowance = 0.155 * basic_salary
    meal_subsidy = 500
    long_service_allowance = 0.02 * basic_salary if years_of_service >= 10 else 0

    total_pay = basic_salary + transport_allowance + housing_allowance + meal_subsidy + long_service_allowance

    print(f"\nPay Slip for Staff {i}:")
    print(f"Basic Salary:\t\t\t\t{basic_salary:.2f}")
    print(f"Transport Allowance (10%):\t\t{transport_allowance:.2f}")
    print(f"Housing Allowance (15.5%):\t\t{housing_allowance:.2f}")
    print(f"Meal Subsidy:\t\t\t\t{meal_subsidy:.2f}")
    print(f"Long Service Allowance:\t\t{long_service_allowance:.2f}")
    print(f"Total Pay:\t\t\t\t{total_pay:.2f}")
