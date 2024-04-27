print("We're going to make multiple math problems from TWO values you give me!")
first_value = int(input("What's your first value? "))
second_value = int(input("And the second? "))
addition = first_value + second_value
subtraction = first_value - second_value
multiplication = first_value * second_value
division = first_value / second_value

print(f'''
Below are the following problems:

      Addition: {first_value} + {second_value} = {addition}
      Subtraction: {first_value} - {second_value} = {subtraction}
      Multiplication: {first_value} * {second_value} = {multiplication}
      Division: {first_value} / {second_value} = {division}
'''
)