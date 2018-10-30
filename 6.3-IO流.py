import io
'''
IO是什么？
文件可以持久存储，但是现在类似于临时的一些文件，不需要持久存储，
如一些临时的二维码等，这个不需要持久存储，
但是却需要短时间内大量读取，这是时候还是只能保存在文件里面吗？
：放到内存中，效率高。
'''

# 字符串-IO
strio = io.StringIO()       # 创建IO
strio.write('帅气的鱼')     # 此时指针在末尾
# strio.seek(0)
a = strio.read()
print(a)
b = strio.getvalue()        # 不需要调节指针位置，可以直接获取
print(b)
strio.close()   # 关闭


# bytes-IO ——操作图片等其他类型文件
bio = io.BytesIO()     # 创建；其余方法同上
bio.write(b'abcd')       # 传入二进制类型；无法直接中文
c = bio.getvalue()
print(c)
bio.close()