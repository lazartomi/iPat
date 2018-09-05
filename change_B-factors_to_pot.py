#
#
import sys

def format_pot(double):
	double10 = double*1
	string = str(double10)
	if double10 >= 0:
		string = string[0:4]
		string = '  '+string
	else:
		string = string[0:5]
		string = ' '+string
	
	return string;

if __name__ == "__main__":
	
	pdbfile = sys.argv[1]
	pdbname = pdbfile[0:4]
	chain = sys.argv[2]
	potfilename = "out_pdb_10-12A_pot.txt"
	pdbfilename = "PDB_files/"+pdbfile
	outfilename = "PDB_files/"+pdbname+"_"+chain+"_pot.pdb"
	
	str_buried = "-10.00"
	potmap = {}

	potfile = open(potfilename, 'r')
	array = []
	for line in potfile:
		line = line.strip()
		if line[0:6] == (pdbname + ' ' + chain):
			array = line.split()
			potmap[ int(array[2]) ] =  float(array[9])
	potfile.close()

	outfile = open(outfilename, 'w')
	pdbfile = open(pdbfilename, 'r')
	for line in pdbfile:
		line = line.strip()
		if line[0:4] == "ATOM":
			if line[20:22] == (" "+chain) :
				if int(line[22:26]) in potmap:
					line = line[0:60] + format_pot( potmap[int(line[22:26])]+0.00000000000001 ) + line[66:]
				else:
					line = line[0:60] + str_buried + line[66:]
				outfile.write(line + '\n')
		'''else:
			outfile.write(line + '\n')'''
	outfile.close()
	pdbfile.close()

