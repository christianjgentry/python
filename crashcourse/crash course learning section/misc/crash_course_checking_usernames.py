current_users = ["puppers123", "the real knuckles", "zgentry69", "mr. fister 69", "xXshadowbladeXx"]
new_users = ["puppers123", "xXshadowbladeXx", "cgentry74", "sotormer", "locshe"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("Sorry, the username", new_user, " is already taken. You will need to choose another username.")
	else:
		print("Congratulations! The username", new_user, "is available.")
