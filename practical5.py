import random

def generate_password(dictionary_file, length):
  """Generates a password using a random combination of words from the given list.

  Args:
    dictionary_file: A list of words to choose from.
    length: The desired length of the password in words.

  Returns:
    A string representing the generated password.
  """

  password = []
  for _ in range(length):
    password.append(random.choice(dictionary_file))

  return ' '.join(password)

# Read words from a text file
with open('dictionary_file.txt', 'r') as f:
  dictionary_file = f.read().splitlines()

# Generate a password
password = generate_password(dictionary_file, length=int(input('Enter the number of character you want: ')))
print(password)