import pandas as pd

def sales_analysis(sales_table, product_table):
    result_df = pd.merge(sales_table, product_table, on='product_id')
    result_df = result_df[['product_name', 'year', 'price']]
    return result_df

# Sample data for Sales and Product tables
sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}

product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}

# Create DataFrames for Sales and Product tables
sales_df = pd.DataFrame(sales_data)
product_df = pd.DataFrame(product_data)

# Call the sales_analysis function
result_table = sales_analysis(sales_df, product_df)

# Display the result
print(result_table)
