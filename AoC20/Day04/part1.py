import re
with open('f','r') as f:
	v=0
	s=[]
	for l in f:
		if len(l) != 1:
			s.append(l[:-2])
		else:
			w=' '.join(s)
			s=[]
			g=re.findall('[a-z]{3}:[^ ]*',w+' ')
			n=len(g)
			t=sum(map(lambda x:x.split(':')[0]=='cid',g))
			v+=(n-t)==7
print(v)
