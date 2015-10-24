#Learn-Python
This is my Python demo

##关于编码
==

[TOC]

>本来只是准备简单的写一写，结果发现越写越多。

正好最近在知乎看到一道题目，中国的程序员与美国的程序员的差别在哪里，其他的方面不敢说，在字符编码这个问题上，估计大部分的中国程序员都遇到过，而且肯定认知比美国的程序员更深刻。。。  

这里相关的程序运行背景也有必要先说明一下。  
- Python2.7
- sublime_text 2 有时候也在cmd中执行
- Windows 10

##几点基础知识
- 编码格式有ASCII，GBK，gb2312，UTF-8，Unicode，，GB18030在MySQL里还有utf8，在Windows下还有cp936。其中，除了ASCII，其他都是能够显示中文的，只不过兼容或者不兼容的问题。  
>- Unicode是一种字符集，它为古代或现代使用的文字系统中出现的每一个字符都提供了统一的序列号，规定了符号的二进制代码，但没有规定这个二进制代码该如何存储。也就是说，Unicode的编码方式是固定的，但是实现方式根据需要有很多种，常见的有UTF-8，UTF-16和UTF-32等。
>- gb2312是中国政府在1980年颁布的，共收录汉字7445个，支持6763个汉字和682个其他字符。1995年汉字扩展规范GBK1.0收录了21886个符号，它分为汉字区和图形符号区，汉字包括21003个字符。2000年的GB18030是取代GBK1.0的正式国家标准。该标准收录了27484个汉字，同时还收录了藏文、蒙文、维吾尔文等主要的少数民族文字。
>- 从 ASCII、GB2312、GBK到GB18030，这些编码方法是向下兼容的，即同一个字符在这些方案中总是有相同的编码，后面的标准支持更多的字符。即在这些编码中，后面的编码格式支持前面的编码格式，但前面的编码格式不一定支持后面的编码格式。Unicode和UTF-8与这些编码格式完全不兼容。
>- Windows下中文的默认编码格式是cp936（code page 936），即GBK编码。若非要具体比较起来，GBK定义字符比cp936多出95个字符（80个汉字和15个其他字符）。但是在PHP下的mb_detect_encoding函数会识别为cp936。
>- Windows的笔记本在另保存的时候可以选择为ASCII，Unicode，Unicode big endian，UTF-8。但是这个UTF-8斌不是标准的UTF-8，而是带有BOM（Byte Order Mark）的UTF-8编码。所以一般都在编程的时候都不建议直接用笔记本，根本就不是标准的编辑器，还不说它的默认编码是ASCII。
>- utf-8的编码格式比GBK的编码格式实在好太多了，在Linux和Mac下默认的中文编码格式就是UTF-8，而且全世界通用，强烈建议在任何情况下都将其他的编码格式转化为UTF-8。
>- python的'\'一般表示转义字符，所以用'\\'表示一个正常'\'，这种形式在Python的正则表达式里面经常遇到，所以在这个时候就可以在字符串之前加上'r'，表示'raw'原生字符串，不具有任何转义意义。同样的道理，在字符串之前加上'u'，表示这是一个以Unicode形式输入的字符串。
- Python 2.X 的版本与Python 3.X的版本差别有很多。其中有一点就是Python 2.X默认编码ASCII ， 而Python 3.X默认编码UTF-8。  
>你可以使用如下代码来查看验证这一点。
>```python
>import sys
>sys.getdefaultencoding()
>```
- 但是在Python代码中做编码转换的时候，却需要先将其他的编码格式解码(decode)为Unicode，再从Unicode编码(encode)为另一种格式，不能直接在两种不同的编码格式之间转换，比如说GBK和UTF-8。   
>- decode作用是将其他编码格式的字符串解码为Unicode编码，比如`str.decode('gb2312')`是指将gb2312编码的字符串转化为Unicode编码。
>- encode作用是将Unicode编码的字符编码为其他编码格式，比如`str.encode('utf-8')`是指将Unicode编码的字符串转化为utf-8编码。
>- Unicode(str,defaultcode)，就是指定写入的格式为defaultcode，这样才在Python中正确的保存为为Unicode编码格式。同`str.decode("utf-8")`。
- 因为Python 2.X的默认编码格式是ASCII，那么在没有指定Python源码编码格式的情况下，源码中所有字符都会被默认 为ASCII码。
- sublime_text中默认的编码和输出格式是utf-8，而且不能正确识别GBK编码的中文，如果需要能够识别GBK编码的中文，需要安装GBK Encoding Support 插件，但是即便如此，在打开GBK格式编码的中文文件时，sublime会自动生成一个dump文件，文件修改过程中，不会修改原文件，只有按"保存"了才会将dump的数据更新到原文件里，关闭当前编辑的dump文件则会自动删除dump文件。
- isinstance()。功能有很多。
>- 判断一个对象是不是列表`isinstance(SomeThing,list)`
>- 判断一个对象是不是字符串`isinstance(SomeThing,basestring)`
>- 判断一个字符串是不是Unicode字符串`isinstance(SomeThing,unicode)`

