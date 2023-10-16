import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://drive.google.com/file/d/1x3Sr7khSxY_KKdnZmrIBX52qVB6gAehR/view?usp=sharing'
file_id = url.split('/')[-2]
download_url = 'https://drive.google.com/uc?id=' + file_id
customers_df = pd.read_csv(download_url)

correlation_matrix = customers_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Basic')
plt.show()

mask = correlation_matrix.abs() < 0.5
correlation_triangle = correlation_matrix.mask(mask)

sns.heatmap(correlation_triangle, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap - Triangle')
plt.show()

sns.scatterplot(data=customers_df, x='Annual Income ($)', y='Family Size')
plt.xlabel('Annual Income ($)')
plt.ylabel('Family Size')
plt.title('Annual Income vs Family Size')