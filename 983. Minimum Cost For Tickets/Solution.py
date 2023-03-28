class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:

        dp = dict()

        def helper(index, spent, pass_till_date):

            if index >= len(days):
                return spent

            # Using 3D based array for achieving dynamic programming
            if index not in dp.keys():
                dp[index] = dict()
            if spent not in dp[index].keys():
                dp[index][spent] = dict()
            if pass_till_date in dp[index][spent].keys():
                return dp[index][spent][pass_till_date]

            curr = float('inf')

            if pass_till_date < days[index]:
                # can buy three passes since pass expired
                curr = min(helper(index+1, costs[0], days[index])+spent, curr)
                curr = min(helper(index+1, costs[1], days[index]+6)+spent, curr)
                curr = min(helper(index+1, costs[2], days[index]+29)+spent, curr)
            else:
                # if pass isnt expired then continue, no need to renew
                curr = min(helper(index+1, 0, pass_till_date)+spent, curr)

            dp[index][spent][pass_till_date] = curr
            # return the current spent
            return curr

        # calling the helper function assuming 0th day with 0 spendings
        return helper(0, 0, 0)