##常见的编码错误
- SyntaxError: Non-ASCII character   
这种异常最不容易出现，也最容易处理，主要原因是Python源码文件中有非ASCII字符，而且同时没有声明源码编码格式,如：
```python
S = "中文"
print S
```
即会抛出语法错误，有非ASCII字符在代码中出现，但是没有设定编码方式。这个错误在文件中sublime_text中写好代码后，无论是用sublime_text执行还是用cmd执行都会报这个错。   
`SyntaxError: Non-ASCII character '\xe4' in file C:\Users\dell\.ssh\Python_Lib\Chinese_decode.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
`   
**解决方法：**在代码头声明编码格式。
```python
#coding=utf-8
#或者这样写也可以
# -*- coding: utf-8 -*-
S = "中文"
print S
```
这样在sublime_text中即能够正确显示，但是在cmd中能够显示出来，只不过是乱码。
![Chinese_decode_1.jpg](Chinese_decode_1.jpg)   
![Chinese_decode_2.jpg](Chinese_decode_2.jpg)   
这是因为在Windows下中文的默认编码格式为cp936，所以即使我们设定了编码格式为UTF-8，utf-8编码格式的中文也不能再cp936格式下正常显示。可以在cmd中输入`chcp`来查看当前字符集编码格式，使用`chcp 65001`来将Windows默认中文编码格式临时改为UTF-8。
但是在这里我再次尝试时出现了问题。  
![Chinese_decode_3.jpg](Chinese_decode_3.jpg)
这是为什么呢？找不到这个文件？看来还是文件编码不对，在sublime中将这个代码文件的编码格式改为GBK再试试。
![Chinese_decode_4.jpg](Chinese_decode_4.jpg)
虽然找到了，但是这回字符又找不到了。将Windows的默认编码格式换回去。
![Chinese_decode_5.jpg](Chinese_decode_5.jpg)
这是什么情况，虽然这样可以看到了，但是因为编码格式不是UTF-8，在sublime中不是编辑代码源文件了，而是dump的临时文件，这样看起来非常的不舒服。那我们再换回去。然而换回去的话，在cmd中显示的图片就和我们一开始在cmd中看到的乱码一样了，这样要怎么解决呢？   
还有，有时候或许是在Python代码的注释中混有中文，效果也是和以上一样。
- UnicodeDecodeError   
这个异常有时候会在调用decode方法时出现，原因是Python打算将其他编码的字符转化为Unicode编码，但是字符本身的编码格式和decode方法传入的编码格式不一致
```python
#coding=utf-8
S = "中文"
S.decode("gbk")
#或者是这样
#s.encode('gbk')
print S
```
即会抛出错误，在sublime和cmd中都会出现。   
`UnicodeDecodeError: 'gbk' codec can't decode bytes in position 2-3: illegal multibyte sequence`   
**解决办法：**认准你的字符编码格式。我觉得应该不会有人犯这种低级明显的错误吧。
- UnicodeEncodeError   
错误的使用decode和encode方法会出现这种异常，比如：使用decode方法将Unicode字符串转化的时候。
```python
#coding=utf-8
S = u"中文"
print S
```
即会抛出错误，在sublime中报错，但是在cmd中正常显示了。
`
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
`
错误上写清楚了是ASCII编码无法解码，因为Unicode编码毫无疑问是多于128个的。但是在cmd中正常显示了，说明在cmd中输出的时候，Windows进行了自动转码为GBK，就可以正确显示。
**解决办法：**将字符串编码为其他格式输出即可
```python
#coding=utf-8
S = u"中文"
print S.encode("utf-8")
```
在使用这样的代码之后，在sublime中可以正常显示了，但是在cmd中还是乱码，cp936与UTF-8的不兼容。


##衷心的建议
- 只要你的代码里出现了中文，请一定在代码头加上代码的编码格式`#coding=utf-8`。
- 尽可能使用UTF-8的编码，无论何时何地，并牢记这一点。
- 使用`u"中文"`代替`"中文"`，这样的话，你载需要使用的时候可以直接对字符串进行操作，或者用它打开文件。当你需要把它输出的时候，不要忘记了给它一个编码方式。
- 重置Python的默认编码格式,需要重新加载一次sys模块。
```python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```
- decode early, unicode everywhere, encode late 。即在输入字符串之后就将它转码为Unicode编码格式，然后就可以在按需对其进行操作了，最后，在输出的时候，不要忘了给它一个编码格式。
- 升级Python 2.X到Python 3.X 。Python 3.X的改进有一下几点。
>- 默认编码格式改为unicode
>- 所有的Python内置模块都支持unicode
>- 不再支持u'中文'的语法格式
- 或者有一个Python模块codecs，可以使用这个来进行编码和解码，当然前提是你还是得要了解当前的编码相关的一些基础知识。


##一些小测试


##参考链接
[Python的中文编码问题](http://segmentfault.com/a/1190000002412924)   
[Python 设置系统默认编码](http://shirley-ren.iteye.com/blog/1018750)   
[设置python的默认编码为utf8](http://blog.csdn.net/lgy807720302/article/details/7515743)   
[ 字符集编码cp936、ANSI、UNICODE、UTF-8、GB2312、GBK、GB18030、DBCS、UCS](http://blog.csdn.net/wanghuiqi2008/article/details/8079071)
[字符集编码Unicode ,gb2312 cp936](http://www.xiaowanxue.com/up_files/201212717915.html)
[UTF-8、ISO 8859-1、GB、CP936……](http://kongxz.com/2010/03/utf8-iso8859-gb-cp936-etc/)
[CP936与GBK、GB2312、GB18030](http://blog.wuliaoa.com/?p=503)
[Windows代码页](http://blog.wuliaoa.com/?p=495)
[字符集编码Unicode ,gb2312 cp936](http://www.xiaowanxue.com/up_files/201212717915.html)
[程序员趣味读物：谈谈Unicode编码](http://pcedu.pconline.com.cn/empolder/gj/other/0505/616631.html)