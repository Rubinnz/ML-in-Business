import sqlite3
import pandas as pd

def get_customers_with_min_invoices(db_path, min_invoices):
    """
    Trả về danh sách các Customer có số lượng hóa đơn >= min_invoices.

    Args:
        db_path (str): Đường dẫn đến file cơ sở dữ liệu SQLite.
        min_invoices (int): Số lượng hóa đơn tối thiểu.

    Returns:
        DataFrame: DataFrame chứa danh sách Customer với số lượng hóa đơn >= min_invoices.
    """
    sqliteConnection = None
    try:
        # Kết nối đến cơ sở dữ liệu
        sqliteConnection = sqlite3.connect(db_path)
        query = f"""
        SELECT 
            Customer.CustomerId, 
            Customer.FirstName || ' ' || Customer.LastName AS CustomerName,
            COUNT(Invoice.InvoiceId) AS InvoiceCount
        FROM Customer
        JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId
        HAVING COUNT(Invoice.InvoiceId) >= {min_invoices};
        """
        # Thực thi câu truy vấn và chuyển kết quả thành DataFrame
        df = pd.read_sql_query(query, sqliteConnection)
        return df

    except sqlite3.Error as error:
        print('Error occurred -', error)
        return None

    finally:
        if sqliteConnection:
            sqliteConnection.close()

# Sử dụng hàm
database_path = '../databases/Chinook_Sqlite.sqlite'  # Đường dẫn tới cơ sở dữ liệu
min_invoice_count = 5  # Ví dụ: Lấy khách hàng có từ 5 hóa đơn trở lên
result_df = get_customers_with_min_invoices(database_path, min_invoice_count)

if result_df is not None:
    print(result_df)
