class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        r2 = r3 = r5 = r7 = 0
        while temp % 2 == 0:
            r2 += 1
            temp //= 2
        while temp % 3 == 0:
            r3 += 1
            temp //= 3
        while temp % 5 == 0:
            r5 += 1
            temp //= 5
        while temp % 7 == 0:
            r7 += 1
            temp //= 7

        if temp > 1:
            return "-1"

        def min_spaces(c2, c3, c5, c7):
            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)
            c8, rem2 = divmod(c2, 3)
            c9, rem3 = divmod(c3, 2)
            if rem2 == 0 and rem3 == 0:
                extra = 0
            elif rem2 == 2 and rem3 == 1:
                extra = 2
            else:
                extra = 1
            return c5 + c7 + c8 + c9 + extra

        def consume(c2, c3, c5, c7, digit):
            if digit == 2:
                c2 -= 1
            elif digit == 3:
                c3 -= 1
            elif digit == 4:
                c2 -= 2
            elif digit == 5:
                c5 -= 1
            elif digit == 6:
                c2 -= 1
                c3 -= 1
            elif digit == 7:
                c7 -= 1
            elif digit == 8:
                c2 -= 3
            elif digit == 9:
                c3 -= 2
            return c2, c3, c5, c7

        digits = []
        has_zero = False
        for ch in num:
            if ch == '0' or has_zero:
                digits.append(1)
                has_zero = True
            else:
                digits.append(int(ch))

        n = len(digits)

        def build_suffix(prefix, factors, target_len):
            res = list(prefix)
            fc2, fc3, fc5, fc7 = factors
            for pos in range(len(prefix), target_len):
                spaces_left = target_len - 1 - pos
                for d in range(1, 10):
                    next_factors = consume(fc2, fc3, fc5, fc7, d)
                    if min_spaces(*next_factors) <= spaces_left:
                        res.append(d)
                        fc2, fc3, fc5, fc7 = next_factors
                        break
            return "".join(map(str, res))

        pref_factors = [(r2, r3, r5, r7)]
        for d in digits:
            pref_factors.append(consume(*pref_factors[-1], d))

        if min_spaces(*pref_factors[-1]) == 0:
            return "".join(map(str, digits))

        for i in range(n - 1, -1, -1):
            spaces_left = n - 1 - i
            for d in range(digits[i] + 1, 10):
                next_factors = consume(*pref_factors[i], d)
                if min_spaces(*next_factors) <= spaces_left:
                    return build_suffix(digits[:i] + [d], next_factors, n)

        target_len = max(n + 1, min_spaces(r2, r3, r5, r7))
        return build_suffix([], (r2, r3, r5, r7), target_len)