#coding:utf-8

import os
import codecs

def ReadFile(filePath, encoding):
    with codecs.open(filePath, "r", encoding=encoding) as f:
        return f.read()

def WriteFile(filePath, content, encoding):
    with codecs.open(filePath, "w", encoding=encoding) as f:
        f.write(content)

def UTF8_to_GBK(src, dst):
    content = ReadFile(src, encoding="utf-8")
    WriteFile(dst, content, "gbk")

if __name__ == '__main__':
	UTF8_to_GBK("XXX","XXX")