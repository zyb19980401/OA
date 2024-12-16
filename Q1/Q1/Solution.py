# We are find the min Variance. Which is min(len(subarray) - min(ele))
# We are only looking for pairs. Since 1XX1XX1 will always be worse than 1XX1
# Since occurence is always 2 for heights we can always keep a map to check last
# seen index of height and then find the length of subset - 2 which will give us our variance
#  the first element height in the group = 2 always
from collections import defaultdict


def findMinimumVariance(heights):
    last_seen = defaultdict(int)
    res = float('inf')
    for i,ele in enumerate(heights):
        if ele in last_seen:
            res = min(res, i - last_seen[ele] + 1 - 2)
        last_seen[ele] = i
    return res


if __name__ == '__main__':
    height = [4, 2, 5, 4]
    print(findMinimumVariance(height))