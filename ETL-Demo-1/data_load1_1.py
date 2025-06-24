import pandas as pd


# define the load_data Function

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV data into a DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()
    

# Call the Function with Your Path
df = load_data(r"/Applications/Ramos/Coding Repo/ETL Project/Python'25/Python-Case-Studies/ETL-Demo-1/sample_customers.csv")
df.head()
print(df.columns)


# Convert Data Types

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert Columns data types to appropriate formats.
    """
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['purchase_amount'] = pd.to_numeric(df['purchase_amount'], errors='coerce')
    
    print("✅ Data types converted.")
    return df

df = convert_data_types(df)
df.dtypes