from neighbors import *
from cptFreq import *
from collections import Counter

def revComplement(sPtn):
	nLen = len(sPtn)
	sRevC = ""
	for i in range(nLen):
		nucl = ''
		if sPtn[i] == 'A':
			nucl = 'T'
		elif sPtn[i] == 'C':
			nucl = 'G'
		elif sPtn[i] == 'G':
			nucl = 'C'
		elif sPtn[i] == 'T':
			nucl = 'A'
		sRevC = nucl + sRevC
	return sRevC

def freqWordsWMismatches(sText, nLenPoly, nDist):
	lWordsWMismatches = []
	nLenText = len(sText)
	for i in range(nLenText - nLenPoly + 1):
		sPtn = sText[i:i+nLenPoly]
		sRevC = revComplement(sPtn)
		lPtnWMis = neighbors(sPtn, nDist)
		lRCWMis = neighbors(sRevC, nDist)
		lWordsWMismatches += [ptnToNumb(ptn) for ptn in (lPtnWMis+lRCWMis)]
	freqNumbWMis = Counter(lWordsWMismatches)
	freqVals = np.array(list(freqNumbWMis.values()))
	freqKeys = np.array(list(freqNumbWMis.keys()))
	mostFreqIdxs = np.argwhere(freqVals == np.amax(freqVals))
	freqPtnWMis = [numbToPtn(freqKeys[int(idx)], nLenPoly) for idx in mostFreqIdxs]
	return freqPtnWMis

if __name__ == "__main__":
	print(" ".join(freqWordsWMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)))