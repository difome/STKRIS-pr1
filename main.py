def main() -> None:
    name: str = input("Enter student name: ")
    
    grades: list[float] = [
        float(input(f"Enter grade for subject {i} (0-100): "))
        for i in range(1, 4)
    ]
    
    average: float = sum(grades) / len(grades)
    print(f"Student {name} has an average grade of {average:.2f}")

if __name__ == "__main__":
    main()
