import numpy as np

def ptnToNumb(sPtn):
	lNucls = ['A', 'C', 'G', 'T']
	nNumb = 0
	nPtnLen = len(sPtn)
	for i in range(nPtnLen):
		nNumb += 4**(nPtnLen-1-i) * lNucls.index(sPtn[i])
	return nNumb

def numbToPtn(nNumb, nK):
	lNucls = ['A', 'C', 'G', 'T']
	sPtn = ""
	nCurrQ = nNumb
	nCurrR = 0
	for i in range(nK):
		nCurrR = nCurrQ % 4
		sPtn = lNucls[nCurrR] + sPtn
		nCurrQ = int(nCurrQ/4)
	return sPtn

def cptFreq(sText, nK):
	nparrFreqArray = np.zeros(4**nK)
	nTextLen = len(sText)
	for i in range(nTextLen - nK + 1):
		sPtn = sText[i:i+nK]
		nNumb = ptnToNumb(sPtn)
		nparrFreqArray[nNumb] += 1
	return nparrFreqArray

def freqWords(sText, nK):
	nparrFreqArray = cptFreq(sText, nK)
	nparrMaxIdxs = np.argwhere(nparrFreqArray == np.amax(nparrFreqArray))
	lFreqWords = [numbToPtn(int(nNumb), nK) for nNumb in nparrMaxIdxs]
	return lFreqWords

def main():
	sText = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
	nK = 4
	lFreqWords = freqWords(sText, nK)
	print(" ".join(lFreqWords))

if __name__ == "__main__":
	main()