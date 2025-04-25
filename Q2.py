s = input("Enter a string: ")
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

i = 0
lowercase = ""
while i < len(s):
    found = False
    j = 0
    while j < len(upper):
        if s[i] == upper[j]:
            lowercase += lower[j]
            found = True
            break
        j += 1
    if not found:
        lowercase += s[i]
    i += 1
print("Lowercase:", lowercase)

i = 0
uppercase = ""
while i < len(s):
    found = False
    j = 0
    while j < len(lower):
        if s[i] == lower[j]:
            uppercase += upper[j]
            found = True
            break
        j += 1
    if not found:
        uppercase += s[i]
    i += 1
print("Uppercase:", uppercase)

i = 0
toggle = ""
while i < len(s):
    j = 0
    changed = False
    while j < len(lower):
        if s[i] == lower[j]:
            toggle += upper[j]
            changed = True
            break
        elif s[i] == upper[j]:
            toggle += lower[j]
            changed = True
            break
        j += 1
    if not changed:
        toggle += s[i]
    i += 1
print("Toggle Case:", toggle)
