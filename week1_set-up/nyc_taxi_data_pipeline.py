import sys
import pandas as pd 

print(sys.argv)
date = sys.argv[1]
version = pd.__version__

print(f'job finished successfully for day = {date}')
print(f'you are using this version of pandas: {version}')