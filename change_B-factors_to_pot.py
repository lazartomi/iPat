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
	
	pdbname = "3r2x"
	chain = 'C'
	potfilename = "/home/tomi/workspace/FinalScom/out_T50_10-12_ultimate_pot.txt"
	#potfilename = "/home/tomi/workspace/FinalScom/Conf_changes/Z_2O3B/unbound/out_unb_Z2O3B_10-12_ultimate_pot.txt"
	#potfilename = "/home/tomi/workspace/FinalScom/Conf_changes/Z_2O3B/bound/out_Z_2O3B_10-12_ultimate_pot.txt"
	pdbfilename = "/home/tomi/workspace/FinalScom/T50_files/"+pdbname+".pdb1"	
	#pdbfilename = "/home/tomi/workspace/FinalScom/Conf_changes/Z_2O3B/bound/"+pdbname+".pdb1"
	#pdbfilename = "/home/tomi/workspace/FinalScom/Conf_changes/Z_2O3B/unbound/"+pdbname+"_"+chain+".pdb"
	outfilename = "/home/tomi/workspace/FinalScom/"+pdbname+"_"+chain+"_pot_ultimate.pdb"
	
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

