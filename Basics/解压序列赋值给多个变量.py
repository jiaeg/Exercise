# 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
# 如果变量个数和序列元素的个数不匹配，会产生一个异常。
# 不想赋值的参数可以使用 _ 作为占位符将之丢弃。
# 
# 这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。
# 包括字符串，文件对象，迭代器和生成器。 

variate = [123, 'qaz', 'wsx', 'edc', (789, 897, 978)]
var1, var2, var3, var4, var5 = variate
print(var1, var2, var3, var4, var5)

a, b, _ = var5
print(a, b)

e, d, c, r, f = 'Hello'
print(e, d, c, r, f)