arr1 = [1, 1, 3, 2, 5, 6, 5]

# preserves order of the list
res = dict.fromkeys(arr1)
print(res)

# Doesn't preserves order of the list
print(set(arr1), list(set(arr1)))
print(list(res.keys()))

# preserves order of the list
res = {}
for i in arr1:
    res[i] = res.get(i, 0) + 1
print(res, res.keys())

# previous project, keys, schema(star), fact and dim tables, truncate and load
# ETL:
# Spark: Optimize
# SQL:
# AWS: EMR
# Data modelling:
