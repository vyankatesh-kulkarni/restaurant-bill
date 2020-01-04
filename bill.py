#!C:\Users\Venatesh\AppData\Local\Programs\Python\Python37-32\pythonw.exe
print("content-type:text/html\r\n\r\n")
import cgi
formdata=cgi.FieldStorage()


m=formdata.getvalue('order')
v=formdata.getvalue('qty')


#print(m)
#print(v)

l=len(m)
i=0
l=len(m)
total=0
sum_=0
while i<=l-1:
	sum_= int(m[i])*int(v[i])
	total=sum_+total
	i+=1
#print(total)
print("<h2 style=' text-align:center;margin-top:50px;'>Your total bill is Rs.",total, "/- only</h2>")

#################################################################################
'''order=formdata.getvalue('order')
qty=formdata.getvalue('qty')
'

#print(m)
#print(v)

l=len(order)
i=0
l=len(order)
total=0
sum_=0
while i<=l-1:
	sum_= int(order[i])*int(qty[i])
	total=sum_+total
	i+=1
#print(total)
print("<h2>Your total bill is Rs.",total, "</h2>")'''
