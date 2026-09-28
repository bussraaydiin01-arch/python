# Task 1. Write a Python program to get a list, sorted in increasing order by the last element in
# each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sorted(my_list, key=lambda x: x[-1])
print(result)

# Task 2. Given a string s1, write a program to return the sum and average of the digits that
# appear in the string, ignoring all other characters.

s1 = "Python 3.14 is fun!"
digits = [int(char) for char in s1 if char.isdigit()]
total = sum(digits)
average = total / len(digits)
print("Sum:", total)
print("Average:", average)


# Task 3. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries : [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi
# Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue’}]
# Sorting the List of dictionaries : [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make':
# 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

my_list = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
result = sorted(my_list, key=lambda x: int(x['model']))
print(result)


# Task 4. Write a Python program to convert a given list of strings into list of lists using map
# function.

my_list = ["hello", "world", "python"]
result = list(map(list, my_list))
print(result)


# Task 5. Create a dictionary with the events in Dortmund and the date of the event. List all
# events that were running during the Night of Museums in Dortmund on 19th September 2026.

events = {
    "Museumsrallye durch den Adlerturm": "19.09.2026",
    "Mit VR die Museen der Welt entdecken": "19.09.2026",
    "Polizeiausstellung 110": "19.09.2026",
    "Connected – Digitale Kultur im Ruhrgebiet": "19.09.2026",
    "Stille im Zero Raum": "19.09.2026",
    "Die DEW21 Museumsnacht tanzt": "19.09.2026",
    "Nachts im Museum": "19.09.2026",
    "Erkennt ihr euer Dortmunder?": "19.09.2026",
    "DEW21 Museumsnacht": "19.09.2026",
    "Museumsnacht im Dortmunder Kunstverein": "19.09.2026"
}

date = "19.09.2026"

print("Events on", date, ":")

for event, event_date in events.items():
    if event_date == date:
        print(event)