s = input()
om = 0
cm = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cm += 1
    else:
        cm = 1
    om = max(cm, om)
return om