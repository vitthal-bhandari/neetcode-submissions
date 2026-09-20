class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        def dfs(openP, closeP):
            nonlocal subset
            if openP == closeP == n:
                res.append("".join(subset))
                return
            if openP < n:
                subset.append("(")
                dfs(openP + 1, closeP)
                subset.pop()
            if closeP < openP:
                subset.append(")")
                dfs(openP, closeP + 1)
                subset.pop()
            
        dfs(0, 0)
        return res