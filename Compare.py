# -*- encoding: utf-8 -*-

import json
import requests
import os
import codecs
import re

import xlwt

def getfixedregion(receiptData, cls_num):
    fixedregions = receiptData.get(u'fixedregions')
    if not fixedregions:
        return ''

    for region in fixedregions:
        if region[u'cls'] == cls_num:
            return region.get(u'result', '')

    return ''

def request(url, image_path):
    files = {}

    with open(image_path, "rb") as f:
        response = requests.post(url, data=f)
        return response.json()

    return {}

def getStandard(url):
    with open(url, 'r') as f:
        content = f.read()
        content = json.loads(content)
        content = content[u'regions']
        #flag = 0
        for con in content:
            if (con[u'cls'] == 9):
                return con[u'result']
        return ''

def compare(url, dir_path):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('test', cell_overwrite_ok=True)
    sheet.write(0, 0, 'FileName')
    sheet.write(0, 1, 'right')
    sheet.write(0, 2, 'Fixed')
    #sheet.write(0, 1, 'date')
    #standard_result = json.load(codecs.open(standard_result_path, 'r', encoding='utf-8'))
    #filename = []
    #values = []
    images = filter(lambda name: name.lower().endswith(('.jpeg', '.jpg', '.png')), os.listdir(dir_path))
    #code_false_count = 0
    num = 0
    success_num = 0
    for image in images:
        num += 1
        sheet.write(num, 0, image.split('.')[0]+'.'+image.split('.')[1])
        result_standard = getStandard(dir_path+image.split('.')[0]+'.'+image.split('.')[1]+'.txt')
        sheet.write(num, 1, result_standard)
        receiptData = request(url, os.path.join(dir_path, image))
        '''if receiptData.has_key(u'regions'):
            for res in receiptData[u'regions']:
                if res[u'cls'] == 15:
                    filename.append(image.split('.'))
                    values.append(res[u'result'])
                    break'''
        result_fixed = getfixedregion(receiptData, 9)
        sheet.write(num, 2, result_fixed)
        if result_fixed == result_standard:
            success_num += 1
    '''book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('test', cell_overwrite_ok=True)
    sheet.write(0, 0, 'Name')
    sheet.write(0, 1, 'date')
    n = 1
    for fi in filename:
        sheet.write(n, 0, fi)
        n = n + 1
    n = 1
    for con in values:
        sheet.write(n, 1, con) 
        n = n + 1'''
    print success_num
    book.save(dir_path + '/compare9.xls')
        # code
        # fixed_code = getfixedregion(receiptData, 1)
        # standard_result[image]['1']['fixed'] = fixed_code
        # standard_result[image]['1']['equals'] = fixed_code == standard_result[image]['1']['standard']
        #is_equals = parse_result(standard_result, receiptData, '1', image)
        #code_false_count += int(is_equals)

    #standard_result['accuracy_code'] = float(code_false_count) / len(images)

    #json.dump(standard_result, codecs.open(out_result_path, 'w', encoding='utf-8'), skipkeys=True, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    url = 'http://10.35.11.14:5009'
    dir_name = os.getcwd()
    #print dir_name
    image_path = dir_name+'/10505/'
    #standard_result_path = 'C:/Users/User/Desktop/HZP_scripts/toll/data/standard_result.json'
    #out_result_path = 'C:/Users/User/Desktop/HZP_scripts/toll/data/compare_result.json'
    #compare(url, image_path, standard_result_path, out_result_path)
    #compare(url, image_path)
    #print getStandard(image_path+'DH00117045445_190.00.txt')
    compare(url, image_path)
    #print