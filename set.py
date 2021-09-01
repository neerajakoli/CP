# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

from itertools import combinations
def limitedPowerSet(n, k):
    # Your code goes here...
    demo = []
    for i in range (1,n+1):
        demo.append(i)
    l = [{}]
    for i in range(1,len(demo)+1):
        z=list(map(set, combinations(demo,i)))
        for j in range(len(z)):
            if (len(l)!=k):
                l.append(z[j])
            else:
                return l

assert (limitedPowerSet(5, 7)==[ {}, {1}, {2}, {3}, {4}, {5}, {1, 2}])
print("All test cases passed")