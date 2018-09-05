import os;
import numpy as np;
import re;

def createUnbounds(filename):
	aminoacids = ['PHE','ILE','LEU','VAL','PRO','ALA','GLY','MET','CYS','TRP','TYR','THR','SER','GLN','ASN','GLU','ASP','HIS','LYS','ARG']
	is_xray = False
	chains = []
	pdbfile = open(filename, 'r')
	newpdbfile = ""
	for line in pdbfile:
		line = line.strip()
		if line[17:20] != "HOH":
			if line[0:4] == "ATOM" or line[0:6] == "HETATM" or line[0:3] == "TER":
				if line[0:4] == "ATOM" and line[17:20] not in aminoacids:
					break;
				else:
					if line[21:22] not in chains:
						chains.append( line[21:22] )
						os.system("touch " + filename[0 : len(filename)-5] + "_" + line[21:22] + ".pdb")
						newpdbfile = open(filename[0 : len(filename)-5] + "_" + line[21:22] + ".pdb", 'a+')
						newpdbfile.write(line + "\n")
					else:
						try:
							newpdbfile.write(line + "\n")
						except:
							#print "NOT POSSIBLE:  " + line
							pass

					if line[0:3] == "TER":
						newpdbfile.close()
			elif line[0:6] == "EXPDTA":
				if "X-RAY" in line:
					is_xray = True
			elif line[0:6] == "ENDMDL":
					break;
	pdbfile.close()		
	return chains, is_xray;



def getChains(filename):
	is_xray = False
	chains = []
	pdbfile = open(filename, 'r')
	newpdbfile = ""
	for line in pdbfile:
		line = line.strip()
		if line[17:20] != "HOH":
			if line[0:4] == "ATOM" or line[0:6] == "HETATM" or line[0:3] == "TER":
				if line[21:22] not in chains:
					chains.append( line[21:22] )
			elif line[0:6] == "EXPDTA":
				if "X-RAY" in line:
					is_xray = True
			elif line[0:6] == "ENDMDL":
					break;
	pdbfile.close()		
	return chains, is_xray;



def create_strides(filename, chains):
	os.system("./stride " + filename + " -f" + filename[0 : len(filename)-5] + ".str >temp.out")
	for chain in chains:
		try:
			os.system("./stride " + filename[0 : len(filename)-5] + "_" + chain + ".pdb -f" + filename[0 : len(filename)-5] + "_" + chain + ".str >>temp.out")
		except:
			print "Problem with " + filename[0 : len(filename)-5] + "_" + chain + ".pdb"
	return;



def calc_accessibility(filename, chains, pdbcode):
	surface = []
	interface = []
	intf_core = []
	
	AsaCs = {}
	stridefile = open(filename[0 : len(filename)-5] + ".str", 'r')
	for line in stridefile:
		line = line.strip()
		if line[0:3] == "ASG":
			AsaCs[ line[9:15] ] = float(line[64:70])
	stridefile.close()

	for chain in chains:
		if os.path.isfile("PDB_files/" + pdbcode + "_" + chain+ ".str") == False:
			return surface, interface, intf_core;
		stridefile = open(filename[0 : len(filename)-5] + "_" + chain + ".str", 'r')
		for line2 in stridefile:
			line2 = line2.strip()
			if line2[0:3] == "ASG":
				asaU = float(line2[64:70])
				aa = line2[5:8]
				chain = line2[9:10]
				m = re.search(r'\d+$', line2[10:15])
				if m is not None:
					resnum = int(line2[10:15])
				else:
					resnum = int(line2[10:14])
				relASA = getRelASA( asaU , aa )
				if relASA >= 0.1:
					surface.append( chain+" "+str(resnum) )
					asaC = AsaCs[ line2[9:15] ]
					if asaC < asaU:
						interface.append( chain+" "+str(resnum) )
						if getRelASA( asaC , aa ) < 0.25:
							intf_core.append( chain+" "+str(resnum) )
		stridefile.close()

	return surface, interface, intf_core;


def getRelASA(asa, aa):
	tripeptASA = {'PHE':210,'ILE':175,'LEU':170,'VAL':155,'PRO':145,'ALA':115,'GLY':75,'MET':185,'CYS':135,'TRP':255,'TYR':230,'THR':140,'SER':115,'GLN':180,'ASN':160,'GLU':190,'ASP':150,'HIS':195,'LYS':200,'ARG':225}
	return (asa / tripeptASA[ aa ] );


