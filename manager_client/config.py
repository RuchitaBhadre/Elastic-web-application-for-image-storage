import os
password = os.getenv("MYSQL_PASSWORD")
db_config = {'user': 'admin',
             'password': password,
             'host': 'database-2.cabadqcqayd0.us-east-1.rds.amazonaws.com',
             'port': '3306',
             'database': 'ImageStore'}
#
max_capacity = 2
replacement_policy = 'Least Recently Used'
