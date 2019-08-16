
import sys

def smallest_prime_factor(n, lower=1):
	if n<2:
		raise ValueError('no smallest prime factor exist for '+str(n))
	while lower<2 or n%lower:
		lower+=1
	return lower


def prime_power_decomp(n,fmt = False):
	ppows = []
	m =n

	p =1
	while n>1:
		p = smallest_prime_factor(n,p+1)
		e = 0
		while not n%p:
			n/=p
			e+=1
		ppows.append((p,e))

	if not fmt:
		return ppows
	return fmt_decomp(m,ppows)


def fmt_decomp(n,dec):
	s = '%d = '%n
	if not dec:
		s+= '1'
		return s
	for p,e in dec:
		s+= '%d^%d * '%(p,e)

	return s[:-3]


if __name__ == '__main__':
	n = 8 if len(sys.argv)<2 else int(sys.argv[1])
	print prime_power_decomp(n, True)




