def bintodecima(b_num):
 value = 0
 for i in range(len(b_num)):
 digit = b_num.pop()
 if digit == '1':
 value = value + pow(2, i)
 return value
b_num = list(input("Input a binary number: "))
value = bintodecima(b_num)
print("The decimal value of the number is", value)
# Octal to Hexadecimal using List and while Loop
print("\n Enter the Octal Number: ")
octnum = int(input())
chk = 0
i = 0
decnum = 0
while octnum!=0:
 rem = octnum%10
 if rem>7:
 chk = 1
 break
 decnum = decnum + (rem * (8 ** i))
 i = i+1
 octnum = int(octnum/10)
if chk == 0:
 i = 0
 hexdecnum = []
while decnum != 0:
 rem = decnum % 16
 if rem < 10:
 rem = rem + 48
 else:
 rem = rem + 55
 rem = chr(rem)
 hexdecnum.insert(i, rem)
 i = i + 1
 decnum = int(decnum / 16)
 print("Equivalent Hexadecimal Value is: ")
 i = i - 1
 while i >= 0:
 print(end=hexdecnum[i])
 i = i - 1
 print()
else:
 print("\n Invalid Input!")
