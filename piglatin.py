sentence = input("Enter a sentence to be converted into pig latin: ")
vowels = ["a", "e", "i", "o", "u"]
words =sentence.split()

for i in range(len(words)):
  # check if the first letter is a vowel
  if words[i][0] in vowels:
    # if the first letter is a vowel, add "ay" at the end
    words[i] = words[i] + "ay"
  else:
    # if first letter is a consonant, move it to the end and add "ay"
    words[i] = words[i][1:] + words[i][0] + "ay"
# combine the words into a sentence
pig_latin_sentence = " ".join(words)
# print the pig latin sentence
print(pig_latin_sentence)
