import sys
import platform
import datetime

# Print system information
print("Python Version:", sys.version)
print("Platform:", platform.platform())
print("Current Time:", datetime.datetime.now())
print("\nEnvironment is working correctly!")

# Try importing some libraries that should be installed
try:
    import numpy as np
    import pandas as pd
    print("\nNumPy version:", np.__version__)
    print("Pandas version:", pd.__version__)
    
    # Create a simple array and perform an operation
    arr = np.array([1, 2, 3, 4, 5])
    print("\nSample NumPy array:", arr)
    print("Mean value:", np.mean(arr))
    
    # Create a simple DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    print("\nSample DataFrame:")
    print(df)
    print("\nDataFrame description:")
    print(df.describe())
    
    print("\nLibraries imported successfully!")
except ImportError as e:
    print(f"\nError importing libraries: {e}")
    print("Please make sure all required libraries are installed.")