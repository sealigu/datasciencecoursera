import re
import numpy as np

# Q1  
# string = ' bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
# result = re.findall('b[ao]t', string)
# print(result)

# # Q2
# def l2_dist(a, b):
#     result = ((a-b) * (a-b)).sum()
#     result = result ** 0.5
#     return result


# # Q3
# a1 = np.random.rand(4)
# a2 = np.random.rand(4, 1)
# a3 = np.array([[1, 2, 3, 4]])
# a4 = np.arange(1, 4, 1)
# a5 = np.linspace(1 , 4, 4)

# print(a1.shape)
# print(a2.shape)
# print(a5.shape)

# Q4
# old = np.array([[1, 1, 1], [1, 1, 1]])
# new = old
# new[0, :2] = 0
# print(old)

# Q6
# s = 'ACBCAC'
# result = re.findall('^AC', s)
# print(result)

# Q7
# s = 'ACAABAACAAAB'
# result = re.findall('A{1,2}', s)
# L = len(result)
# print(L)

# Q9
# string = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
# pattern = '(?<=[https]:\/\/)([A-Za-z0-9.]*)'
# result = re.findall(pattern, string)
# print(result)

# Q10
# text = r'''Everyone has the following fundamental freedoms:
# (a) freedom of conscience and religion;
# (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
# (c) freedom of peaceful assembly; and
# (d) freedom of association.
# '''
# pattern = '\(.\)'
# print(len(re.findall(pattern, text)))
