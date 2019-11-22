#Finding the prime factors of 600851475143
from joblib import Parallel, delayed
import multiprocessing
num_cores = multiprocessing.cpu_count()
prime_factors = []

n = 1
with Parallel(n_jobs=num_cores) as parallel:
    while n <= 600851475143:
        k = 0
        if 1600851475143 % n == 0:
            j = 1
            while (j <= n):
                if n % j == 0:
                    k = k + 1
                j = j+ 1
            if k==2:
                prime_factors.append(n)
        n = n + 1


print("The prime factors of 600851475143 are: ",prime_factors)
print("\n")
print("The largest prime factor of 600851475143 is: ", max(prime_factors))