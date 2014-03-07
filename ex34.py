animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
numbers = [1, 2, 3, 4, 5, 6]
for i,j in zip (animals, numbers):
	print "The %d st animal is at %d and it is a %s. " % (j, j, i)
