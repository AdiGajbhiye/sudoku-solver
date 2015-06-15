import time
start_time = time.time()
#declaration
n = 9
m = 3
aans = True
a = [[0 for i in range(n)] for i in range(n)]
puzz = open("puzzle.txt","r")
for i in range(n):
	s = puzz.read(n+1)
	for j in range(n):
		a[i][j] = int(s[j])
puzz.close()
b = tuple(tuple(a[i]) for i in range(n))
#declrn end

#display
def print_():
	for i in range(n):
		print a[i]
#display end

#constraint
def is_safe(i,j):
	for x in range(n):
		if x != i and a[x][j] == a[i][j] and a[i][j] != 0:
			return False

	for x in range(n):
		if x != j and a[i][x] == a[i][j] and a[i][j] != 0:
			return False

	for x in range(m*(i//m),(m*(i//m))+m):
		for y in range(m*(j//m),(m*(j//m))+m):
			if x != i and y != j and a[i][j] == a[x][y] and a[i][j] != 0:
				return False
	return True
#constrnt end

#solve function
def sol(i,j):
	if j >= n:
		i = i+1
		j = 0
	if i == n:
		return True
	while b[i][j]!=0:
		j += 1
		if j >= n:
			i = i+1
			j = 0
		if i == n:
			return True
	a[i][j] += 1
	if a[i][j] > n:
		a[i][j] = 0
		return False
	while not(is_safe(i,j)):
		a[i][j] += 1
		if a[i][j] > n:
			a[i][j] = 0
			return False
	aans = sol(i,j+1)
	if aans:
		return True
	else:
		aans = sol(i,j)
		return aans
#solve end

#main
aans = sol(0,0)
print_()
#main end
print(time.time() - start_time)
