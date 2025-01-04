
# Dictionaries containing information
rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Function to display details
def display_course_details(course_number):
    if course_number in rooms:
        print(f"Room Number: {rooms[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {times[course_number]}")
    else:
        print("Course number not found. Please check your input.")

# program execution
if __name__ == "__main__":
    course_input = input("Enter a course number (e.g., CSC101): ")
    display_course_details(course_input)
