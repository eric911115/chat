
lines = [ ]
with open ('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line)
for s in lines:
	s = lines.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(s)