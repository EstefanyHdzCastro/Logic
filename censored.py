#Given a text and a search, censor all matches of the search in the text with [-Censored-].
#If the text or search is empty show "Cannot read text and search" in case both parameters are not reached. 

def censor_text(text,  search):
  if not text or not search:
    return "Cannot read text an search"

  censored_text = text.replace(search, "[-Censored-]")
  return censored_text

#Example
original_text = "This is a sample text. The sample contains the word 'example' multiple times."
search_term = "example"

result = censor_text(original_text, search_term)
print(result)