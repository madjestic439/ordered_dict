###!src/bin/python

"""classe for a dict who can be sorted and more..."""

class SortableDict:

	def __init__(self, *ADict, **KeyValues):
		param = {}
		if len(KeyValues) > 0 :
			for k, v in KeyValues.items() :
				param[k] = v
		elif len(ADict) > 0 :
			param = ADict[0]
		self.ks = []
		self.vals = []
		for pKey, pValue in param.items() :
			self.ks.append(pKey)
			self.vals.append(pValue)

	def __str__(self):
		present = '{'
		n = 0
		while n < len(self.ks) :
			if n > 0 :
				present += ', '
			present += "'{}': {}".format(self.ks[n], self.vals[n])
			n += 1
		present += '}'
		return present
