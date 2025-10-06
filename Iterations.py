def inputValid(text):
  if text == "":
    return "empty", None

  hasLetter = False
  for char in text:
    if char.isalpha():
      hasLetter = True
      break

  if hasLetter:
    return "ok", text
  else:
    return "no letters", None

def letterFreq(text):
  letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  freq = [0] * 26
  text = text.upper()

  for char in text:
    if char.isalpha():
      for i in range(26):
        if char == letters[i]:
          freq[i] += 1
          break
  return freq

def printResults(freq, text):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  print(f"\nYou entered: {text}")
  print("Letter Frequency Analysis:")
  for i in range(26):
    if freq[i] > 0:
      print(f"{letters[i]} : {freq[i]}")

def main():
  text = input("Enter a sentence: ")
  status, text = inputValid(text)

  if status == "ok":
    freq = letterFreq(text)
    printResults(freq, text)
  elif status == "empty":
    print("Error: The input string is empty.")
  elif status == "no letters":
    print("Error: The input string contains no letters.")

while True:
  main()