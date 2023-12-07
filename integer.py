#Given an integer, invert it and return the integer again.

def invert_integer(number):
  #Convert the integer to a srtrin, reverse it, and convert it back to an integer
  inverted_number = int(str(number)[::-1])
  return inverted_number

#Example:
original_number = 1234
inverted_result = invert_integer(original_number)

print(f"Original number: {original_number}")
print(f"Inverted number: {inverted_result}")