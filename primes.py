'''
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a positive integer n, find all primes less than n.

Here's an example and some starter code:
'''

def find_primes(n):
    data = []
    for num in range(1,n+1):
        for i in range(2,num):
            if num%i == 0:
                break
            elif num in data:
                continue
            else:
                data.append(num)
    return data

print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
