# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"需要从供应商，在中国市场的研究，或者你在国外的下一个假期的web形式转换非英语电子邮件？")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)