def properties_around(pdbcode, lins, radii, surface, interface, intf_core, property_dict):	
	aminoacids = ['PHE','ILE','LEU','VAL','PRO','ALA','GLY','MET','CYS','TRP','TYR','THR','SER','GLN','ASN','GLU','ASP','HIS','LYS','ARG']
	aa_prop = []
	for lin in lins:
		lin = lin.strip()
		string = ""
		if lin[0:4] == "ATOM" and lin[17:20] not in aminoacids:
			break;
		elif lin[0:4] == "ATOM" and lin[77:78] == 'C':
			if (lin[13:15] == "CA" or lin[13:17] == "CA A") and lin[13:17] != "CA B" and lin[13:17] != "CA C" and lin[13:17] != "CA D":
				chain = lin[21:22]
				resnum = int(lin[22:26]) 
				prop = property_dict[ lin[17:20] ]
				classif = getClassif(chain+" "+str(resnum), surface, interface, intf_core)
				coordx = float(lin[28:38])
				coordy = float(lin[38:46])
				coordz = float(lin[46:54])
				if classif != 'buried':
					string = pdbcode+" "+chain+" "+str(resnum)+" "+prop+" "
					for rad in radii:
						HPpn = [0,0,0,0]
						HPpn = collectProperties(lins, rad, chain, resnum, coordx, coordy, coordz, property_dict)
						#print pdbcode+" "+chain+" "+str(resnum)+" "+prop+" ", HPpn
						string += str(int(rad))+"A "+str(HPpn[0])+" "+str(HPpn[1])+" "+str(HPpn[2])+" "+str(HPpn[3])+" "
					string += classif
					aa_prop.append(string)
	return aa_prop;



def getClassif(key, surface, interface, intf_core):
	if key in surface:
		if key in interface:
			if key in intf_core:
				return 'interface_core'
			else:
				return 'interface_rim'
		else:
			return 'surface'
	else:
		return 'buried';



def collectProperties(lins, rad, chain, resnum, coordx, coordy, coordz, property_dict):
	HPpn = [0,0,0,0]
	for row in lins:
		row = row.strip()
		if row[0:4] == "ATOM" and row[77:78] == 'C':
			if (row[13:15] == "CA" or row[13:17] == "CA A") and row[13:17] != "CA B" and row[13:17] != "CA C" and row[13:17] != "CA D":
				chain2 = row[21:22]
				resnum2 = int(row[22:26]) 
				prop2 = property_dict[ row[17:20] ]
				classif2 = getClassif(chain2+" "+str(resnum2), surface, interface, intf_core)
				coordx2 = float(row[28:38])
				coordy2 = float(row[38:46])
				coordz2 = float(row[46:54])
				if classif2 != 'buried' and chain == chain2:
					if resnum != resnum2:
						if getDist(coordx, coordy, coordz, coordx2, coordy2, coordz2) <= rad:
							if prop2 == 'H':
								HPpn[0] += 1
							elif prop2 == 'P':
								HPpn[1] += 1
							elif prop2 == '+':
								HPpn[2] += 1
							elif prop2 == '-':
								HPpn[3] += 1
	return HPpn;



def getDist(coordx, coordy, coordz, coordx2, coordy2, coordz2):
	temp = (coordx-coordx2)*(coordx-coordx2) + (coordy-coordy2)*(coordy-coordy2) + (coordz-coordz2)*(coordz-coordz2)
	return np.sqrt(temp);




# ----------------------------------------------------------------------------------------------------------
# MAIN


radii = [10.0, 11.0, 12.0]
rad1 = str(int(radii[0]))
rad3 = str(int(radii[2]))
outfile = open("out_pdb_"+rad1+"-"+rad3+"A.txt", 'w')
outfile2 = open("out_pdb_"+rad1+"-"+rad3+"A.txt.out", 'w')

infile = open("pdb_ids.txt", 'r')
property_dict = {'ALA':'H','LEU':'H','MET':'H','PHE':'H','PRO':'H','TYR':'H','TRP':'H','ILE':'H','VAL':'H','ASN':'P','CYS':'P','GLN':'P','SER':'P','THR':'P','GLY':'P','ARG':'+','LYS':'+','HIS':'+','ASP':'-','GLU':'-'}				

filestoskip = open("filesnotavailable.txt", 'a')

for line in infile:
	line = line.strip()
	if len(line) == 4:
		pdbcode = line
		if os.path.isfile("PDB_files/" + line + ".pdb1") == False:
			try:
				os.system("wget -nv https://files.rcsb.org/download/" + line + ".pdb1.gz")
			except:
				print "Problem with " + line
			if os.path.isfile(line + ".pdb1.gz") == False:
				filestoskip.write(line + "\n")
				continue;
			os.system("mv " + line + ".pdb1.gz PDB_files/")
			os.system("gunzip PDB_files/" + line + ".pdb1.gz")
		complexfile = open("PDB_files/" + line + ".pdb1", 'r')
		lins = complexfile.readlines()
		is_xray = False
		chains = []
		num_chains = len([name for name in os.listdir("PDB_files") if name.startswith(line+'_') and os.path.isfile(os.path.join("PDB_files", name))])
		if num_chains <= 1:
			chains, is_xray = createUnbounds("PDB_files/" + line + ".pdb1")
		else:
			chains, is_xray = getChains("PDB_files/" + line + ".pdb1")
		if is_xray == True and len(chains) > 1:
			if num_chains <= 1:
				create_strides("PDB_files/" + line + ".pdb1", chains)
			outfile2.write(pdbcode + "\n")
			surface = []
			interface = []
			intf_core = []
			surface, interface, intf_core = calc_accessibility("PDB_files/" + line + ".pdb1", chains, pdbcode)
			if len(surface) == 0 and len(interface) == 0 and len(intf_core)	== 0:
				continue;
			aa_prop = []
			aa_prop = properties_around(pdbcode, lins, radii, surface, interface, intf_core, property_dict)
			for row in aa_prop:
				outfile.write(row+"\n")
			complexfile.close()
infile.close()
outfile.close()
outfile2.close()
filestoskip.close()

