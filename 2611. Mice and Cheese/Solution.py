class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:

        # mouse1 can eat only k but mouse2 can eat all thats left
        # mouse2 picks all the cheese but drops laters based on what mouse1 picks
        m2 = sum(reward2)

        # finding difference in score is mouse1 picks that type of cheese
        diff = [a-b for a,b in zip(reward1, reward2)]

        # sorting difference array so we get bigger cheese for mouse1
        diff.sort(reverse=True)

        # pick only larget k of cheese and return with m2
        return sum(diff[:k:]) + m2