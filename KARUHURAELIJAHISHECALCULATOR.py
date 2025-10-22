#HEADING
print("=" * 10)
print("PYTHON TAKE HOME ASSIGNMENT, DONE BY KARUHURA ELIJAH ISHE")
print("=" * 30)

print("\n--- TASK 1: Variables for name, age, GPA ---")
print("\n let's talk about variables")

# CREATING VARIABLES
name = "Karuhura Elijah Ishe"
age = 23
gpa = 3.8
year =3.1

# DISPLAYING THE VARIABLES AND KNOWING THEIR TYPES
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"year:{year}")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of gpa: {type(gpa)}")
print(f"Type of year: {type(year)}")

#  CONVERTING between int, float, str

print("\n TYPE CONNVERSIONS")

# Starting values
number_int = 42
number_float = 3.14
number_str = "100"

print(f"\nOriginal values:")
print(f"number_int = {number_int} (type: {type(number_int)})")
print(f"number_float = {number_float} (type: {type(number_float)})")
print(f"number_str = {number_str} (type: {type(number_str)})")

# Convert int to float
int_to_float = float(number_int)
print(f"\nInt to Float: {number_int} = {int_to_float} (type: {type(int_to_float)})")
#convert float to int
float_to_int =int(number_float)
print(f"\nfloat_to_int: {number_float} ={float_to_int} (type:{type(float_to_int)}) ")
#convert int to string
int_to_str =str(number_int)
print(f"\nint_to_str:{number_int}={int_to_str} (type:{type(int_to_str)}) ")
print(f"\nUse the same procedures for the other conversions")


print("\n **PERFORMING MATHS OPERATIONS**")
num1 = 15
num2 = 4
print(f"\nNumbers: num1 = {num1}, num2 = {num2}")
print(f"\nArithmetic Operations:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus (Remainder): {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")
num3 =41
print(f"addition once i add the third number  :{num1}+{num2}+{num3} ={num1 +num2 +num3}")
print(f"mltiplication once i add the third number  :{num1}*{num2}*{num3} ={num1 *num2 *+num3}")

# More complex operations
print(f"\nComplex Math Operations:")
a = 10
b = 3
c = 2

result1 = (a + b) * c
result2 = a ** b - c
result3 = (a / b) + c

print(f"({a} + {b}) * {c} = {result1}")
print(f"{a} ** {b} - {c} = {result2}")
print(f"({a} / {b}) + {c} = {result3:.2f}")

#SLICING AND MODIFYING STRINGS
print("\nString Slicing and Modification ")

# Original string
text = "computer science"
print(f"\nOriginal string: '{text}'")

# String slicing
print(f"\nString Slicing:")
print(f"First character: text[0] = '{text[0]}'")
print(f"Last character: text[-1] = '{text[-1]}'")
print(f"First 6 characters: text[0:6] = '{text[0:6]}'")
print(f"Characters 7 to end: text[7:] = '{text[7:]}'")
print(f"Last 11 characters: text[-11:] = '{text[-11:]}'")
print(f"Every 2nd character: text[::2] = '{text[::2]}'")
print(f"Reverse string: text[::-1] = '{text[::-1]}'")



# String modification methods
print(f"\nString Modification:")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Title Case: '{text.title()}'")
print(f"Replace 'computer science' with 'information Technology': '{text.replace('Python', 'Java')}'")
print(f"Split into words: {text.split()}")

# More string operations
student_name = "  KARUHURA ELIJAH ISHE "
print(f"\nStudent name: '{student_name}'")
print(f"Strip whitespace: '{student_name.strip()}'")
print(f"Strip and title case: '{student_name.strip().title()}'")
print(f"Strip and upper case: '{student_name.strip().upper()}'")
print(f"Strip and lower case: '{student_name.strip().lower()}'")
print(f"Length: {len(student_name.strip())}")



# String concatenation
first_name = "Karuhura"
last_name = "Elijah Ishe"
full_name = first_name + " " + last_name
print(f"\nConcatenation: {first_name} + {last_name} = '{full_name}'")

# Build a simple calculator
print("\nA simple calculator")

def calculator():
    
   
    print("  SIMPLE CALCULATOR")

    
    print("\nOperations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Modulus (%)")
    print("7. Exponentiation ()")
    
    try:
        # Get user input
        choice = input("\nChoose operation (1-7): ")
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on choice
        if choice == "1":
            result = num1 + num2
            operation = "+"
            print(f"\n{num1} {operation} {num2} = {result}")
        
        elif choice == "2":
            result = num1 - num2
            operation = "-"
            print(f"\n{num1} {operation} {num2} = {result}")
        
        elif choice == "3":
            result = num1 * num2
            operation = "*"
            print(f"\n{num1} {operation} {num2} = {result}")
        
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                operation = "/"
                print(f"\n{num1} {operation} {num2} = {result}")
            else:
                print("\nError: Cannot divide by zero!")
        
        elif choice == "5":
            if num2 != 0:
                result = num1 // num2
                operation = "//"
                print(f"\n{num1} {operation} {num2} = {result}")
            else:
                print("\nError: Cannot divide by zero!")
        
        elif choice == "6":
            if num2 != 0:
                result = num1 % num2
                operation = "%"
                print(f"\n{num1} {operation} {num2} = {result}")
            else:
                print("\nError: Cannot divide by zero!")
        
        elif choice == "7":
            result = num1 ** num2
            operation = ""
            print(f"\n{num1} {operation} {num2} = {result}")
        
        else:
            print("\nInvalid choice! Please select 1-7.")
    
    except ValueError:
        print("\nError: Please enter valid numbers!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Run the calculator
# Uncomment the line below to run the interactive calculator
# calculator()

# Demo calculator with predefined values
print("\n--- Calculator Demo (with predefined values) ---")
demo_num1 = 20
demo_num2 = 5

print(f"\nDemo Numbers: {demo_num1} and {demo_num2}")
print(f"Addition: {demo_num1} + {demo_num2} = {demo_num1 + demo_num2}")
print(f"Subtraction: {demo_num1} - {demo_num2} = {demo_num1 - demo_num2}")
print(f"Multiplication: {demo_num1} * {demo_num2} = {demo_num1 * demo_num2}")
print(f"Division: {demo_num1} / {demo_num2} = {demo_num1 / demo_num2}")
print(f"Floor Division: {demo_num1} // {demo_num2} = {demo_num1 // demo_num2}")
print(f"Modulus: {demo_num1} % {demo_num2} = {demo_num1 % demo_num2}")
print(f"Exponentiation: {demo_num1} ** {demo_num2} = {demo_num1 ** demo_num2}")
