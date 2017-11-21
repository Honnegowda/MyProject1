def get_even_generator():
    n = 2
    while True:
	yield n
	n = n+2

even_gen = get_even_generator()

#print even_gen
for i in range(1, 11):
    print even_gen.next()

