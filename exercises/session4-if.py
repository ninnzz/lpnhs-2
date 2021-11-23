# lists

a = 1
b = 20

if a == 1 and b <= 10:      # True and False = False
    print("inside if")
else:
    print("nope")

greetings = "Magandang umaga!"

if greetings == "Magandang umaga!":
    print("Magandang umaga din!")
else:
    print("Magandang Hapon!")

angle = 180

if angle < 90:
    print("Acute")
elif angle == 90:
    print("Right")
else:
    print("Obtuse")


email = "nreclarin@gmail.com"


if email == "":
    print("No email included")
elif "@" not in email:
    print("Invalid email")
else:
    print("Valid email")


if "eclarin" in email:
    print("Its ninz's email")

