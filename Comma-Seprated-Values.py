#csv文件中的每行代表电子表格中的一行，逗号分割了该行中的单元格
#要用csv模块从CSV文件中读取数据，需要创建一个Reader对象。Reader对象让你遍历csv文件中的每一行。
import csv
exampleFile=open('test.csv',encoding='utf-8')       #此处对encoding传入值很重要
Reader=csv.reader(exampleFile)      #获取到的是一个Reader对象

#转换为list类型，获取csv文件中的数据
Data=list(Reader)
print(Data)

#对于大型的csv文件，可以采用如下的方式
for row in Reader:  #Reader对象只能循环遍历一次，要再次读取csv文件，必须调用csv.reader，创建一个Reader对象
    print(row)
    print(Reader.line_num)  #获取行号

#要将数据写入csv文件，需要创建一个Writer对象，需要调用csv.writer()函数

writeFile=open('writeTest.csv','a+',newline='')
outputWriter=csv.writer(writeFile)
x=outputWriter.writerow(['ldq','zhang','san'])        #返回值是写入这一行的字符数（包含字符数）
print(x)

#如果希望通过制表符代替逗号来分隔单元格，并希望有两倍行距，可以通过以下的方式
writeFile=open('writeTest.csv','a+',newline='')
#通过改变delimiter的值可以修改以什么作为分隔符
csvWrite=csv.writer(writeFile,delimiter='a',lineterminator='\n\n')
#改变lineterminator的值，可以改变行距
csvWrite.writerow(['apple','bacon','grap'])
csvWrite.close()
print(len('http://www.ygdy8.com/'))

