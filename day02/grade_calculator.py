def main():
    while True:
        # Ask for the student's name
        name = input("\nEnter student's name (or type 'Exit' to quit): ")
        if name.strip().lower() == 'exit':
            print("Exiting the program.")
            break

        # Ask for 3 subject marks
        try:
            mark1 = float(input("Enter mark for subject 1: "))
            mark2 = float(input("Enter mark for subject 2: "))
            mark3 = float(input("Enter mark for subject 3: "))
        except ValueError:
            print("Invalid input! Please enter numerical values for the marks.")
            continue

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        # Determine the grade
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        # Display the results
        print("\n------------------------------")
        print(f"Name : {name.capitalize()}")
        print(f"Average: {average:.1f}")
        print(f"Grade : {grade}")
        print("------------------------------")


if __name__ == "__main__":
    main()
