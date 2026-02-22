failed_attempts = []

with open("auth.log", "r") as file:
    for line in file:
        if "FAILED_LOGIN" in line:
            failed_attempts.append(line.strip())

print("Failed Login Attempts:")
for attempt in failed_attempts:
    print(attempt)