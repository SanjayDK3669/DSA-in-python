'''
file = open(r"Normal.txt",'r')
print(file.name)
print(file.mode)
print(file.read())
file.close()
'''
#with open('Normal.txt', 'r') as file:
    # # for line in file:
    # #     print(line, end = "")
    
    # size_of_read = 10
    # file_content = file.read(size_of_read)
    # print(file_content, end = "")
    
    # file.seek(1)
    
    # file_content = file.read(size_of_read)
    # print(file_content) 

    # print(file.tell())
    
    # while len(file_content) > 0:
    #     print(file_content, end = " * ")
    #     file_content = file.read(size_of_read)
    
    # file_content = file.readline(100)
    # print(file_content, end = "")

# print(file.name)
# print(file.mode)
# print(file.closed)

""" with open("Normal2.txt",'w') as file:
    file.write("Test this is the my first read and write python program to handling")
    file.seek(1)
    file.write('HEllo programmer') """
    
with open("Normal.txt", 'r') as rf:
    with open("Normal_copy.txt", 'w') as wf:
        wf.write("This is the copy of Normal.txt \n")
        for line in rf:
            wf.write(line)