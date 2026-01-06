import pandas as pd

# Load the data properly
BF_final_df = pd.read_csv('BF_final.csv')
# Assuming you have an SP500 equivalent file - let me check what files you have
print("Available CSV files with 'SP500' in name:")
import os
sp500_files = [f for f in os.listdir('.') if 'SP500' in f and f.endswith('.csv')]
print(sp500_files)

# Convert date column to datetime
BF_final_df['date'] = pd.to_datetime(BF_final_df['date'])

# Get unique dates from the data
dates = BF_final_df['date'].unique()
print(f"Available dates in BF_final_df: {len(dates)}")
print(f"First few dates: {dates[:5]}")

# Check if sp_final_df exists - you might need to load it
try:
    # Try to load SP500 data - adjust filename as needed
    sp_final_df = pd.read_csv('SP500_quarterly_data.csv')  # or whatever your SP500 file is called
    sp_final_df['date'] = pd.to_datetime(sp_final_df['date'])
    print(f"SP500 data loaded successfully with {len(sp_final_df)} rows")
except FileNotFoundError as e:
    print(f"SP500 file not found: {e}")
    # Create empty dataframe with same structure
    sp_final_df = pd.DataFrame(columns=BF_final_df.columns)

# Now create snapshots
snapshots = {}
for date in dates:
    temp_BF = BF_final_df[BF_final_df["date"] == date]
    temp_SP = sp_final_df[sp_final_df["date"] == date] if len(sp_final_df) > 0 else pd.DataFrame()
    
    if not temp_BF.empty or not temp_SP.empty:
        temp_merge = temp_BF.merge(temp_SP, how="outer", on="date")
        snapshots[date] = temp_merge

print("Snapshots created:")
print({k: v.shape for k, v in snapshots.items()})

# Debug information
print(f"\nDebug info:")
print(f"BF_final_df shape: {BF_final_df.shape}")
print(f"sp_final_df shape: {sp_final_df.shape if 'sp_final_df' in locals() else 'Not loaded'}")
print(f"Number of unique dates: {len(dates)}")
print(f"Number of snapshots created: {len(snapshots)}")