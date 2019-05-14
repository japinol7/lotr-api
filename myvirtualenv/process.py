import csv as csv
import pandas as pd
import json as json
from pymongo.errors import BulkWriteError
import uuid
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
mydb = client["lotr"]
mycol = mydb["characters"]

# db = client['lotr']
# collection = db.movies
# print (collection)

# csv_input = pd.read_csv('LOTR-API-characters.csv')
# csv_input['birth'] = ''
# csv_input['death'] = ''
# csv_input['gender'] = ''
# csv_input['hair'] = ''
# csv_input['height'] = ''
# csv_input['realm'] = ''
# csv_input['spouse'] = ''
# csv_input.to_csv('output.csv', index=False)

with open('bk/LOTR-API-characters.csv') as csvfile:
    reader = pd.read_csv(csvfile)
    allNames = []
    df = pd.DataFrame(reader)
    for idx, j in df.iterrows():
        print(j[1])
        allNames.extend([j[1]])
    print(allNames)
#         # print(row)
#         name = j[1]
#         birth = j[0]  # still unset
#         print(name)
with open('bk/LOTR-API-characters-more.csv') as csvfile2:
    reader3 = pd.read_csv(csvfile2)
#             # print(reader3)
    df2 = pd.DataFrame(reader3)
    name = []
    birth = []
    gender = []
    death = []
    hair = []
    height = []
    realm = []
    race = []
    spouse = []
    counter = 0
    for idy, k in df2.iterrows():
        if (k[5] not in allNames):
            counter = counter + 1
            birth.extend([k[0] or " "])
            death.extend([k[1] or " "])
            gender.extend([k[2] or " "])
            hair.extend([k[3] or " "])
            height.extend([k[4] or " "])
            name.extend([k[5] or " "])
            race.extend([k[6] or " "])
            realm.extend([k[7] or " "])
            spouse.extend([k[8] or " "])
            df = pd.DataFrame({'birth': birth, 'death': death, 'gender': gender,
                               'hair': hair, 'height': height, 'Name': name, 'Race': race, 'realm': realm, 'spouse': spouse})
            
            #df.columns = df.columns.map(str)
            #records = json.loads(df.to_json(orient='records'))
            # print(records)
            # data = df.to_dict('r')
try:
    print(counter)
    #print(df)
                # print(data)
    mycol.insert_many(df.to_dict('records'))
except BulkWriteError as bwe:
    print(bwe.details)

#                 # print(j)
#                 if name == k[5]:
#                     print("match")
#                 else:
#                     if '_id' in k:
#                         del k['_id']
#                     df = pd.DataFrame(k)
#                     print(df)
#                     df.columns = df.columns.map(str)

#                     # df.loc[idy, '_id'] = str(uuid.uuid4())
#                     data = df.to_dict(orient='records')
#                     try:
#                         mycol.insert_many(data)
#                     except BulkWriteError as bwe:
#                         print(bwe.details)
#     # you can also take this component and do more analysis
#     #werrors = bwe.details['writeErrors']
#                         raise
    #x = mycol.insert_one(k)

    # print('match')
    # df.loc[idx, 'birth'] = k[0]
    # df.loc[idx, 'death'] = k[1]
    # df.loc[idx, 'gender'] = k[2]
    # df.loc[idx, 'hair'] = k[3]
    # df.loc[idx, 'height'] = k[4]
    # df.loc[idx, 'race'] = k[6]
    # df.loc[idx, 'realm'] = k[7]
    # df.loc[idx, 'spouse'] = k[8]
    # break

    # df.to_csv('out.csv')
    # reader2 = csv.reader(csvfile2)
    # lines = list(reader2)
    # print(lines)
    # for row2 in reader3:
    # print(row2)
    # print(index)
    # if name == row2[5]:
    # lines[index]
    # print('match')
    # row2[0] = birth


# with open('LOTR-API-characters-more.csv', newline='') as csvfile:
    # print(sum(1 for row in csvfile))
#     spamreader = csv.reader(csvfile, quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
