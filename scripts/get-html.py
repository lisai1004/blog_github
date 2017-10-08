# -*- coding: utf-8 -*-
import os ,shutil
from sgmllib import SGMLParser  
class GetIdList(SGMLParser):  
    def reset(self):  
        self.IDlist = []  
        self.flag = False  
        self.getdata = False  
        self.verbatim = 0  
        SGMLParser.reset(self)  
          
    def start_div(self, attrs):  
        if self.flag == True:  
            self.verbatim +=1 #进入子层div了，层数加1  
            return  
        for k,v in attrs:#遍历div的所有属性以及其值  
            if k == 'class' and v == 'entry-content':#确定进入了<div class='entry-content'>  
                self.flag = True  
                return  
  
    def end_div(self):#遇到</div>  
        if self.verbatim == 0:  
            self.flag = False  
        if self.flag == True:#退出子层div了，层数减1  
            self.verbatim -=1  
  
    def start_p(self, attrs):  
        if self.flag == False:  
            return  
        self.getdata = True  
          
    def end_p(self):#遇到</p>  
        if self.getdata:  
            self.getdata = False  
  
    def handle_data(self, text):#处理文本  
        if self.getdata:  
            self.IDlist.append(text)  
              
    def printID(self):
        for i in self.IDlist:
            print i
            if i.find("Created") == 0:
                return i
  
  
##import urllib2  
##import datetime  
##vrg = (datetime.date(2012,2,19) - datetime.date.today()).days  
##strUrl = 'http://www.nod32id.org/nod32id/%d.html'%(200+vrg)  
##req = urllib2.Request(strUrl)#通过网络获取网页  
##response = urllib2.urlopen(req)  
##the_page = response.read()  
  
the_page ='''''<html> 
<head> 
<title>test</title> 
</head> 
<body> 
<h1>title</h1> 
<div class='entry-content'> 
<div class= 'ooxx'>我是来捣乱的</div> 
<p>Created Sunday 10 September 2017</p>
<div class= 'ooxx'>我是来捣乱的2<div class= 'ooxx'>我是来捣乱的3</div></div> 
</div> 
<div class='content'> 
<p>内容1</p> 
<p>内容2</p> 
…… 
<p>内容n</p> 
</div> 
</body> 
</html> 
'''  


PATH='/blog_github/_posts'

'''
lister = GetIdList()
the_page1 = open('/blog_github/_posts/net.html').read()
print the_page1
lister.feed(the_page1)  
s=lister.printID()
'''

def add_date_rename(file_name):
	file_name_old = PATH + '/' + file_name

	fp = open(file_name_old)
	tmp = fp.readline()
	year = ''
	month = ''
	day = ''
	while tmp:
		#print tmp
		if tmp.find('Created') == 0:
			'''
			print tmp
			print(tmp.split(' ')[0])
			print(tmp.split(' ')[1])
			print(tmp.split(' ')[2])
			print(tmp.split(' ')[3])
			print(tmp.split(' ')[4])
			'''
			day = tmp.split(' ')[2]
			month = tmp.split(' ')[3]
			year = tmp.split(' ')[4]

			year_tmp = year[0] + year[1] + year[2] + year[3]
	 		break
		tmp = fp.readline()
	fp.close()
	if year == '' or month == '' or day == '':
		return 

	if month == 'January' or month == '一月':
		month = '01'
	elif month == 'February' or month == '二月':
		month = '02'
	elif month == 'March' or month == '三月':
		month = '03'
	elif month == 'April' or month == '四月':
		month = '04'
	elif month == 'May' or month == '五月':
		month = '05'
	elif month == 'June' or month == '六月':
		month = '06'
	elif month == 'July' or month == '七月':
		month = '07'
	elif month == 'August' or month == '八月':
		month = '08'
	elif month == 'September' or month == '九月':
		month = '09'
	elif month == 'October' or month == '十月':
		month = '10'
	elif month == 'November' or month == '十一月':
		month = '11'
	elif month == 'December' or month == '十二月':
		month = '12'
	else :
		print 'month wrong'
		return

	file_name_new = PATH + '/' +  year_tmp + '-' + month + '-' + day + '-' + file_name
	#rename
	os.rename(file_name_old, file_name_new)

def listdir_all_file(path):
	file_path = path
	#print path

	for file_name in os.listdir(path):
		file_path = path + '/' + file_name
		#print(file_name)		
 		while os.path.isdir(file_path):
			listdir_all_file(file_path)
			break
		if os.path.isdir(file_path):
			continue

		if os.path.dirname(file_path) == '/blog_github/_posts':
			continue
		'''
		a=file_path.split('/')
		print a
		file_path_tmp = ''
		i = 1
		for i in range(a.__len__() - 1):
			file_path_tmp = a[i] + '-'
 			i = i + 1
 		file_path_tmp = file_path_tmp + '-' + a[i] 
		file_path= file_path_tmp
		'''
		shutil.move(file_path, '/blog_github/_posts')	
		#print(file_name)


listdir_all_file(PATH)
for file_name in os.listdir(PATH):
	file_path = PATH+'/'+file_name
	if os.path.isdir(file_path):
		command = 'rm -rf ' + file_path
		os.system(command)
		continue

for file_name in os.listdir(PATH):
	add_date_rename(file_name)
