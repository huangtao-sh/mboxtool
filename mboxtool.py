#!/bin/python3
import email
import mailbox
from argparse import ArgumentParser
import sys
from os import listdir,mkdir
from os.path import basename,isdir,isfile,splitext,join,exists

def decode(header):
    h=email.header.decode_header(header)
    s=[]
    for x in h:
        if isinstance(x[0],bytes):
            s.append(x[0].decode(x[1] if x[1] else 'ascii'))
        else:
            s.append(x[0])
    return ''.join(s)

def proc_file_name(file_name):
    ignore_char='/\*"<>|?'
    linux_len=0
    windows_len=0
    new_name=''
    for char in file_name:
        if not(char in ignore_char):
            linux_len+=len(char.encode('utf8'))
            windows_len+=len(char.encode('gbk'))
            if linux_len>255-4 or windows_len>255-4:
                break
            new_name=new_name+char
    return new_name

class Mailbox:
    
    def execute(self):
        if self.emails and self.mailbox:
            if self.importemail:
                self.import_email(self.emails,self.mailbox)
            else:
                self.export_email()
                
    def import_email(self,email_path,mailbox_path):
        dir_list=listdir(email_path)
        dirs=[]
        #将mailbox_file_name 修改为以mailbox_path为名
        base,ext=splitext(basename(mailbox_path))
        mailbox_file_name=join(mailbox_path,basename(mailbox_path))
        mb=mailbox.mbox(mailbox_file_name)
        mb.lock()
        for d in dir_list:
            f=join(email_path,d)
            if isdir(f):
                dirs.append(d)
            elif isfile(f) and splitext(f)[1]=='.eml':
                with open(f) as fn:
                    mb.add(fn)                    
                try:
                    print(splitext(f)[0])
                except:
                    pass

        mb.unlock()
        mb.close()
        if dirs:
            #将目标文件夹的ext带到下一个文件夹
            for d in dirs:
                m_path=join(mailbox_path,d+ext)
                if not exists(m_path):
                    mkdir(m_path)
                e_path=join(email_path,d)
                self.import_email(e_path,m_path)

    def export_email(self):
        pass

def proc_args(instance):
    parser=ArgumentParser(description='Mailbox 导入导出')
    parser.add_argument('-i','--importemail',action='store_true')
    parser.add_argument('-e',dest='emails')
    parser.add_argument('-m',dest='mailbox')
    parser.parse_args(sys.argv[1:],namespace=instance)

if __name__=='__main__':
    '''
    e=Mailbox()
    proc_args(e)
    e.execute()
    '''
    a=[
        '张三阿*"伯张三阿',
        'asfdasdfa<>/|||/?',]
    for x in a:
        print(proc_file_name(x))
