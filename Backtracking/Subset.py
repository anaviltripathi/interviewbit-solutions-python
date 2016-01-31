class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        all_subsets = [[]]
        for item in sorted(A):
            all_subsets += [prev_subset + [item] for prev_subset in all_subsets]
        return sorted(all_subsets)

