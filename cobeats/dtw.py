
# JHH - Cobeats -2020
# Copyright (C) GRyCAP - I3M - UPV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function
import math
import numpy as np
import sys

#def DTW(A, B, window = sys.maxint, d = lambda x,y: abs(x-y)):
def DTW(A, B, window = sys.maxsize, d = lambda x,y: abs(x-y)):
    # create the cost matrix
    A, B = np.array(A), np.array(B)
    M, N = len(A), len(B)
    #cost = sys.maxint * np.ones((M, N))
    cost = sys.maxsize * np.ones((M,N))

    # initialize the first row and column
    cost[0, 0] = d(A[0], B[0])
    for i in range(1, M):
        cost[i, 0] = cost[i-1, 0] + d(A[i], B[0])

    for j in range(1, N):
        cost[0, j] = cost[0, j-1] + d(A[0], B[j])
    # fill in the rest of the matrix
    for i in range(1, M):
        for j in range(max(1, i - window), min(N, i + window)):
            choices = cost[i - 1, j - 1], cost[i, j-1], cost[i-1, j]
            cost[i, j] = min(choices) + d(A[i], B[j])

    # find the optimal path
    n, m = N - 1, M - 1
    path = []

    while (m, n) != (0, 0):
        path.append((m, n))
        m, n = min((m - 1, n), (m, n - 1), (m - 1, n - 1), key = lambda x: cost[x[0], x[1]])

    path.append((0,0))
    return cost[-1, -1], path


def dtw_show(ts,pcs):
    A, B = np.array([1,2,3,4,2,3,2]), np.array([1,1,3,3,4,3,3,3])
    C = np.array([7,8,5,9,11,9,10])
    B = C
    A=ts
    B=pcs
    cost, path = DTW(A, B, window = 4)
    print ('Total Distance is %f' % (cost))
    import matplotlib.pyplot as plt
    offset = 0
    plt.xlim([-1, max(len(A), len(B)) + 1])
    plt.xlabel("Time --->")
    plt.ylabel("FLOPS --->")
    plt.plot(A)
    plt.plot(B)
    #plt.plot(B + offset)
    for (x1, x2) in path:
        plt.plot([x1, x2], [A[x1], B[x2] + offset])
    plt.show()

#if __name__ == '__main__':
#    main()




