import pandas as pd

data = {
    "Person": ["Alice", "Bob", "Charlie"],
    "Hobbies": [["Reading", "Hiking"], ["Gaming", "Coding", "Music"], ["Painting"]],
}

df = pd.DataFrame(data)

exploded_df = df["Hobbies"].explode()
print(exploded_df)
# or
exploded_df = df.explode("Hobbies")
print(exploded_df)
