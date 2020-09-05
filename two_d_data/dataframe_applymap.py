import pandas as pd

# DataFrame applymap()
df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [10, 20, 30],
    'c': [5, 10, 15]
})

def add_one(x):
    return x + 1
    
print(df.applymap(add_one))