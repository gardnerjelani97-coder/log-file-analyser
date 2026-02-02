with open("auth.log", "r") as file:
    logs = file.readlines()

for line in logs:
    print(line.strip())
