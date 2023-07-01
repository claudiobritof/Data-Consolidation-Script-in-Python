# Data-Consolidation-Script-in-Python
 &ensp; This repository contains a Python script for manipulating data from a MySQL remote database table and consolidating it into another MySQL table. The script utilizes the mysql.connector library for database connectivity and the pandas library for data manipulation.  
 
 &ensp; *Please take note that specifically this script is provided as a demonstration. To access the database you may need to have your IP authorized, but for privacy reasons, I will not publish it here the e-mail address to apply and I cannot guarantee that the permission will work anymore. I’m keeping this code here almost as a "read-only".  

<b> Prerequisites:</b>  
 1.	Python 3.x installed
 2.	MySQL Connector/Python library installed (pip install mysql-connector-python)
 3.	Pandas library installed (pip install pandas)
 4.	Access to remote database:  
<pre>
  -	Database: a4f2b49a_sample_database  
  -	Host:40b8f30251.nxcli.io  
  -     User: a4f2b49a_padawan  
  -	Password: KaratFlanksUgliedSpinal  
  -	Port: 3306  
</pre>
 
<b>Setup:</b>  
1.	Clone the repository to your local machine or download the script directly.  
2.	Open the script file in your preferred text editor or integrated development environment (IDE).  
3.	Modify the database connection parameters to match your MySQL database configuration.  

<b>Usage:</b>  
1.	Run the script using a Python interpreter.
2.	The script will establish a connection to the specified MySQL database to read and fetch all the data from the "raw_data" table.
3.	It will create a new table named "consolidated_data" to store the consolidated data. If the table already exists, it will be dropped before creating a new one to avoid duplication.
4.	The script will consolidate the data by month, performing various calculations on the fetched data. The consolidated data will be stored in a pandas DataFrame.
5.	The consolidated data will be inserted into the "dados_consolidados" table row by row.
6.	The changes will be committed to the database, and the connection will be closed.

Necessary data for this exercise is located on “raw_data” table, which contains these columns: 
access_datetime: timestamp when the player executed the action.
modality: type of game (could be Cash Game or Tournament).
