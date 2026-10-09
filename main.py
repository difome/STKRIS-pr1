def get_valid_grade(prompt: str) -> float:
    while True:
        try:
            grade: float = float(input(prompt))
            if 0.0 <= grade <= 100.0:
                return grade
            print("Error: Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_ects_grade(average: float) -> str:
    match average:
        case _ if average >= 90:
            return 'A'
        case _ if average >= 82:
            return 'B'
        case _ if average >= 74:
            return 'C'
        case _ if average >= 64:
            return 'D'
        case _ if average >= 60:
            return 'E'
        case _:
            return 'F'

def main() -> None:
    name: str = input("Enter student name: ")
    
    grades: list[float] = [
        get_valid_grade(f"Enter grade for subject {i} (0-100): ")
        for i in range(1, 4)
    ]
    
    average: float = sum(grades) / len(grades)
    ects: str = get_ects_grade(average)
    
    print(f"\nStudent {name} has an average grade of {average:.2f}")
    print(f"ECTS Grade: {ects}")

if __name__ == "__main__":
    main()
