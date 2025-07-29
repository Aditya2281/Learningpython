# sp100_analysis_numpy.py

import numpy as np
import matplotlib.pyplot as plt
import csv

import numpy as np

# Full path to CSV file
file_path = r'C:\Users\Admin\Downloads\sp100.csv'

try:
    data = np.genfromtxt(file_path, delimiter=',', names=True, dtype=None, encoding='utf-8')
    print(" CSV loaded successfully.")
    print("First 5 rows:\n", data[:5])
except FileNotFoundError:
    print(" File not found. Please check the path.")
except Exception as e:
    print(" Error loading CSV:", e)

#1. Print all company names and their sectors
print("1. Company Names and Sectors")
for company in data:
    print(f"{company['Name']} ({company['Sector']})")


#2. Compute and print the average price and EPS
print("\n2.Average Price and EPS")
avg_price = np.mean(data["Price"])
avg_eps = np.mean(data["EPS"])
print(f"Average Price:{avg_price:.2f},Average EPS:{avg_eps:.2f} ")

# 3. Compute P/E Ratio for each company and add it to a new array
print("\n3.P/E Ratios")
pe_ratios = data["Price"]/ data['EPS']
print(pe_ratios)

# 4. Find the company with the highest P/E ratio
print("\n4. Company with Highest P/E Ratio")
max_index = np.argmax(pe_ratios)
print(f"Highest P/E:{data['Name'][max_index]} ({pe_ratios[max_index]:.2f})")

# 5. Filter and print all companies in the 'Financials' sector
print("n\5.Companies in Financials Sector")
financials = data[data['Sector'] == 'Financials']
for row in financials:
    print(f"{row['Name']}: {row['Price']}")

# 6. Count how many companies are in each sector
print("\n6.Sector Counts")
unique_sectors,counts = np.unique(data['Sector'],return_counts = True)
for sector,count in zip(unique_sectors,counts):
    print(f"{sector}:{count}")


# 7. Calculate average P/E for each sector
print("\n7. Sector-wise Average P/E")
for sector in unique_sectors:
    mask = data['Sector']==sector
    sector_pe= pe_ratios[mask]
    print(f"{sector}:AvgP/E = {np.mean(sector_pe):.2f}")

# 8. Create a histogram of P/E ratios
print("\n8. Histogram of P/E Ratios")
plt.hist(pe_ratios, bins=10, edgecolor='black')
plt.title("Distribution of P/E Ratios")
plt.xlabel("P/E Ratio")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# 9. Identify outlier P/E ratios (2 std above mean)
print("\n9. Outlier Companies")
mean_pe = np.mean(pe_ratios)
std_pe = np.std(pe_ratios)
outlier_mask =pe_ratios >(mean_pe + 2 * std_pe)
print("Outliers:")
print(data['Name'][outlier_mask])

# 10. List top 5 companies with lowest P/E
print("\n10. Top 5 Companies with Lowest P/E")
sorted_indices = np.argsort(pe_ratios)
for idx in sorted_indices[:5]:
    print(f"{data['Name'][idx]}:{pe_ratios[idx]:.2f}")

# 11. Export the original dataset with computed P/E as CSV
print("\n11. Exporting to sp100_with_pe.csv")
with open('sp100_with_pe.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Sector', 'Price', 'EPS', 'P/E'])
    for row, pe in zip(data, pe_ratios):
        writer.writerow([row['Name'], row['Sector'], row['Price'], row['EPS'], round(pe, 2)])

# 12. Plot sector-wise average P/E as a bar chart
print("\n12. Sector-wise Average P/E Bar Chart")
sector_averages = [np.mean(pe_ratios[data['Sector'] == sec]) for sec in unique_sectors]
plt.bar(unique_sectors, sector_averages)
plt.xticks(rotation=90)
plt.ylabel("Average P/E Ratio")
plt.title("Sector-wise Average P/E")
plt.tight_layout()
plt.show()
