from neighbors import *
from cptFreq import *
from collections import Counter

def freqWordsWMismatches(sText, nLenPoly, nDist):
	lWordsWMismatches = []
	nLenText = len(sText)
	for i in range(nLenText - nLenPoly + 1):
		sPtn = sText[i:i+nLenPoly]
		lPtnWMis = neighbors(sPtn, nDist)
		lWordsWMismatches += [ptnToNumb(ptn) for ptn in lPtnWMis]
	freqNumbWMis = Counter(lWordsWMismatches)
	freqVals = np.array(list(freqNumbWMis.values()))
	freqKeys = np.array(list(freqNumbWMis.keys()))
	mostFreqIdxs = np.argwhere(freqVals == np.amax(freqVals))
	freqPtnWMis = [freqKeys[idx] for idx in mostFreqIdxs]
	return freqPtnWMis

if __name__ == "__main__":
	print(" ".join(freqWordsWMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)))