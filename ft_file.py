import re
f=open(r'C:\Users\ft\Desktop\a.txt')
f_txt=f.read()
f.close()
patt=r'\d{4}-\d{7}'
res=re.findall(patt,f_txt)
print(res)
