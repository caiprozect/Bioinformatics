
def hammingDist(sPtnA, sPtnB):
	nHammingDist = 0
	assert(len(sPtnA) == len(sPtnB)), "Two patterns must have the same length"
	for i in range(len(sPtnA)):
		if sPtnA[i] != sPtnB[i]:
			nHammingDist += 1
	return nHammingDist

def neighbors(sPtn, nD):
	lNucls = ['A', 'C', 'G', 'T']
	if nD == 0:
		return sPtn
	if len(sPtn) == 1:
		return lNucls
	lNeighs = []
	sSuffixPtn = sPtn[1:]
	suffixNeighs = neighbors(sSuffixPtn, nD)
	for sText in suffixNeighs:
		if hammingDist(sSuffixPtn, sText) < nD:
			lNeighs = [(nucl+sText) for nucl in lNucls] + lNeighs
		else:
			lNeighs = [sPtn[0] + sText] + lNeighs
	return lNeighs

if __name__ == "__main__":
	print('\n'.join(neighbors("ACG", 1)))