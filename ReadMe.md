Stock-Market application
Code Overview:
The 2 main folders are rc and test. 'src' contains the source code which is further divided into 2 sub folders Stock and Trade, each containing files needed for Data access, class creation for that specific component.
All the methods required to be implemented are present in the "Market.py" file in src.

The test folder contains "MarketTest.py" which contains sample test cases implemented to test the functionality.

Assumptions:
1) For a given stock, fixed dividend & par value cannot be null
2) All calculated values are rounded off upto 4 decimals
3) Volume Weighted Stock Price(VWSP) and GBCE are assumed to be 0 by default if required data is not present
4) No time interval of 5 mins is used while calculating the VWSP for GBCE