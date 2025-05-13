class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        nge = [-1] * n
        st = []
        
        st.append(n - 1)
        for i in range(n - 2, -1, -1):
            while st and prices[st[-1]] > prices[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            st.append(i)
        
        ans = [0] * n
        for i in range(n):
            if nge[i] == -1:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - prices[nge[i]]
        
        return ans