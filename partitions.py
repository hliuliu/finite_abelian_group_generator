

import sys

def gen_parititions(n,m=None,descending=True):
	'''
		Generates the integer partitions of n with largest part at most m
		Each Partiton is stored as a list
	'''

	if m is None:
		m=n

	if n==0:
		yield []
	else:
		m = min (n,m)
		while m:
			for subseq in gen_parititions(n-m, m, descending):
				if descending:
					subseq.insert(0,m)
				else:
					subseq.append(m)
				yield subseq

			m-=1


def fmt_partition(n, partn):
	return '%d = '%n + ' + '.join(map(str,partn))




if __name__ == '__main__':
	n = 3 if len(sys.argv)<2 else int(sys.argv[1])
	print 'Generating partitions of %d with parts in descending order'%n
	ct = 0
	for el in gen_parititions(n):
		print el,'-->',fmt_partition(n,el)
		ct += 1
	print 'Total number of partitions:',ct


