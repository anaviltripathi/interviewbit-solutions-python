class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
            
        cost_sum = 0
        gas_sum = 0
        min_index = -1
        for i in range(len(gas)-1, -1, -1):
            cost_sum += cost[i]
            gas_sum += gas[i]
            if cost_sum <= gas_sum: 
                min_index = i
                cost_sum = 0
                gas_sum = 0
        
        return min_index

