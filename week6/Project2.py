
# Lists to store results
admitted = []
not_admitted = []

# Function to check admission
def check_admission(name, department, jamb_score, credits, passed_interview):
    eligible = False

    if department.lower() == "computer science":
        if jamb_score >= 250 and credits >= 5 and passed_interview:
            eligible = True
    elif department.lower() == "mass communication":
        if jamb_score >= 230 and credits >= 5 and passed_interview:
            eligible = True

    candidate_info = {
        "Name": name,
        "Department": department,
        "JAMB Score": jamb_score,
        "Credits": credits,
        "Interview Passed": passed_interview
    }

    if eligible:
        admitted.append(candidate_info)
        print(f"{name} has been ADMITTED into {department}.")
    else:
        not_admitted.append(candidate_info)
        print(f"{name} has NOT been admitted into {department}.")

# Example usage:
check_admission("Alice", "Computer Science", 255, 6, True)
check_admission("Bob", "Mass Communication", 225, 5, True)
check_admission("Chioma", "Mass Communication", 235, 5, False)
check_admission("David", "Computer Science", 260, 5, True)

# Optional: Print full results
print("\nAdmitted Candidates:")
for candidate in admitted:
    print(candidate)

print("\nNot Admitted Candidates:")
for candidate in not_admitted:
    print(candidate)
