## Environment Setup

### Python

Required Python packages:

- numpy
- pandas
- cython
- sqlalchemy
- pymysql
- quandl
- ta-lib (requires underlying C++ package)
- plotly
- rpy2 (maybe)
- quantlib (maybe, requires underlying C++ package)

Make sure `jTrade/jTrade` is added to python package search path. That is, `Data`, `Core` and other modules can be 
directly imported. This is important!

### Developer

Get credentials for:

- mysql server (RDS)
- linux server (EC2)
- online data vendors

### Server

Remember to put additional ip rules.