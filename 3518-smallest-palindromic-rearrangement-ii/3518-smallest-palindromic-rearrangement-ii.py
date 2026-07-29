from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        chars = []
        half = []
        mid = ""

        for ch in sorted(cnt):
            chars.append(ch)
            half.append(cnt[ch] // 2)
            if cnt[ch] % 2:
                mid = ch

        m = sum(half)

        # Edge case: palindrome length = 1
        if m == 0:
            return s if k == 1 else ""

        CAP = k

        # Smallest Prime Factor
        spf = list(range(m + 1))
        for i in range(2, int(m ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        primes = []
        pidx = {}
        for i in range(2, m + 1):
            if spf[i] == i:
                pidx[i] = len(primes)
                primes.append(i)

        # Prime factorization of every number
        fac = [{} for _ in range(m + 1)]

        for x in range(2, m + 1):
            t = x
            d = {}
            while t > 1:
                p = spf[t]
                c = 0
                while t % p == 0:
                    t //= p
                    c += 1
                d[pidx[p]] = c
            fac[x] = d

        # Exponents of multinomial
        E = [0] * len(primes)

        def add_fact(v, sign):
            for i in range(2, v + 1):
                for idx, e in fac[i].items():
                    E[idx] += sign * e

        add_fact(m, 1)
        for c in half:
            add_fact(c, -1)

        def ways():
            res = 1
            for idx, e in enumerate(E):
                p = primes[idx]
                for _ in range(e):
                    res *= p
                    if res > CAP:
                        return CAP + 1
            return res

        if ways() < k:
            return ""

        ans = []
        counts = half[:]
        rem = m

        while rem:
            for i, ch in enumerate(chars):
                if counts[i] == 0:
                    continue

                # Apply update
                for idx, e in fac[rem].items():
                    E[idx] -= e
                for idx, e in fac[counts[i]].items():
                    E[idx] += e

                counts[i] -= 1
                w = ways()

                if w >= k:
                    ans.append(ch)
                    rem -= 1
                    break

                # Rollback
                k -= w
                counts[i] += 1
                for idx, e in fac[counts[i]].items():
                    E[idx] -= e
                for idx, e in fac[rem].items():
                    E[idx] += e

        left = "".join(ans)
        return left + mid + left[::-1]