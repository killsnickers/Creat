# -*- coding: utf-8 -*-
import os
import re
import sys
import json
import os
import xlwt
class sero():
    def tTe(self):
        import os
        dir_name = os.getcwd()
        path = "/10505/"
        itermss = []
        filenames = []
        contents = []
        iterms = os.listdir(dir_name+path)
        for it in iterms:
            if re.search(u'.txt', it):
                itermss.append(it)
        for itr in itermss:
            with open(dir_name+path+itr, 'r') as f:
                filename = itr[:itr.rfind(".")]
                filenames.append(filename)
                content = f.read()
                content = json.loads(content)
                content = content[u'regions']
                flag = 0
                for con in content:
                    if(con[u'cls']==15):
                        contents.append(con[u'result'])
                        flag = 1
                        break
                if not flag:
                    contents.append(u'')
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet('test', cell_overwrite_ok=True)
        sheet.write(0, 0, 'Name')
        sheet.write(0, 1, 'amount')
        n = 1
        for fi in filenames:
            sheet.write(n, 0, fi)
            n = n+1
        n = 1
        for con in contents:
            sheet.write(n, 1, con)
            n = n+1
        book.save(dir_name+'/test6.xls')


if __name__ == '__main__':
    se = sero()
    se.tTe()
