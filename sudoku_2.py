import time
start_time = time.time()
#declaration 
n = 9
m = 3
ans = True
a = [[0 for i in range (9)] for i in range(9)]
c = [[-1 for i in range (9)] for i in range(9)]
sol = [[[0 for i in range (9)] for i in range(9)]for i in range (9)]
puzz = open("puzzle.txt","r")
for i in range(9):
	s = puzz.read(10)
	for j in range(9):
		a[i][j] = int(s[j])
puzz.close()
b = tuple(tuple(a[i]) for i in range(n))
#end

#display function
#display problem
def disp():
	for i in range(9):
		print a[i]
#display ans		
def disp_sol():
	for i in range (9):
		for j in range (9):
			print "[",
			k = 0
			while(sol[i][j][k] != 0):	
				print sol[i][j][k],
				k = k + 1
			print "]",		
		print	
#display function end


#constraints func
def constraint(x,y):
	#scanning row
	for i in range (9):
		if(a[x][i] != 0):
			continue
		for j in range (9):
			if(sol[x][i][j] == a[x][y]):
				sol[x][i][j] = 0
				break
	
	#scanning column
	for i in range (9):
		if(a[i][y] != 0):
			continue
		for j in range (9):
			if(sol[i][y][j] == a[x][y]):
				sol[i][y][j] = 0
				break
	
	#scanning block
	for i in range(m*(x//m),(m*(x//m))+m):
		for j in range(m*(y//m),(m*(y//m))+m):
			if (a[i][j] != 0):
				continue
			for k in range(9):
				if(sol[i][j][k] == a[x][y]):
					sol[i][j][k] = 0
					break	
										
#func end
	
#initialize			
for i in range (9):
	for j in range (9):
		if(a[i][j] != 0):
			sol[i][j][0] = a[i][j]
		else:
			for k in range(9):
				sol[i][j][k] = k + 1
#init end

#adding constraints				
for i in range (9):
	for j in range (9):
		if(a[i][j] == 0):
			continue
		else:
			constraint(i,j)							
#end

#extraa
for i in range (9):
	for j in range (9):
		sol[i][j].sort()
		sol[i][j].reverse()
#extraa end

#solution
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
	
def solve(i,j):
	if j >= n:
		i = i+1
		j = 0
	if i == n:
		return True		
	while b[i][j]!=0:
		j = j + 1
		if j >= n:
			i = i+1
			j = 0
		if i == n:
			return True		
	c[i][j] += 1	
	q = c[i][j]
	a[i][j] = sol[i][j][q]
	if a[i][j] == 0:
		c[i][j] = -1
		return False
	while not(is_safe(i,j)):
		c[i][j] += 1	
		q = c[i][j]
		a[i][j] = sol[i][j][q]
		if a[i][j] == 0:
			c[i][j] = -1
			return False
	ans = solve(i,j+1)
	if ans:
		return True
	else:
		ans = solve(i,j)
		return ans
#solution end
ch = solve(0,0)
disp()
print(time.time() - start_time)
