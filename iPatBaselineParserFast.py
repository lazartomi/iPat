#
#
import pandas as pd
import numpy as np

def normDataFrame(data):
    summ = 0.0
    for i in range(0,4):
        for j in range(0,4):
            if(i >= j):
                summ += data[i][j]
        
    for i in range(0,4):
        for j in range(0,4):
            data[i][j] = data[i][j] / summ
    
    avg = (data[0][1] + data[1][0])/2; data[0][1] = avg; data[1][0] = avg;
    avg = (data[0][2] + data[2][0])/2; data[0][2] = avg; data[2][0] = avg;
    avg = (data[0][3] + data[3][0])/2; data[0][3] = avg; data[3][0] = avg;
    avg = (data[1][2] + data[2][1])/2; data[1][2] = avg; data[2][1] = avg;
    avg = (data[1][3] + data[3][1])/2; data[1][3] = avg; data[3][1] = avg;
    avg = (data[2][3] + data[3][2])/2; data[2][3] = avg; data[3][2] = avg;
    
    return data;


def generate_baseline(c1, c2, c3,  cI1, cI2, cI3):
   
    data1 = pd.DataFrame([
            [c1[0], c1[1], c1[2], c1[3]],
            [c1[4], c1[5], c1[6], c1[7]],
            [c1[8], c1[9], c1[10], c1[11]],
            [c1[12], c1[13], c1[14], c1[15]] ] )
    dataI1 = pd.DataFrame([
            [cI1[0], cI1[1], cI1[2], cI1[3]],
            [cI1[4], cI1[5], cI1[6], cI1[7]],
            [cI1[8], cI1[9], cI1[10], cI1[11]],
            [cI1[12], cI1[13], cI1[14], cI1[15]] ] )
    
    print '\n10A:\n'
    data1 = normDataFrame(data1)
    print data1
    print str(data1[0][0]) +", "+ str(data1[1][0]) +", "+ str(data1[2][0]) +", "+ str(data1[3][0]) +", "+ str(data1[0][1]) +", "+ str(data1[1][1]) +", "+ str(data1[2][1]) +", "+ str(data1[3][1]) +", "+ str(data1[0][2]) +", "+ str(data1[1][2]) +", "+ str(data1[2][2]) +", "+ str(data1[3][2]) +", "+ str(data1[0][3]) +", "+ str(data1[1][3]) +", "+ str(data1[2][3]) +", "+ str(data1[3][3]) 

    dataI1 = normDataFrame(dataI1)
    print dataI1
    print str(dataI1[0][0]) +", "+ str(dataI1[1][0]) +", "+ str(dataI1[2][0]) +", "+ str(dataI1[3][0]) +", "+ str(dataI1[0][1]) +", "+ str(dataI1[1][1]) +", "+ str(dataI1[2][1]) +", "+ str(dataI1[3][1]) +", "+ str(dataI1[0][2]) +", "+ str(dataI1[1][2]) +", "+ str(dataI1[2][2]) +", "+ str(dataI1[3][2]) +", "+ str(dataI1[0][3]) +", "+ str(dataI1[1][3]) +", "+ str(dataI1[2][3]) +", "+ str(dataI1[3][3]) 
    
    data1log = np.log(dataI1/data1)
    print data1log
    print str(data1log[0][0]) +", "+ str(data1log[1][0]) +", "+ str(data1log[2][0]) +", "+ str(data1log[3][0]) +", "+ str(data1log[0][1]) +", "+ str(data1log[1][1]) +", "+ str(data1log[2][1]) +", "+ str(data1log[3][1]) +", "+ str(data1log[0][2]) +", "+ str(data1log[1][2]) +", "+ str(data1log[2][2]) +", "+ str(data1log[3][2]) +", "+ str(data1log[0][3]) +", "+ str(data1log[1][3]) +", "+ str(data1log[2][3]) +", "+ str(data1log[3][3]) 
    
    
    data2 = pd.DataFrame([
            [c2[0], c2[1], c2[2], c2[3]],
            [c2[4], c2[5], c2[6], c2[7]],
            [c2[8], c2[9], c2[10], c2[11]],
            [c2[12], c2[13], c2[14], c2[15]] ] )
    dataI2 = pd.DataFrame([
            [cI2[0], cI2[1], cI2[2], cI2[3]],
            [cI2[4], cI2[5], cI2[6], cI2[7]],
            [cI2[8], cI2[9], cI2[10], cI2[11]],
            [cI2[12], cI2[13], cI2[14], cI2[15]] ] )
    
    print '\n11A:\n'
    data2 = normDataFrame(data2)
    print data2
    print str(data2[0][0]) +", "+ str(data2[1][0]) +", "+ str(data2[2][0]) +", "+ str(data2[3][0]) +", "+ str(data2[0][1]) +", "+ str(data2[1][1]) +", "+ str(data2[2][1]) +", "+ str(data2[3][1]) +", "+ str(data2[0][2]) +", "+ str(data2[1][2]) +", "+ str(data2[2][2]) +", "+ str(data2[3][2]) +", "+ str(data2[0][3]) +", "+ str(data2[1][3]) +", "+ str(data2[2][3]) +", "+ str(data2[3][3]) 

    dataI2 = normDataFrame(dataI2)
    print dataI2
    print str(dataI2[0][0]) +", "+ str(dataI2[1][0]) +", "+ str(dataI2[2][0]) +", "+ str(dataI2[3][0]) +", "+ str(dataI2[0][1]) +", "+ str(dataI2[1][1]) +", "+ str(dataI2[2][1]) +", "+ str(dataI2[3][1]) +", "+ str(dataI2[0][2]) +", "+ str(dataI2[1][2]) +", "+ str(dataI2[2][2]) +", "+ str(dataI2[3][2]) +", "+ str(dataI2[0][3]) +", "+ str(dataI2[1][3]) +", "+ str(dataI2[2][3]) +", "+ str(dataI2[3][3]) 
    
    data2log = np.log(dataI2/data2)
    print data2log
    print str(data2log[0][0]) +", "+ str(data2log[1][0]) +", "+ str(data2log[2][0]) +", "+ str(data2log[3][0]) +", "+ str(data2log[0][1]) +", "+ str(data2log[1][1]) +", "+ str(data2log[2][1]) +", "+ str(data2log[3][1]) +", "+ str(data2log[0][2]) +", "+ str(data2log[1][2]) +", "+ str(data2log[2][2]) +", "+ str(data2log[3][2]) +", "+ str(data2log[0][3]) +", "+ str(data2log[1][3]) +", "+ str(data2log[2][3]) +", "+ str(data2log[3][3]) 

    
    data3 = pd.DataFrame([
            [c3[0], c3[1], c3[2], c3[3]],
            [c3[4], c3[5], c3[6], c3[7]],
            [c3[8], c3[9], c3[10], c3[11]],
            [c3[12], c3[13], c3[14], c3[15]] ] )
    dataI3 = pd.DataFrame([
            [cI3[0], cI3[1], cI3[2], cI3[3]],
            [cI3[4], cI3[5], cI3[6], cI3[7]],
            [cI3[8], cI3[9], cI3[10], cI3[11]],
            [cI3[12], cI3[13], cI3[14], cI3[15]] ] )
    
    print '\n12A:\n'
    data3 = normDataFrame(data3)
    print data3
    print str(data3[0][0]) +", "+ str(data3[1][0]) +", "+ str(data3[2][0]) +", "+ str(data3[3][0]) +", "+ str(data3[0][1]) +", "+ str(data3[1][1]) +", "+ str(data3[2][1]) +", "+ str(data3[3][1]) +", "+ str(data3[0][2]) +", "+ str(data3[1][2]) +", "+ str(data3[2][2]) +", "+ str(data3[3][2]) +", "+ str(data3[0][3]) +", "+ str(data3[1][3]) +", "+ str(data3[2][3]) +", "+ str(data3[3][3]) 

    dataI3 = normDataFrame(dataI3)
    print dataI3
    print str(dataI3[0][0]) +", "+ str(dataI3[1][0]) +", "+ str(dataI3[2][0]) +", "+ str(dataI3[3][0]) +", "+ str(dataI3[0][1]) +", "+ str(dataI3[1][1]) +", "+ str(dataI3[2][1]) +", "+ str(dataI3[3][1]) +", "+ str(dataI3[0][2]) +", "+ str(dataI3[1][2]) +", "+ str(dataI3[2][2]) +", "+ str(dataI3[3][2]) +", "+ str(dataI3[0][3]) +", "+ str(dataI3[1][3]) +", "+ str(dataI3[2][3]) +", "+ str(dataI3[3][3]) 
    
    data3log = np.log(dataI3/data3)
    print data3log
    print str(data3log[0][0]) +", "+ str(data3log[1][0]) +", "+ str(data3log[2][0]) +", "+ str(data3log[3][0]) +", "+ str(data3log[0][1]) +", "+ str(data3log[1][1]) +", "+ str(data3log[2][1]) +", "+ str(data3log[3][1]) +", "+ str(data3log[0][2]) +", "+ str(data3log[1][2]) +", "+ str(data3log[2][2]) +", "+ str(data3log[3][2]) +", "+ str(data3log[0][3]) +", "+ str(data3log[1][3]) +", "+ str(data3log[2][3]) +", "+ str(data3log[3][3]) 

    column_labels = list('HP+-')
    row_labels = list('HP+-')
    
    return;


