#Learn-Python
This is my Python demo

>本来只是准备简单的写一写，结果发现越写越多。

##关于编码
正好最近在知乎看到一道题目，中国的程序员与美国的程序员的差别在哪里，其他的方面不敢说，在字符编码这个问题上，估计大部分的中国程序员都遇到过，而且肯定认知比美国的程序员更深刻。。。  

这里相关的程序运行背景也有必要先说明一下。
Python2.7
sublime_text 2 有时候也在cmd中执行
Windows 10

恩，编码格式有ASCII，GBK，gb2312，UTF-8，Unicode，在MySQL里还有utf8。其中，除了ASCII，其他都是能够显示中文的，只不过兼容或者不兼容的问题。  
Python 2.X 的版本与Python 3.X的版本差别有很多。  
其中有一点就是Python 2.X默认编码ASCII ， 而Python 3.X默认编码UTF-8。  
但是在Python代码中做编码转换的时候，却需要先将其他的编码格式解码(decode)为Unicode，再从Unicode编码(encode)为另一种格式，不能直接在两种不同的编码格式之间转换，比如说GBK和UTF-8。   
 - decode作用是将其他编码格式的字符串转化为Unicode编码，比如`str.decode('gb2312')`是指将gb2312编码的字符串转化为Unicode编码。
 - encode作用是将Unicode编码的字符串转化为其他编码格式，比如`str.encode('utf-8')`是指将Unicode编码的字符串转化为utf-8编码。
 - Unicode
