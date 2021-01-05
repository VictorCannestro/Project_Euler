from src.pe23 import recordSums 

def test_1():
    # Filter to find all the abundant numbers below the analytic limit
    N = 28123
    abundant = [k for k,v in  recordSums(N).items() if v > k]

    # Find all the numbers that are the sum of 2 abundant numbers (below analytic limit) 
    sum_of_2_abundants = set([i+j for i in abundant for j in abundant])

    # The set of all nums up to our analytic limit 
    all_nums = set([*range(1,N+1)])

    # Filter out all the numbers that can be written as the sum of two abundant numbers
    not_sum_of_2 = list(all_nums - sum_of_2_abundants)
    ans = sum(not_sum_of_2)
    assert ans == 4179871