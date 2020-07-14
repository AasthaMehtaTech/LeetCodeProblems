#smart short
class Solution:
    def coinChange(self,c,a):
        c.sort(reverse=True)
        n,r=len(c),a+1
        def dfs(x,t,cnt_until_now):
            nonlocal r
            if cn+math.ceil(t/c[x])>=r:return
            if t%c[x]==0:
                r=cnt_until_now+t//c[x]
                return
            if x==n-1:return
            for i in range(t//c[x],-1,-1):dfs(x+1,t-c[x]*i,cnt_until_now+i)
        dfs(0,a,0)
        return-1if r>a else r


#fastest dfs
class Solution:
    def coinChange(self, coins, amount):
        def dfs(start, amt, n_coins):
            nonlocal min_coins

            coin = coins[start]

            # LHS = lower bound on number of coins, achieved using the current coin
            # Return early since we can't possibly achieve original "amount"
            # along this path.
            # For this particular solution, this check isn't necessarily,
            # since there is another check within the loop below. However, it
            # speeds up the solution. Better to have this check before the
            # "amt == 0" check below.
            #if n_coins + (amt + coin - 1) / coin > min_coins:
            #if (min_coins - n_coins - 1) * coin + 1 < amt:
            #    return

            div = amt // coin
            n_coins += div
            amt %= coin
            
            if amt == 0:
                min_coins = min(min_coins, n_coins)
                return
            
            if start < len_coins:
                # use as many of current coin as possible, and try next smaller coin
                dfs(start + 1, amt, n_coins)

                # Always greedily taking as many of biggest coins as possible doesn't work.
                # "Backtrack" by using 1 less of current coin per iteration, and
                # trying the next smaller coin.

                next_coin = coins[start + 1]
                
                for _ in range(div):
                    amt += coin 
                    n_coins -= 1
                    
                    if (min_coins - n_coins - 1) * next_coin + 1 > amt:
                    #if (min_coins - n_coins) * next_coin > amt: # hope still exists
                        dfs(start + 1, amt, n_coins)
                    else:
                        break
        
        len_coins = len(coins) - 1
        
        # try biggest coins first
        coins.sort(reverse=True)
        
        min_coins = float('inf')

        dfs(0, amount, 0)
        
        return min_coins if min_coins < float('inf') else -1
