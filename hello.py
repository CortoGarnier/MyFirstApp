import pandas as pd

# Create a DataFrame
data = {
    'name': ['John Doe', 'Jane Smith', 'vador'],
    'description': ['A sample description 1', 'A sample description 2', 'A sample description 3'],
    'title': ['Title 1', 'Title 2', 'Title 3']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

