# How to add a Level to Pandas MultiIndex in Python

import pandas as pd

df = pd.DataFrame({
    'A': [1, 1, 1, 2, 3],
    'B': [1, 2, 3, 4, 5]
})

df2 = pd.concat([df], keys=['X'], names=['First Level'])

#                A  B
# First Level
# X           0  1  1
#             1  1  2
#             2  1  3
#             3  2  4
#             4  3  5
print(df2)

print('-' * 50)

# 👇️ ['First Level', None]
print(df2.index.names)