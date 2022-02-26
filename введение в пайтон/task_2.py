with open("input_file.txt", "r") as fr , open("output_file.txt", 'w') as fw:
    for line in fr:
        str1 = line.split(' ')
        eva_str = str1[1] + str1[0] + str1[2]
        fw.write(str(eval(eva_str))+',')
        size = fw.tell()
    fw.truncate(size-1)
