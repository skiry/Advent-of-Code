import re
def y(e):return int(e)
def c(a,b,d):return a in range(b,d+1)
with open('f','r') as f:
	v=0
	s=[]
	for l in f:
		if len(l) != 1:
			s.append(l.rstrip())
		else:
			w=' '.join(s)
			s=[]
			g=re.findall('(byr:[\d]{4}|iyr:[\d]{4}|eyr:[\d]{4}|hgt:[\d]*(?:cm|in)|iyr:[\d]{4}|hcl:#[\da-f]{6}|ecl:(?:amb|blu|brn|gry|grn|hzl|oth)|pid:[\d]{9})',w+' ')
			n=len(g)
			t=sum(map(lambda x:x.split(':')[0]=='cid',g))
			q=0
			for d in g:
				i=d[:3]
				e=d[-4:]
				k=d[4:-2]
				j=d[-2:]
				if (i=='byr' and c(y(e),1920,2002)) or (i=='iyr' and c(y(e),2010,2020)) or (i=='eyr' and c(y(e),2020,2030)) or (i=='hgt' and ((c(y(k),150,193) and j=='cm') or (c(y(k),59,76) and j=='in'))):q+=1
			if q==4:v+=(n-t)==7
print(v)
