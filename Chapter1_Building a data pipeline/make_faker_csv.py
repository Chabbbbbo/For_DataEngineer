import csv
from faker import Faker

######### TEST #############
# output = open('My_csv.csv', mode = 'w')
# mywriter = csv.writer(output)

# header = ['name', 'age']
# mywriter.writerow(header)

# data = ['Chabbo', '31']
# mywriter.writerow(data)
# output.close()
############ 1000개 fake data 생성 ##############
output = open('data.csv', mode = 'w')
mywriter = csv.writer(output)
fake = Faker()
header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
mywriter.writerow(header)
for _ in range(1000):
    mywriter.writerow([fake.name(), fake.random_int(min = 18, max = 80, step=1), fake.street_address(), fake.city(), fake.zipcode(), 
    fake.longitude(), fake.latitude()])
output.close()

####### data 중 name 읽기 ##########
with open('data.csv') as f:
    myreader = csv.DictReader(f)
    headers = next(myreader)
    for row in myreader:
        print(row['name'])