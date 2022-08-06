
with open("UII.csv") as file:
    data = file.read()

from_csv = data.split('\n')
for i in range(8):
    print(f"{i}: {from_csv[i]}")
# for i in range(5, len(data)):
#     print(data[i].strip().split(';'))
