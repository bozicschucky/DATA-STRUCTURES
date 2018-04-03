class Range:
	"""A class that mimic's the built in range class """

	def __init__(self, start, stop=None, step=1):
		"""
		Intialize a Range Instance 
		Semantics is similar to built-in range class

		 """

		if step==0:
			raise ValueError('stop can\'t be 0')


		if stop is None:					#special case of range(n)
			start,stop=0,start 				#should be treated as if range(0,n)


		#Calculate the effective lenght once
		self._lenght = max(0, (stop-start+step-1)//step)

		#need knowledge of start and stop (but not stop) to support __getitem__
		self._start= start
		self._step=step 

	def __len__(self):
		"""
		Return number of entries in the range
		"""
		return self._lenght

	def __getitem__(self,k):
		"""
		Return entry at index k (Using standard interpreattion if negative )

		"""
		if k < 0:
			k += len(self) 			#attempt to convert negative index


		if not 0 <=k<self._lenght:
			raise IndexError('index out of range')

		return self._start + k *self._step

