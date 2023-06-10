#!/usr/bin/env python3
#################################################################
## Author: Joachim Elen
## Date: 2023-06-10
## 
## Purpose: Convert Nagios Core object files to excel
## License: GNU GPLv2
#################################################################
import sys
import xlwt
import time
import os

# get every object from a cfg file
def get_objects(lines):
    file = open(filename,'r')
    lines = file.readlines()
    type = ""
    objects = []
    inobject = False
    for line in lines:
        line = line.strip()       
        if len(line) > 0:
            if inobject == False:
                if line.startswith('define') and line.endswith('{'):
                    inobject = True
                    object = {}
                    line = line[6:].strip()
                    line = line[:-1].strip()
                    object['type'] = line
            
                #elif line.startswith('#'):
                #    object = {}
                #    object['type'] = line
                #    objects.append(object)
            else:
                if line.startswith('}'):
                    inobject = False
                    objects.append(object)
                else:
                    type = line.split()[0]
                    object[type] = line[len(type):].strip()
    return objects
            
def get_keys(objects):
    keys = []
    for object in objects:
        for key in object.keys():
            if key not in keys:
                keys.append(key)
    return keys

def create_sheet(workbook, sheetname, objects):
    worksheet = workbook.add_sheet(sheetname)
    keys = get_keys(objects)
    col = 0
    row = 0
    # generate headers
    for key in keys:
        worksheet.write(0,col,key)
        col = col + 1
    row = row + 1

    # generate rows
    for object in objects:
        for key, val in object.items():
            c = keys.index(key)
            worksheet.write(row,c,val)
        row = row + 1


if len(sys.argv) != 2:
    print("error, no output filename found")
    sys.exit()

excelfile = sys.argv[1]

dir_path = '.'
config_files = []
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path,path)):
        if path[-4:] == '.cfg':
            config_files.append(path)

workbook = xlwt.Workbook()

for config_file in config_files:
    sheetname = config_file[:-4]
    filename = os.path.join(dir_path,config_file)
    objects = get_objects(filename)
    create_sheet(workbook, sheetname, objects)

workbook.save(excelfile)
            