# --------------- main ---------------

if __name__ == "__main__":
    
    filename = "out_pdb_10-12A.txt"
    infile = open(filename, 'r')
    composition1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    composition2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    composition3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    
    compositionI1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    compositionI2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    compositionI3 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    
    e = 0
    pdbCodeBeginning = '00'
    prevChain = ''
    
    for line in infile:
        line = line.strip()
        if len(line) < 4:
            continue;
        array = line.split(" ")
        pdbCode = array[0]
        chain = array[1]
        thisChain = pdbCode + ' ' + chain
        aatype = array[3]
        
        if (pdbCodeBeginning != pdbCode[0:2] ):
            print pdbCode[0:2]
        pdbCodeBeginning = pdbCode[0:2]
        
        if (aatype == 'H'):
            e = 0
        elif (aatype == 'P'):
            e = 4
        elif (aatype == '+'):
            e = 8;
        elif (aatype == '-'):
            e = 12;
        
        begin = pdbCode + ' ' + chain + ' ' + array[2]

        if (array[19] == "interface_core"):
            is_interface = True
        else:
            is_interface = False

        
        H1 = array[5]
        P1 = array[6]
        p1 = array[7]
        n1 = array[8]
        H2 = array[10]
        P2 = array[11]
        p2 = array[12]
        n2 = array[13]
        H3 = array[15]
        P3 = array[16]
        p3 = array[17]
        n3 = array[18]
        
        
        if (is_interface == False):
            composition1[e+0] += int(H1)
            composition1[e+1] += int(P1)
            composition1[e+2] += int(p1)
            composition1[e+3] += int(n1)
            composition2[e+0] += int(H2)
            composition2[e+1] += int(P2)
            composition2[e+2] += int(p2)
            composition2[e+3] += int(n2)
            composition3[e+0] += int(H3)
            composition3[e+1] += int(P3)
            composition3[e+2] += int(p3)
            composition3[e+3] += int(n3)
        else:
            compositionI1[e+0] += int(H1)
            compositionI1[e+1] += int(P1)
            compositionI1[e+2] += int(p1)
            compositionI1[e+3] += int(n1)
            compositionI2[e+0] += int(H2)
            compositionI2[e+1] += int(P2)
            compositionI2[e+2] += int(p2)
            compositionI2[e+3] += int(n2)
            compositionI3[e+0] += int(H3)
            compositionI3[e+1] += int(P3)
            compositionI3[e+2] += int(p3)
            compositionI3[e+3] += int(n3)

        prevChain = thisChain
        
    generate_baseline(composition1, composition2, composition3, compositionI1, compositionI2, compositionI3)
    infile.close()
