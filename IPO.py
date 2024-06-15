class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mc1 = [(c, p) for c, p in zip(capital, profits)]
        heapify(mc1)
        mc2 = []
        while k:
            while mc1 and mc1[0][0] <= w:
                heappush(mc2, -heappop(mc1)[1])
            if not mc2:
                break
            w -= heappop(mc2)
            k -= 1
        return w
        