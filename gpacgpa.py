def calculate_cgpa(courses):
    total_credit_hours = 0
    total_quality_points = 0

    for course in courses:
        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'E': 0.0,
        }
        
        # Extract data from the course dictionary
        grade = course['grade']
        credit_hours = course['credit_hours']
        passed = course['passed']
        
        if passed:
            total_credit_hours += credit_hours
            total_quality_points += grade_points[grade] * credit_hours

    if total_credit_hours == 0:
        return 0.0

    cgpa = total_quality_points / total_credit_hours
    return cgpa

# Example usage:
courses = [
    {'grade': 'A', 'credit_hours': 3, 'passed': True},
    {'grade': 'B', 'credit_hours': 4, 'passed': True},
    {'grade': 'C', 'credit_hours': 2, 'passed': False},
    # Add more courses as needed
]

result_cgpa = calculate_cgpa(courses)
print(f"CGPA: {result_cgpa:.2f}")
