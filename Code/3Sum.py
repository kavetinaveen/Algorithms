# Author: ddhnnngg
class Solution:
    def threeSum(self, nums):
    	n = len(nums)
    	pos = {}
    	neg = {}
    	zeros = 0
    	result = set()
    	for i in nums:
    		if i < 0:
    			neg.setdefault(i, 0)
    			neg[i] += 1
    		elif i > 0:
    			pos.setdefault(i, 0)
    			pos[i] += 1
    		else:
    			zeros += 1

    	for i in nums:
    		if i < 0:
    			for j in pos:
    				k = -i-j
    				if k in pos:
    					if k == j and pos[j]-1 < 1:
    						continue
    					else:
    						result.add(tuple(sorted((i, j, k))))
    				elif k == 0 and zeros > 0:
    					result.add(tuple(sorted((i, j, 0))))
    		elif i > 0:
    			for j in neg:
    				k = -i-j
    				if k in neg:
    					if k == j and neg[j]-1 < 1:
    						continue
    					else:
    						 result.add(tuple(sorted((i, j, k))))
    				elif k == 0 and zeros > 1:
    					result.add(tuple(sorted((i, j, k))))
    	if zeros >= 3:
    		result.add((0, 0, 0))
 		   					
    	return [list(x) for x in result]