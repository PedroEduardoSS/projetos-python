import pandas as pd

dic = {"col1": [1,2,3,4], "col2":[2,3,4,5]}

df = pd.DataFrame(dic)

df.to_csv("pasta\my-file.csv", index=False)

data = pd.read_csv("pasta\my-file.csv")
print(data)