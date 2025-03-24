import re 
#Display welcome message
print("----------Password Complexity Checker----------")

def check_password_complexity(password):
    #Define a standard 
    length_standard = len(password) >= 8
    uppercase_standard = bool(re.search(r'[A-Z]', password))
    lowercase_standard = bool(re.search(r'[a-z]', password))
    number_standard = bool(re.search(r'[0-9]', password))
    specialchar_standard = bool(re.search(r'[!@#$%^&*?,.|{}]', password))
    
    #calculate password strength
    password_strength = sum([length_standard, uppercase_standard, lowercase_standard, number_standard, specialchar_standard])
    
    #Provide report
    report = []
    if not length_standard:
        report.append("Password should be atleast 8 characters long.")
    if not uppercase_standard:
        report.append("Password should contain atleast one uppercase letter.")
    if not lowercase_standard:
        report.append("Password should contain atleast one lowercase letter.")
    if not number_standard:
        report.append("Password should contain atleast one number.")
    if not specialchar_standard:
        report.append("Password should contain atleast one special character.")

    #Determine the Strength
    if password_strength == 5:
        strength = "Strong."
    elif password_strength == 3:
        strength = "Medium."
    else:
        strength = "Weak."

    return strength, report

def main():
    password = input("Enter a password to check its strength: ")

    #Check Password Strength
    strength, report = check_password_complexity(password)

    #Display result
    print(f"\nPassword Strength: {strength}")
    if report:
        print("Feedback:")
        for message in report:
            print(f"-{message}")  

main()