import concurrent.futures
import multiprocessing
import numpy as np
import time

multiplier = 400

def random_matrix(num):
    return np.random.rand(num*multiplier,num*multiplier)

def heavy_function(matrixtoinvert):
    return np.linalg.inv(matrixtoinvert)
matrix_to_invert = random_matrix(5)

tstart = time.time()
results = [""]*5
for i in range(5):
    results[i] = heavy_function(matrix_to_invert)
print('Time taken with single processor is ', time.time()-tstart, ' seconds')

tstart = time.time()
results = [""]*5
for i in range(5):
    results[i] = heavy_function(matrix_to_invert)
print('Time taken with single processor is ', time.time()-tstart, ' seconds')

tstart = time.time()
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [""]*5
    for i in range(5):
        results[i] = executor.submit(heavy_function,matrix_to_invert)

print('Time taken with concurrent Futures is ', time.time()-tstart, ' seconds')

tstart = time.time()
results = [0]*5
for i in range(5):
    p = multiprocessing.Process(target = heavy_function, args = [matrix_to_invert])
    p.start()
    results[i]=p
for result in results:
    result.join()

print('Time taken with multi processing is ', time.time()-tstart, ' seconds')

tstart = time.time()
results = []
for i in range(5):
    p = multiprocessing.Process(target = heavy_function, args = [matrix_to_invert])
    p.start()
    results.append(p)
for result in results:
    result.join()

print('Time taken with multi processing 2 is ', time.time()-tstart, ' seconds')
