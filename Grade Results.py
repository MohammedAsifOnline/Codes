searchbar = input("Enter Marks: ")
Marks = int(searchbar)

if Marks >= 101:
    print("Invalid Marks")
elif Marks >= 90:
    print("Grade A")
elif Marks >= 80:
    print("Grade B")
elif Marks >= 70:
    print("Grade C")
elif Marks >= 60:
    print("Grade D")
else:
    print("Fail")