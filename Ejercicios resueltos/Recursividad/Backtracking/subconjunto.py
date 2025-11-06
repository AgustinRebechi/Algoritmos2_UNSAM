def subconjuntos(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res, sol = [], []

    def backtrack(i):
        # Caso Base
        if i == n:
            res.append(sol[:])
            return
        
        # No agarro nums[i]
        backtrack(i+1)

        # Agarro num[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return res

print(subconjuntos([1,2,3]))