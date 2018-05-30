usernames = ["admin", "cgentry74", "dark vestige", "christianjgentry",
"zimzizeroo"]

for username in usernames:
	if username == "admin":
		print("Hello", username + ", would you like to see a status report?")
	if username != "admin":
		print("Hello", username + "! Welcome back!")

if not usernames:
	print("We need to find some users!")


