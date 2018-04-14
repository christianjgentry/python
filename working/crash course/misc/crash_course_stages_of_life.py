age = 90
lifeStage = ""

if age < 2:
	lifeStage = "baby"
if age > 2 and age < 5:
	lifeStage = "toddler"
if age >= 5 and age < 13:
	lifeStage = "child"
if age >= 13 and age < 18:
	lifeStage = "teenager"
if age >= 18 and age < 65:
	lifeStage = "adult"
if age >= 65 and age < 100:
	lifeStage = "senior"
	
print("This person is a", lifeStage)
