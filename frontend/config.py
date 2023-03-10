import os, requests, json
#resp = requests.get("http://169.254.169.254/latest/user-data/")
#conf_dict = json.loads(resp.content.decode('utf-8'))

conf_dict={
    "MYSQL_USER": "admin",
    "MYSQL_PASSWORD":"a2cloudruchisneha",
    "MYSQL_HOST":"database-2.cabadqcqayd0.us-east-1.rds.amazonaws.com",
    "aws_access_key_id":"AKIARQKRVO4S26T5MJKW",
    "aws_secret_access_key":"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"
}

db_config = {'user': conf_dict["MYSQL_USER"],
             'password': conf_dict["MYSQL_PASSWORD"],
             'host': conf_dict["MYSQL_HOST"],
             'port': '3306',
             'database': 'ImageStore'}

aws_config = {
    'aws_access_key_id': conf_dict['aws_access_key_id'],
    'aws_secret_access_key': conf_dict['aws_secret_access_key']
}

max_capacity = 2
replacement_policy = 'Least Recently Used'

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + 'main/frontend/static/images'
