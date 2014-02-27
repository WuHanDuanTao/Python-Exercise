from sys import argv

script, filename = argv

txt = open (filename) # open txt

print "Here's your file %r:" % filename
print txt.read() # 执行read 命令 然后打印出来

print "Type the filename again:"
file_again = raw_input ("> ") # 将文件名赋值给file_again变量

txt_again = open (file_again) # 再次打开这个文件 并且赋值给txt_again变量

print txt_again.read() # 执行read 命令 然后打印出来
