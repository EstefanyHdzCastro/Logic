#Given a text string, flip it around and invert the order of its characters, without using language methods, only control structures.

def reverse_string(input_string):
  reversed_string = ""
  for char in input_string:
    reversed_string = char + reversed_string

  return reversed_string

#Exaple
original_string = "Hello, World!"
flipped_string = reverse_string(original_string)

print(f"Original string: {original_string}")
print(f"Flipped string: {flipped_string}")