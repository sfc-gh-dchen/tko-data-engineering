#------------------------------------------------------------------------------
# Hands-On Lab: Data Engineering with Snowpark
# Script:       05_fahrenheit_to_celsius_udf/app.py
# Author:       Jeremiah Hansen, Caleb Baechtold
# Last Updated: 1/9/2023
#------------------------------------------------------------------------------

# SNOWFLAKE ADVANTAGE: Snowpark Python programmability
# SNOWFLAKE ADVANTAGE: Python UDFs (with third-party packages)
# SNOWFLAKE ADVANTAGE: SnowCLI (PuPr)

import sys
from scipy.constants import convert_temperature #Comment this out later - part of step 10

def main(temp_f: float) -> float:
    # return (float(temp_f) - 32) * (5/9) #initial run of step 5. Commented out during step 10.
    # Extra comment
    # 7-26-2023 DChen
    return convert_temperature(float(temp_f), 'F', 'C') #Comment this out later - part of step 10


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore






