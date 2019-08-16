

def iterable(seq):
	try:
		iter(seq)
	except:
		return False
	return True


def type_is(datatype):
	return lambda seq: type(seq) is datatype


def flatten_seq(L,iter_test= iterable):
	F = []

	for x in L:
		if iter_test(x):
			F.extend(flatten_seq(x))
		else:
			F.append(x)

	return F


def list_to_str(L,delim = ', '):
	return delim.join(map(str,L))

def print_table_row(row,width):
	efmt = '{:^%d}'%width
	print '|'.join([efmt.format(entry) for entry in row])

def print_table(str_table, padding = 5, header = True):
	width = max([max(map(len,row)) for row in str_table])
	width += 2*padding

	for i, row in enumerate(str_table):
		print_table_row(row,width)
		if header and not i:
			print '+'.join(['-'*width for _ in row])






