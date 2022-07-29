# file = open('test.txt', 'rt')
# # content = file.read()
# # print(content)
#
# for line in file:
#     print(line)
#
# file.close()

with open('test.txt', 'rt') as file:
    for line in file:
        print(line)

