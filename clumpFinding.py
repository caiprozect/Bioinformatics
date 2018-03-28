from cptFreq import *
from time import time

def clumpFinding(sGenome, nLenPolymer, nOccur, nLenReg):
	nparrClump = np.zeros(4**nLenPolymer)
	sText = sGenome[0:nLenReg]
	nparrFreqArray = cptFreq(sText, nLenPolymer)
	for i in np.argwhere(nparrFreqArray >= nOccur):
		nparrClump[int(i)] = 1
	for i in range(1, len(sGenome) - nLenReg + 1):
		sFstPtn = sGenome[i-1:i-1+nLenPolymer]
		nFstIdx = ptnToNumb(sFstPtn)
		nparrFreqArray[nFstIdx] -= 1
		sLstPtn = sGenome[i+nLenReg-nLenPolymer:i+nLenReg]
		nLstIdx = ptnToNumb(sLstPtn)
		nparrFreqArray[nLstIdx] += 1
		if nparrFreqArray[nLstIdx] >= nOccur:
			nparrClump[nLstIdx] = 1
	lFreqPtns = [numbToPtn(int(i), nLenPolymer) for i in np.argwhere(nparrClump==1)]
	return lFreqPtns

def main():
	fName = "E.ColiGenome.txt"
	fHandle = open(fName, 'r')
	sGenome = fHandle.read()
	fHandle.close()
	nLenPolymer = 9
	nOccur = 3
	nLenReg = 500
	lFreqPtns = clumpFinding(sGenome, nLenPolymer, nOccur, nLenReg)
	#print(" ".join(lFreqPtns))
	print(len(lFreqPtns))

if __name__ == "__main__":
	main()