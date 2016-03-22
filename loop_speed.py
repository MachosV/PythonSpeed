import time,string,random

def do_test(lst):
	best_time=99
	for x in xrange(0,100):
		start=time.clock()
		lst1=map(str.upper,lst)
		end=time.clock()-start
		if best_time>end:
			best_time=end
	print "map method    {:.4f}".format(best_time)

def do_test_improved(lst):
	best_time=99
	for x in xrange(0,100):
		start=time.clock()
		lst1=[]
		for i in lst:
			lst1.append(i.upper())
		end=time.clock()-start
		if best_time>end:
			best_time=end
	print "simple method {:.4f}".format(best_time)
	
def do_test_lists(lst):
	best_time=99
	for x in xrange(0,100):
		start=time.clock()
		lst1=[s.upper() for s in lst]
		end=time.clock()-start
		if best_time>end:
			best_time=end
	print "list method   {:.4f}".format(best_time)
	
def do_test_iter(lst):
	best_time=99
	for x in xrange(0,100):
		start=time.clock()
		lst1=(s.upper() for s in lst)
		end=time.clock()-start
		if best_time>end:
			best_time=end
	print "iter method   {:.8f}".format(best_time)

def main():
	a=string.ascii_lowercase
	lst=[]
	for i in range(0,100000):
		lst.append(random.choice(a))
	do_test(lst)
	do_test_improved(lst)
	do_test_lists(lst)
	do_test_iter(lst)
	return 0

if __name__ == '__main__':
	main()

