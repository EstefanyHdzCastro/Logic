#Given a word, look it up in a sentence and return how many times it appears in the sentence.
#The phrase and the word must be parameters of a function.

def count_word_ocurrence (setence, word):
  # Convert both the sentence and the word to lowercase for case-insensitive comparison
  setence_lower = setence.lower()
  word_lower = word.lower()

  # Split the sentence into words based on spaces
  occurrences = setence_lower.split().count(word_lower)

  return occurrences

#Example
setence = "This is a sample setence. The sample contains sample"
word_to_count = "sample"

result = count_word_ocurrence(setence, word_to_count)
print(f"The word '{word_to_count}' appears {result} times in the setence")