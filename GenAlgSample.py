"""
    By Jason Randolph Eads <jeads442@gmail.com>
    
    Written prior to July 2012
    Modified by Jason Eads 19-20 June 2014
    
    Method Inspiration: http://www.ai-junkie.com/ga/intro/gat3.html
"""

import random as rand

# make a genome
Genome = []
i = -1
while i < 32:
	i = i+1
	nuc = rand.randint(0, 15)
	if nuc < 10:
		Genome.append( nuc )
	elif nuc == 10:
		Genome.append( '+' )
	elif nuc == 11:
		Genome.append( '-' )
	elif nuc == 12:
		Genome.append( '*' )
	elif nuc == 13:
		Genome.append( '/' )
	else:
		Genome.append( ' ' )

# Convert to string and display
GenomeString = ''
for nuc in Genome:
	if nuc < 10:
		nuc = str(nuc)
	GenomeString += nuc
print
print 'Base Genome: ' + GenomeString

# Pick and display retained values
Retained = []
selecting = 'num' # op or num, start with num
for nuc in Genome:
    # If searching for a number, only collect the next digit
	if selecting == 'num':
		if nuc < 10:
			Retained.append(nuc)
			selecting = 'op'
    # If searching for an operator, only collect the next operator
	else: #selecting == 'op':
		if (nuc == '+') | (nuc == '-') | (nuc == '*') | (nuc == '/'):
			Retained.append(nuc)
			selecting = 'num'
			
if selecting == 'num': # Clean extra op 
	Retained.pop()


# Convert to string and display
GenomeString = ''
for nuc in Retained:
	if nuc < 10:
		nuc = str(nuc)
	GenomeString += nuc
	GenomeString += ' '
print
print 'Active Genome: ' + GenomeString


# Solve and display
cnt = len(Retained)
Retained.reverse()
while True:
	if(cnt >= 3):
		num1 = Retained[cnt-1]
		op = Retained[cnt-2]
		num2 = Retained[cnt-3]
		if ( op == '+' ):
			newnum = num1 + num2
		elif ( op == '-' ):
			newnum = num1 - num2
		elif ( op == '*' ):
			newnum = num1 * num2
		elif (op == '/') & (num2 != 0):
			newnum = float(num1) / num2
		elif (op == '/') & (num2 == 0):
			Retained = [""] # divide by zero
			break
		Retained.pop()
		Retained.pop()
		Retained.pop()
		Retained.append( newnum )
		cnt = len(Retained)
	else:
		break

print
print 'Genome Value: ' + str( Retained.pop() )
print
