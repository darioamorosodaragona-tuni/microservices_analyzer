import pandas as pd

data = pd.read_csv("include.csv")

result = [data.iloc[-4] == "M = proper microservice architecture"]
print(result)

