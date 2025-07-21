from sklearn.datasets import fetch_covtype

data_bunch = fetch_covtype(as_frame=True)
print(data_bunch.DESCR)  # description of the dataset

df = data_bunch.data  # Extract the actual DataFrame
target = data_bunch.target  # Extract the target variable
df['Cover_Type'] = target  # Add the target variable to the DataFrame

print(type(df))

class dataset:
        def __init__(self):
                self.df = df
        
        def get_dataframe(self):
                return self.df
