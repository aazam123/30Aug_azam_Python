#Write a Python script to check if a given key already exists in a dictionary
def key_in_dict(d, key):
  return (key in d) 
students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print(key_in_dict(students, 'Roxanne'))
print(key_in_dict(students, 'Gina'))