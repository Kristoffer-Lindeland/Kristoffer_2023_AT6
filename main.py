class DataValidation:
   def __init__(self):
       self.valid_positive_integers = []
   def validate_inputs(self, input_list):
       for input_str in input_list:
           # Check if the string is a valid digit
           if input_str.isdigit():
               # Convert the string to an integer
               integer_value = int(input_str)
               # Check if the integer is a positive integer
               if integer_value > 0:
                   # If it's a positive integer, add it to the valid_positive_integers list
                   self.valid_positive_integers.append(integer_value)


   # Method to print the list
   def get_valid_positive_integers(self):
       return self.valid_positive_integers


# Test list
input_list = ["78", "ABC", "4", "123", "-5", "678", "@@@", "D543"]


validator = DataValidation()
validator.validate_inputs(input_list)
valid_integers = validator.get_valid_positive_integers()
print(valid_integers)


