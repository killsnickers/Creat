# -*- encoding: utf-8 -*-

import re
import json
import codecs
import os

def parse(path, out_file):
    default_keys = [1, 2, 3, 19, 29, 9, 15, 16, 43]
    result = {}
    files = filter(lambda filename: filename.lower().endswith((u'.txt')), os.listdir(path))
    for file in files:
        standard_json = json.load(open(os.path.join(path, file), 'r'))
        region_item = {}
        for region in standard_json.get(u'regions', []):
            region_item[region[u'cls']] = { u'standard': region[u'result'][0] }

        for key in default_keys:
            if not region_item.get(key):
                region_item[key] = { u'standard': '' }

        result[re.sub(r'\.txt|\.TXT', '.jpeg', file)] = region_item

    json.dump(result, codecs.open(out_file, 'w', encoding='utf-8'), skipkeys=True, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    path = 'D:\\workplace\\test_data\\482825f2_road_roll\\482825f2_train\\10507'
    out_file = 'C:/Users/User/Desktop/HZP_scripts/toll/data/standard_result.json'
    parse(path, out_file)
