# Surname

# Use the list provided for the next 6 questions

bank = {
    "name": "BPI",
    "client_count": 0,
    "secret_key": "this_should_not_be_included",
    "client": [
        {
          "id": "7d1c69a0-862e-428f-89ba-e075572d4f4c",
          "first_name": "Lorry",
          "last_name": "Ettels",
          "country": "Senegal",
          "city": "Ndibène Dahra",
          "gender": "Male",
          "savings": "$9.65"
        }, {
          "id": "78d4bf14-dfd5-4e21-a4e4-a82e0fc7ac4f",
          "first_name": "Al",
          "last_name": "Skentelbury",
          "country": "Philippines",
          "city": "Ibaan",
          "gender": "Male",
          "savings": "$5.81"
        }, {
          "id": "72fe7d7a-fc61-4f3f-8285-9ff9fdcdcfb9",
          "first_name": "Cilka",
          "last_name": "Rulton",
          "country": "Indonesia",
          "city": "Kotadukuh",
          "gender": "Female",
          "savings": "$9.77"
        }, {
          "id": "22ee487d-5218-4bbb-94b6-7d4e1cbf4cd2",
          "first_name": "Dudley",
          "last_name": "Baily",
          "country": "Thailand",
          "city": "Phuket",
          "gender": "Male",
          "savings": "$5.69"
        }, {
          "id": "89ad0706-d1d9-4a9a-b509-68d7abd16d35",
          "first_name": "Christi",
          "last_name": "Roizin",
          "country": "Georgia",
          "city": "Akhaldaba",
          "gender": "Female",
          "savings": "$3.08"
        }
    ]
}

# Add a new client using the following info
# id - daa0e754-7293-4f7f-bebe-8f3619e445e3
# your name
# Philippines
# Tayabas
# your gender
# your bank savings
print("Question 1:")

print(bank["client"])

# Print the savings of Cilka Rulton
print("Question 2:")

print(f"Her savings is: ")

# Change the savings of Lorry Ettels to $1500, then print her new savings
print("Question 3:")

print(f"Her savings is: ")

# Print all the keys in the dictionary
# There is a dictionary property to get all the keys and convert it to a list
print("Question 4:")

print(f"Keys: ")

# Delete the key "secret_key" from the dictionary and print all the keys similar to what you did 
# in Question 4
print("Question 5:")

print(f"Keys: ")

# Change the value of "client_count" to reflect how many clients are actually in the client list
print("Question 6:")

print(f"Total client count is:")


# Use the dictionaries below for the next questions

section1 = { 
    "gt": {
        "teacher": "Georgia Talabong",
        "school_year": 2008,
        "students": [ 
            {
                "name": "Ninz",
                "marks":{ 
                    "physics":100,
                    "english": 100,
                    "history":100,
                    "math": 100,
                    "mapeh": 60,
                    "values_ed": 60
                }
            }
        ]
    }
}

section2 = { 
    "mc": {
        "teacher": "Marietta Cabuyao",
        "school_year": 2005,
        "students": [ 
            {
                "name": "Ninz",
                "marks":{ 
                    "general_science":100,
                    "english": 100,
                    "philippine_history":100,
                    "math": 100,
                    "mapeh": 60,
                    "values_ed": 60
                }
            }
        ]
    }
}

# Create a new dictionary called "section3". 
# It should contain atleast 5 students and atleast 5 subjects
print("Question 7:")
section3 = {} # change this


# Combine section1, section2 and section3 into one dictionary called "sections"
# Search on how to merge dictionaries in python
print("Question 8:")
section = {} # Change this

print(section)

# Print all the teachers of the three sections using the "section" variable
print("Question 9:")
print(f"Teachers: ")


# Remove all items in the dictionary "section"
print("Question 10:")

print(section) # This should return "{}" an empty dictionary
