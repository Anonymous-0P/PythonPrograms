sentence = input("Enter a sentence: ")
(words, digits, upper, lower) = (0, 0, 0, 0)
l_w = sentence.split()
words = len(l_w)
for ch in sentence:
 if ch.isdigit():
 digits = digits + 1
 elif ch.isupper():
 upper = upper + 1
 elif ch.islower():
 lower = lower + 1
print ("No of Words: ", words)
print ("No of Digits: ", digits)
print ("No of Uppercase letters: ", upper)
print ("No of Lowercase letters: ", lower)
