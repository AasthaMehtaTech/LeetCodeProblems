'''
https://leetcode.com/discuss/interview-question/818225/GOOGLE-or-OA-(intern-2021-India)-or-The-minimum-cost


DP with Bitmasking. But approach is slow for large N > 13.

s='12345'
for k in range(1<<len(s)):
    #will give 32 combinations/rows of 4 ele each
    print(k, end=' this: ')
    for i in range(len(s)):
        #print((k & (1 << i)),end=', ')#binary val weights
        print((k & ~(1 << i)),end=' ')# k's complement
    print(' ')
'''

def minimum_cost(s, cost):
    f = [[float("Inf")]*len(s) for k in range(1<<len(s))]
    
    for k in range(1<<len(s)):
        for i in range(len(s)):
            if (k & (1 << i)) != 0:
                if (k & ~(1 << i)) == 0:
                    f[k][i] = 0
                else:
                    for j in range(len(s)):
                        if j != i:
                            f[k][i] = min(f[k][i], f[k & ~(1 << i)][j] + cost[j][i])
    
    return min(f[(1<<len(s))-1])
