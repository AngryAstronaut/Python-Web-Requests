import requests
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTZjusfWgTiXGVSUeApaJmHVUDt9907vgteCyQi9UwUwozJIZDXKx9O0hCkK7JVxBa_w-Qzxc0j3tkL/pub?gid=0&single=true&output=csv"
r = requests.get(url)
# print(r.text)
p = r.text.replace('\r\n', ',')
m = p.split(',')
# print(str(r.status_code))

headers = m[:4]
print(headers)

Serial = m[4::4]
Name = m[5::4]
Asset = m[6::4]
Building = m[7::4]

num = len(Serial)
for i in range(num):
    print(Serial[i], Name[i], Asset[i], Building[i])


# curl -X GET 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTZjusfWgTiXGVSUeApaJmHVUDt9907vgteCyQi9UwUwozJIZDXKx9O0hCkK7JVxBa_w-Qzxc0j3tkL/pub?gid=0&single=true&output=csv'

#
# try:
#     f = m
#     reader = csv.DictReader(f, fieldnames=['Serial', 'Name', 'Asset', 'Building'])
#     next(reader)
#     for row in reader:
#         serial = row['Serial']
#         name = row['Name']
#         asset = row['Asset']
#         building = row['Building']
#         print(serial)
#         print(name)
#         print(asset)
#         print(building)
# except:
#     print("No CSV To Open... ")
#     # print("Manual Entry: ")
#     # m = input("Enter iPad Asset Here: ")
#     # print(m)
#
