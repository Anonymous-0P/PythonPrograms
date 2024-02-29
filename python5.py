import re
def find_phone_numbers_and_emails(filename):
 # Read the contents of the file
 with open(filename, 'r') as file:
 text = file.read()
 # Find all phone numbers in the text
 phone_numbers = re.findall(r'\+\d{11}', text)
 # Find all email addresses in the text
 email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[AZ|a-z]{2,}\b', text)
 # Return the results
 return phone_numbers, email_addresses
# Test the function with a sample text file
filename = 'Files.txt'
phone_numbers, email_addresses = find_phone_numbers_and_emails(filename)
# Print the results
print('Phone numbers:')
for number in phone_numbers:
 print(number)
print('\nEmail addresses:')
for email in email_addresses:
 print(email)