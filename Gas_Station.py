class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        start_index = 0
        end_index = 0
        total_gas = 0

        for i in range(n):
            total_gas += gas[i] - cost[i]

            if total_gas < 0:
                start_index = i + 1
                end_index = i + 1  
                total_gas = 0

        if end_index >= start_index and sum(gas) - sum(cost) >= 0:
            return start_index
        else:
            return -1
