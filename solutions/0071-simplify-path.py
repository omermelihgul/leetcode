# 0071. Simplify Path
# https://leetcode.com/problems/simplify-path
# Difficulty: Medium
# Tags: String, Stack


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion and portion != ".":
                stack.append(portion)

        return "/" + "/".join(stack)


s = Solution()
print(s.simplifyPath("/home/"))  # "/home"
print(s.simplifyPath("/home//foo/"))  # "/home/foo"
print(s.simplifyPath("/home/user/Documents/../Pictures"))  # "/home/user/Pictures"
