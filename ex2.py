fName = "Erik"
lName = "Anderson"

print(f'{fName} {lName}')

fullName = [fName, lName]
print(f'{fullName}')

fullName = {"First": fName, "Last": lName}
for v in fullName.items():
    print(v)
print(fullName["First"],fullName["Last"])
