guestList = ["Stephen King", "Elon Musk", "Frank Ghery"]


print("Greetings " + guestList[0] + ",", guestList[1] + ", and", guestList[2] + ".")
print("I would like to invite you all to my dinner party.")

print("Update:", guestList[2], "couldn't make the party.")
guestList[2] = "Christopher Nolan"


print("I will be inviting", guestList[2], "in his place.")

print("Greetings " + guestList[0] + ",", guestList[1] + ", and", guestList[2] + ".")
print("I would like to invite you all to my dinner party.")

print("Good news everyone! I found a larger dinner table.\nTherefore I will be inviting three more guests.")

guestList.insert(0, "Barack Obama")
guestList.insert(3, "Albert Einstein")
guestList.append("Ken Levine")

print(guestList)

print("Greetings " + str(guestList) + ".")
print("I would like to invite you all to my dinner party.")

print("lol jk everyone. I can only invite two guests.")
guestList.pop()
guestList.pop()
guestList.pop()
guestList.pop()
print("The two guests that I will invite are" + str(guestList))
print("lol jk again. I am removing all of you.")
del guestList[0]
del guestList[0]
print(guestList)
