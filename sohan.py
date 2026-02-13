import pandas as pd 
# Load dataset 
df = pd.read_csv("C:/Users/Ganesh/Downloads/Chocolate Sales (2) (1).csv") 
# 1. head() command 
print("\n1. head() - First 5 rows:") 
print(df.head()) 
print() 
# 2. info() command 
print("2. info() - Dataset information:") 
df.info() 
print() 
# 3. describe() command 
print("3. describe() - Statistical summary:") 
print(df.describe(include='all')) 
print() 
# 4. shape command 
print("4. shape - Dataset dimensions:") 
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}") 
print() 
print("\n
🔹
 TECHNIQUE 1: Check missing values") 
print(df.isnull().sum()) 
print() 
print("
🔹
 TECHNIQUE 2: Check duplicate rows") 
duplicates = df.duplicated().sum() 
print(f"Duplicate rows found: {duplicates}") 
print() 
print("\n
🔹
 TECHNIQUE 3: Remove duplicates") 
# First define duplicates 
duplicates = df.duplicated().sum() 
print(f"Duplicate rows found: {duplicates}") 
# Then remove duplicates 
if duplicates > 0: 
df = df.drop_duplicates() 
print(f"Removed {duplicates} duplicate rows") 
else: 
print("No duplicates to remove") 
print(f"Rows after cleaning: {df.shape[0]}") 
print() 
print("\n
🔹
 TECHNIQUE 4: Standardize column names") 
print("Original columns:", df.columns.tolist()) 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_') 
print("Cleaned columns:", df.columns.tolist()) 
print() 
print("\n
🔹
 TECHNIQUE 5: Fix data types") 
print("Before fixing - Data types:") 
print(df.dtypes) 
print() 
# Fix Date column (correct column name: 'Date') 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
# Fix Amount column (convert to numeric) 
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce') 
print("After fixing - Data types:") 
print(df.dtypes) 
print() 
print("\n
🔹
 TECHNIQUE 6: Extract date features") 
# Make sure Date is datetime 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
# Extract features 
df['year'] = df['Date'].dt.year 
df['month'] = df['Date'].dt.month 
df['day'] = df['Date'].dt.day 
df['day_name'] = df['Date'].dt.day_name() 
print("Extracted: year, month, day, day_name") 
print() 
print("\n
🔹
 TECHNIQUE 7: Extract exact release date") 
 
# Ensure datetime format (safety) 
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce') 
 
# Create formatted date column (YYYY-MM-DD) 
df['exact_release_date'] = df['release_date'].dt.strftime('%Y-%m-%d') 
 
# Print sample dates 
print("Sample exact release dates:") 
print(df['exact_release_date'].head(10)) 
 
print("\nDate range in dataset:") 
print("Earliest movie date:", df['exact_release_date'].min()) 
print("Latest movie date:", df['exact_release_date'].max()) 
print() 
 
print("\n
🔹
 TECHNIQUE 8: Create sale amount categories") 
 
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce') 
 
def amount_cat(value): 
    if value < 1000: 
        return 'Low' 
    elif value < 5000: 
        return 'Medium' 
    else: 
        return 'High' 
 
df['amount_category'] = df['Amount'].apply(amount_cat) 
 
print(df['amount_category'].value_counts()) 
print() 
 
print("\n
🔹
 TECHNIQUE 9: Binary encoding") 
df['is_usa'] = df['Country'].apply(lambda x: 1 if str(x).lower() == 'usa' else 0) 
print("Created binary column: is_usa") 
print() 
 
print("\n
🔹
 TECHNIQUE 10: Product grouping") 
 
def product_group(name): 
    name = str(name).lower() 
    if 'dark' in name: 
        return 'Dark Chocolate' 
    elif 'milk' in name: 
        return 'Milk Chocolate' 
    elif 'white' in name: 
        return 'White Chocolate' 
    else: 
        return 'Other' 
df['product_group'] = df['Product'].apply(product_group) 
print(df['product_group'].value_counts()) 
print() 
 
print("\n
🔹
 TECHNIQUE 11: Sales performance grouping (based on Boxes Shipped)") 
def performance_by_boxes(boxes): 
    if boxes < 50: 
        return 'Low Performance' 
    elif boxes < 150: 
        return 'Medium Performance' 
    else: 
        return 'High Performance' 
df['performance_group'] = df['Boxes Shipped'].apply(performance_by_boxes) 
print("Sales performance groups created based on Boxes Shipped:") 
print(df['performance_group'].value_counts()) 
print() 
 
print("\n
🔹
 TECHNIQUE 12: High sales indicator") 
 
# Create binary indicator based on shipment volume 
df['is_high_sale'] = df['Boxes Shipped'].apply(lambda x: 1 if x >= 100 else 0) 
 
print("Created binary column: is_high_sale") 
print(df['is_high_sale'].value_counts()) 
print() 
 
print("\n
🔹
 TECHNIQUE 13: Sales aggregation (Daily)") 
 
# Ensure Date is datetime 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
 
daily_sales = df.groupby('Date').agg( 
    Total_Amount=('Amount', 'sum'), 
    Total_Boxes=('Boxes Shipped', 'sum'), 
    Orders_Count=('Product', 'count') 
).reset_index() 
 
print("Daily aggregated sales data:") 
print(daily_sales.head()) 
print() 
print("\n
🔹
 TECHNIQUE 14: Sales Amount Distribution (Histogram)") 
import matplotlib.pyplot as plt 
plt.figure(figsize=(10, 5)) 
plt.hist(df['Amount'], bins=30) 
plt.title("Distribution of Sales Amount") 
plt.xlabel("Sales Amount") 
plt.ylabel("Frequency") 
plt.grid(True, alpha=0.3) 
plt.show() 
print("Histogram displayed for sales amount distribution") 
print() 
import matplotlib.pyplot as plt 
import seaborn as sns 
df['Amount'] = pd.to_numeric(df['Amount'].replace('[\$,]', ', regex=True), errors='coerce') 
df = df.dropna(subset=['Amount']) 
plt.figure(figsize=(10, 6)) 
sns.histplot(df['Amount'], bins=30, kde=True, color="chocolate") 
plt.title("Sales Amount Distribution (Histogram)") 
plt.xlabel("Sales Amount") 
plt.ylabel("Frequency") 
plt.show() 
import matplotlib.pyplot as plt 
df['Amount'] = pd.to_numeric( 
df['Amount'].replace('[\$,]', ', regex=True), 
errors='coerce' 
) 
top_products = ( 
df.groupby('Product')['Amount'] 
.sum() 
.sort_values(ascending=False) 
.head(10) 
) 
plt.figure(figsize=(10, 6)) 
top_products.plot(kind='bar') 
plt.title("Top 10 Products by Total Sales") 
plt.xlabel("Product") 
plt.ylabel("Total Sales Amount") 
plt.xticks(rotation=45, ha='right') 
plt.tight_layout() 
plt.show() 
import matplotlib.pyplot as plt 
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) 
# Clean Amount column 
df['Amount'] = pd.to_numeric( 
df['Amount'].replace('[\$,]', ', regex=True), 
errors='coerce' 
) 
df = df.dropna(subset=['Date', 'Amount']) 
sales_trend = df.groupby('Date')['Amount'].sum() 
plt.figure(figsize=(12, 6)) 
plt.plot(sales_trend.index, sales_trend.values) 
plt.title("Sales Trend Over Time") 
plt.xlabel("Date") 
plt.ylabel("Total Sales Amount") 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show() 
import seaborn as sns 
import matplotlib.pyplot as plt 
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) 
df['Amount'] = pd.to_numeric( 
df['Amount'].replace('[\$,]', ', regex=True), 
errors='coerce' 
) 
numeric_df = df.select_dtypes(include='number') 
corr_matrix = numeric_df.corr() 
plt.figure(figsize=(8, 6)) 
sns.heatmap( 
corr_matrix, 
annot=True, 
cmap='coolwarm', 
fmt=".2f", 
linewidths=0.5 
) 
plt.title("Correlation Heatmap of Sales Data") 
plt.tight_layout() 
plt.show() 
import matplotlib.pyplot as plt 
import pandas as pd 
df['Amount'] = pd.to_numeric( 
df['Amount'].replace('[\$,]', ', regex=True), 
errors='coerce' 
) 
df['Product_Name_Length'] = df['Product'].astype(str).apply(len) 
df = df.dropna(subset=['Product_Name_Length', 'Amount']) 
plt.figure(figsize=(8, 5)) 
plt.hist(df['Product_Name_Length'], bins=15) 
plt.title("Distribution of Product Name Length") 
plt.xlabel("Number of Characters in Product Name") 
plt.ylabel("Frequency") 
plt.tight_layout() 
plt.show() 
plt.figure(figsize=(8, 5)) 
plt.scatter(df['Product_Name_Length'], df['Amount']) 
plt.title("Product Name Length vs Sales Amount") 
plt.xlabel("Product Name Length") 
plt.ylabel("Sales Amount") 
plt.tight_layout() 
plt.show() 
import pandas as pd 
print("\n
🔹
 TECHNIQUE 19: Most sold products analysis") 
top_products = df['Product'].value_counts().head(10) 
print("Top 10 most sold products:") 
print(top_products) 
print() 
import pandas as pd 
df = pd.read_csv(r"C:\Users\Ganesh\Downloads\Chocolate Sales (2) (1).csv") 
product_encoded = pd.get_dummies(df['Product'], prefix='Product') 
df_encoded = pd.concat([df, product_encoded], axis=1) 
print(df_encoded.head()) 