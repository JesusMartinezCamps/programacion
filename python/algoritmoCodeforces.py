import math

input = 4

k = 1

level = input + 1

x = 2

presses = 0

while k < level and presses < 1e18:

	presses = presses + 1
	x = x + k

	if x == math.sqrt(x) * math.sqrt(x) and math.sqrt(x) % (k+1) == 0:
		
		x = math.sqrt(x)
		k = k + 1

		print(presses)
		presses = 0

	else:
		pass
