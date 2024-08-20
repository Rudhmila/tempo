print("Enter Your Mobile No: ")
no = input("+88")

operator = "GP" if no [2] == '7' or no[2] == '3' else 'Robi' if no[2] == "8" else 'Banglalink' if no[2] == '9' else 'Teletalk' if no[2]=='5' else 'Airtel' if[2] == '6' else 'invalid operator'

print(operator)