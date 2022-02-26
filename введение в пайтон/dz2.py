file1 = "import_file_2_1.txt"
file2 = "import_file_2_2.txt"
file3 = "output_file.txt"
with open(file1, "r") as fr1, open(file2, 'r') as fr2, open(file3, 'w') as fw:
    for line1 in fr1:
        line2 = fr2.readline()
        coord = line2.split(' ')
        letter = line1[ int(coord[0]): int(coord[1])+1 ]
        print(letter)
        fw.write(letter+' ')
        size = fw.tell()
    fw.truncate(size-1)
