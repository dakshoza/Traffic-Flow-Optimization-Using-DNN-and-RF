import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary with the data
data = {
    'Time Cycle': [80, 80, 82, 81, 85, 83, 86, 82, 87, 82],
    'Human Controlled': [67, 74, 74, 67, 70, 62, 67, 80, 78, 71],
    'RFC': [106, 97, 94, 90, 100, 95, 95, 96, 93, 92],
    'DNN': [101, 93, 101, 96, 97, 97, 91, 97, 94, 103]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add an 'Iteration' column
df['Iteration'] = range(1, 11)

# Create the line plot
plt.figure(figsize=(12, 6))
for method in data.keys():
    plt.plot('Iteration', method, data=df, marker='o', linewidth=2, markersize=8, label=method)

# Customize the plot
plt.title('Scores Across Iterations for Discussed and Proposed Methods', fontsize=16)
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# Set y-axis limits to better showcase the differences
plt.ylim(60, 110)

# Add average score for each method as text
for method in data.keys():
    avg_score = df[method].mean()
    plt.text(10.1, df[method].iloc[-1], f'{method}: Avg = {avg_score:.1f}', 
             verticalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()  