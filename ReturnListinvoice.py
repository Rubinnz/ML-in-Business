import pandas as pd

def find_and_sort_orders(df, min_value, max_value, sort_type=True):
    # Calculate total value for each order
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='Sum')  # Rename the aggregated column to 'Sum'

    # Filter orders within the specified range
    filtered_orders = order_totals[
        (order_totals['Sum'] >= min_value) & (order_totals['Sum'] <= max_value)
    ]

    # Sort the orders based on the `sort_type`
    sorted_orders = filtered_orders.sort_values(by='Sum', ascending=sort_type)

    return sorted_orders

# Example usage
if __name__ == "__main__":
    # Load the data
    df = pd.read_csv('Dataset/SalesTransactions.csv')

    # Get user input for min, max, and sorting type
    min_value = float(input("Nhập giá trị min: "))
    max_value = float(input("Nhập giá trị max: "))
    sort_type = input("Sắp xếp theo thứ tự tăng dần (True) hay giảm dần (False)? ").strip().lower() == 'true'

    # Get the result
    result = find_and_sort_orders(df, min_value, max_value, sort_type)

    # Display the result
    print("Danh sách các hóa đơn trong phạm vi giá trị:")
    print(result)