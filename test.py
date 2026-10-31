with open("tasks.txt","w") as f:
    for task in ["buy milk","study"]:
        f.write(task + "\n")


# reading
with open("tasks.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
print(lines)