# %%
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns

# %%
data = pd.read_csv(r"cereal.csv")

# %%
print(data.head())

# %%
print(data.describe())

# %%
print(data[["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "potass", "vitamins", "shelf", "weight", "cups", "rating"]].corr())

# %%
plt.figure(figsize = (10, 8))
sns.heatmap(data[["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "potass", "vitamins", "shelf", "weight", "cups", "rating"]].corr(), annot = True, cmap = "coolwarm", vmin = -1, vmax = 1)
plt.title("Correlation Matrix of Cereal")
plt.show()

# %%
scatter_data = pd.DataFrame(data)

plt.figure(figsize = (12, 10))
pd.plotting.scatter_matrix(scatter_data, figsize = (12, 10))
plt.suptitle("Scatter Matrix of Cereal", y = 0.95)
plt.show()

# %%
plt.figure(figsize = (8, 5))
mfr_count = data["mfr"].value_counts()
sns.barplot(x = mfr_count.index, y = mfr_count.values, palette = "pastel")
plt.title("Number of Cereals by Manufacturer")
plt.xlabel("Manufacturer")
plt.ylabel("Count")
plt.xticks(rotation = 45)
plt.show()

# %%
plt.figure(figsize = (8, 6))
sns.scatterplot(x = "calories", y = "rating", data = data, hue = "mfr", palette = "Set2", s = 100)
plt.title("Calories vs. Rating of Cereals")
plt.xlabel("Calories")
plt.ylabel("Rating")
plt.legend(title = "Manufacturer", loc = "upper left", bbox_to_anchor = (1, 1))
plt.show()

# %%
plt.figure(figsize = (8, 6))
sns.histplot(data["rating"], bins = 10, kde = True, color = "skyblue")
plt.title("Histogram of Ratings of Cereals")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()
