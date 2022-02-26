import json
import re
periodic_table = json.load(open('periodic_table.json'))
file1 = "import_file_3.txt"
file2 = "output_file.txt"

with open(file1, "r") as fr1, open(file2, 'w') as fw:
    for line1 in fr1:
        split = re.findall('[A-Z][^A-Z]*', line1)
        for i in split:
            fw.write(periodic_table.get(i))
