cijfers = []
invoer = 0

while invoer != -1:
    invoer = int(input("Geef een getal: "))
    if invoer != -1:
        gevonden = False
        for check in cijfers:
            if check == invoer:
                gevonden = True

        if not gevonden:
            cijfers.append(invoer)

print(cijfers)

cijfers.sort()
print(cijfers[-2])
print(cijfers[len(cijfers)-2])