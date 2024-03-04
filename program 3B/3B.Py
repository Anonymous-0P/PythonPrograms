def similarity(str1, str2):
 len1 = len(str1)
 len2 = len(str2)
 max_len = max(len1, len2)
 common_chars = 0
 for i in range(max_len):
 if i < len1 and i < len2 and str1[i] == str2[i]:
 common_chars += 1
 return common_chars / max_len
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("Original string1:\n", str1)
print("Second string:\n",str2)
print("Similarity between two said strings:")
print(similarity(str1, str2))