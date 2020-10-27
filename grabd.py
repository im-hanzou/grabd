import datetime
import requests, os, sys
from re import findall as reg
from time import sleep
from pyfiglet import Figlet


custom_fig = Figlet(font='graffiti')

print(custom_fig. renderText('GRAB.D'))
print('\t Domain Grabber just with Date')
print('\t By https://github.com/xcapri/\n')



def save(fnam,date):
	save = open(fnam, 'a')
	save.write(str(date)+'\n')
	save.close()
def peg(fnames,p):
	red = open(fnames, 'r').read().split('\n')
	for xd in red:		
		for page in range(1,int(p)):
			headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}	
			url = 'https://www.cubdomain.com/domains-registered-by-date/'+xd+'/'+str(page)
			viewsource = requests.get(url,headers=headers, timeout=10).text
			# print(viewsource)
			if 'site' in viewsource:
				# print(viewsource)
				domen = reg('<a href="(.*?)">', viewsource)
				#domen = reg('<img src = >', viewsource)
				for x in domen:
					# print(domen)

					if 'https://www.cubdomain.com/site/' not in viewsource:
						return exit()
					elif 'tools' in x:
						# print('NONE.NONE')
						sleep(0.5)
						# return next(x)
					elif 'domains' in x:
						# return next(x)
						# print('NONE.NONE')
						sleep(0.5)
					elif 'javascript:;"' in x:
						# return next(x)
						# print('NONE.NONE')
						sleep(0.5)
					elif 'dcounter.cubdom' in x:
						# return next(x)
						# print('NONE.NONE')
						sleep(0.5)
					elif 'contact"' in x:
						sleep(0.5)
						
					elif 'about"' in x:
						sleep(0.5)
						
					elif 'chrome.goo' in x:
						sleep(0.5)
						
					elif 'er.com/inte' in x:
						sleep(0.5)
					elif 'facebook.com/cubdo' in x:
						sleep(0.5)
					elif 'rest.com/cub' in x:
						sleep(0.5)
					elif 'domain.com"' in x:
						sleep(0.5)
						
					else:
						asw = x.replace("https://www.cubdomain.com/site/","")
						pew = asw.replace('https://www.cubdomain.com/tools/sitemap-generator" title="Sitemap Generator', '')
						print('\033[0;37;42m [p0n] \033[0m\033[0;37;41m'+pew+'\033[0m')

						save = open('domengrab.txt', 'a')
						save.write(str(pew)+'\n')
						save.close()
					 
					

def forr(sdate,edate,pp):

	ssdate = str(sdate).split('|')
	edates = str(edate).split('|')

	start_date = datetime.date(int(ssdate[0]), int(ssdate[1]), int(ssdate[2]))
	end_date = datetime.date(int(edates[0]), int(edates[1]), int(edates[2]))
	delta = datetime.timedelta(days=1)

	while start_date <= end_date:
		fname = ssdate[0]+'file'+edates[0]
		save(fname,start_date)
		start_date += delta


	peg(fname,pp)

sdate = raw_input(' Input start date: ')
edate = raw_input(' Input end date: ')
pages = raw_input(' Input page: ')

if pages:
	forr(sdate,edate,pages)
