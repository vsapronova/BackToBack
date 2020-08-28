
import math

def squareRoot(n):
    '''
    :type n: int
    :rtype: int
    '''
    if n == 1:
        return 1
    end = n/2
    lo = 1
    ans = 0
    while lo <= end:
        mid = lo + math.floor(end - lo) / 2
        if math.floor(mid * mid) <= n:
            ans = mid
            lo = mid + 1
        else:
            end = mid - 1
    return ans



print(squareRoot(25))