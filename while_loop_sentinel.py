total_sum = 0
while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    try:
        number = float(user_input)  # Convert input to a number
        total_sum += number  # Add the number to the total sum
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        
print("The total sum is:", total_sum)
