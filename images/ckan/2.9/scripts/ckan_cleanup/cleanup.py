import sqlalchemy as db 
import argparse

parser = argparse.ArgumentParser(
                    prog='Ckan Cleanup',
                    description='Cleans up resources from ckan database and deletes them',
                    epilog='Created by Kiril Poposki')

parser.add_argument('hostname')
parser.add_argument('-u', '--user',required=True)
parser.add_argument('-p', '--password',required=True)
parser.add_argument('-d', '--database',required=True)
parser.add_argument('-o', '--output',default="inactive_resources.txt")

args = parser.parse_args()

username = args.user
password = args.password
database = args.database
ip = args.hostname
output_file = args.output

db_url = f'postgresql+psycopg2://{username}:{password}@{ip}:5432/{database}'

engine = db.create_engine(url=db_url)
connection = engine.connect()
print("Connected to database")

query_string = db.text('SELECT * FROM resource')
print("Fetching resources")
query = connection.execute(query_string).fetchall()
inactive_resources = list()
for resource in query:
    if resource[6] != 'active':
        inactive_resources.append(f'{resource[20]}:{resource[0]}')

with open(output_file,"w") as f:
    print("Dumping to file")
    tabs = '\t'*9
    f.writelines(f"dataset{tabs}resource\n")
    for resource in inactive_resources:
        dataset,resource = resource.split(":")
        f.writelines(f'{dataset}\t{resource}\n')