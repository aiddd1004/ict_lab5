def calculate_average(grades):
    if not grades: 
        return 0.0
    return sum(grades) / len(grades)

def main():
    grades = []

    for i in range(5):
        grade = float(input(f"Enter grade for student {i + 1}: "))
        grades.append(grade)
    
    
    average_grade = calculate_average(grades)
    print(f"Group average grade: {average_grade}")

 
if __name__ == "__main__":
    main()
