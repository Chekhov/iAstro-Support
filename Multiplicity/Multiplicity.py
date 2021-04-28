import argparse
import sys

#Para correr o programa basta
#python3 Multiplicity.py nomedoficheiro.tra

parser = argparse.ArgumentParser(description='Discover the Multiplicity')
parser.add_argument("file", help="Define .tra file here")

args = parser.parse_args()
if args.file :
	print("File read")
else:
	sys.exit("No Input File was given")

f = open(args.file)
content = f.readlines()

SQ = []
i = 0

for line in content:
	if line.find('SQ') != -1 :
		nk = line.split()
		# print(nk)
		SQ.append(int(nk[1]))
		i += 1	
	elif line.find('ET PH') != -1 :
		# print ("Hey we exist!")
		SQ.append(1)
		i += 1
	else:
		continue 

multiplicity = [SQ.count(1), SQ.count(2), SQ.count(3), sum(i > 3 for i in SQ)]
print("Multiplicity Parser")
print("All:", i)
print("SQ1:", multiplicity[0],"|", round(multiplicity[0]*100/i,5) , "%" )
print("SQ2:", multiplicity[1],"|", round(multiplicity[1]*100/i,5), "%")
print("SQ3:", multiplicity[2],"|", round(multiplicity[2]*100/i,5), "%")
print("SQ+:", multiplicity[3],"|", round(multiplicity[3]*100/i,5), "%")
