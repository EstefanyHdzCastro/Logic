#Given two arrays, return array with only the common elements between them

def find_common_elements(arra1, array2):
  #Use set intersection to find common element
  common_elements = list(set(arra1)& set(array2))
  return common_elements

#Example
array1 = [1,2,3,4,5]
array2 = [3,4,5,6,7]

result = find_common_elements(array1,array2)
print(f"Common elements: {result}")