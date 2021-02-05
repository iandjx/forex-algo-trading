# Basic arithmetic operation does a .map to the array
# += -= mutate array

# Unary operations
# >>> a = rg.random((2, 3))
# >>> a
# array([[0.82770259, 0.40919914, 0.54959369],
#        [0.02755911, 0.75351311, 0.53814331]])
# >>> a.sum()
# 3.1057109529998157
# >>> a.min()
# 0.027559113243068367
# >>> a.max()
# 0.8277025938204418


# to apply operations to a specific axis well use axis arg
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
# >>>
# >>> b.sum(axis=0)     # sum of each column
# array([12, 15, 18, 21])
# >>>
# >>> b.min(axis=1)     # min of each row
# array([0, 4, 8])
# >>>
# >>> b.cumsum(axis=1)  # cumulative sum along each row
# array([[ 0,  1,  3,  6],
#        [ 4,  9, 15, 22],
#        [ 8, 17, 27, 38]])


# accessing  value/s in a numpy array
# >>> def f(x, y):
# ...     return 10 * x + y
# ...
# >>> b = np.fromfunction(f, (5, 4), dtype=int)
# >>> b
# array([[ 0,  1,  2,  3],
#        [10, 11, 12, 13],
#        [20, 21, 22, 23],
#        [30, 31, 32, 33],
#        [40, 41, 42, 43]])
# >>> b[2, 3]
# 23
# >>> b[0:5, 1]  # each row in the second column of b
# array([ 1, 11, 21, 31, 41])
# >>> b[:, 1]    # equivalent to the previous example
# array([ 1, 11, 21, 31, 41])
# >>> b[1:3, :]  # each column in the second and third row of b
# array([[10, 11, 12, 13],
#        [20, 21, 22, 23]])