

from sys import argv

from partitions import *
from factorization import *
from manip import *

from copy import deepcopy



def gen_pp_cyclic_summands(pdec,start=0):
	if start==len(pdec):
		yield []
	else:
		p,e = pdec[start]
		currseqs = [[p**k for k in ptn] for ptn in partns[e]]
		
		for sseq in gen_pp_cyclic_summands(pdec,start+1):
			for seq in currseqs:
				yield [seq]+sseq


def to_torsion_coef_form(ppform):
	ppform = deepcopy(ppform)
	tcf = []
	factor = 0
	counter = sum(map(len,ppform))
	while counter:
		factor = 1
		for pcol in ppform:
			if pcol:
				factor*= pcol.pop(0)
				counter-=1
		tcf.append(factor)

	return tcf











n = int(argv[1])

pdec = prime_power_decomp(n)

print 'prime power decomposition:'

print fmt_decomp(n,pdec)





partns = {}

for _,e in pdec:
	if e not in partns:
		partns[e] = list(gen_parititions(e))

print 'Computing all Abelian groups of order %d: up to isomorphism'%n

print 'OUTPUT: A list of the orders of the cyclic summands'
print 

table = [['Prime Power Factor Decomposition', 'Torsion Coefficients Decomposition']]
count = 0
for ppcm in gen_pp_cyclic_summands(pdec):
	fl_ppcm = flatten_seq(ppcm)
	tcf = to_torsion_coef_form(ppcm)
	table.append( map(list_to_str,[fl_ppcm,tcf]) )
	count+=1

print_table(table)

print 
print 'Total group count:',count

