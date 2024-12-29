def calculate_bmi(height, weight):
    """Calculates Body Mass Index (BMI)."""
    height_m = height / 100  # Convert height from cm to meters
    bmi = weight / (height_m * height_m)
    return bmi

# Get user input
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = calculate_bmi(height, weight)

# Print BMI
print(f"Your BMI is: {bmi:.2f}")

# Interpret BMI (you can add more detailed categories)
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a healthy weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")