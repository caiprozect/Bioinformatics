import sys
from cptFreq import *
from neighbors import *

def medianString(nK, lDnas):
	lKmers = []
	for i in range(4**nK):
		lKmers.append(numbToPtn(i, nK))
	sMedian = ""
	dist = sys.maxsize
	for Kmer in lKmers:	
		tempDist = sum([distDnaPtn(sDna, Kmer) for sDna in lDnas])
		if tempDist <= dist:
			dist = tempDist
			sMedian = Kmer
	return sMedian

def distDnaPtn(sDna, sPtn):
	nK = len(sPtn)
	dist = sys.maxsize
	for i in range(len(sDna)-nK+1):
		sDnaSeg = sDna[i:i+nK]
		tempDist = hammingDist(sDnaSeg, sPtn)
		if tempDist <= dist:
			dist = tempDist
	return dist

def main():
	nK = 3
	sText = "AAATTGACGCAT\nGACGACCACGTT\nCGTCAGCGCCTGn\nGCTGAGCACCGG\nAGTTCGGGACAG"
	lDnas = sText.splitlines()
	sMedian = medianString(nK, lDnas)
	print(sMedian)

if __name__ == "__main__":
	main()