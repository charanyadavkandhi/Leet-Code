class Solution:
    def sumAndMultiply(self, s: str, a: List[List[int]]) -> List[int]:
        M = 10**9+7
        p = [*accumulate(map(int,s),lambda q,v:v and (q*10+v)%M or q,initial=0)]
        w = [*accumulate((c>'0' for c in s),initial=0)]
        q = [*accumulate(map(int,s),initial=0)]

        return [(p[r+1]-p[l]*pow(10,w[r+1]-w[l],M))*(q[r+1]-q[l])%M for l,r in a]