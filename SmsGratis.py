import mechanize,time,os
from bs4 import BeautifulSoup as BS

class Sms:
	def __init__(self):
		self.br = mechanize.Browser()
		self.br.set_handle_referer(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_gzip(True)
		self.br.set_handle_equiv(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		self.br.addheaders =[('Connection','keep-alive'),
		('Pragma','no-cache'),
		('Cache-Control','no-cache'),
		('Origin','http://sms.payuterus.biz'),
		('Upgrade-Insecure-Requests','1'),
		('Content-Type','application/x-www-form-urlencoded'),
		('User-Agent','Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'),
		('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),
		('Referer','http://sms.payuterus.biz/alpha/'),
		('Accept-Encoding','gzip, deflate'),
		('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
		]
		self.u='http://sms.payuterus.biz/alpha'
		self.menu()

	def menu(self):
		os.system('clear')
		print("\033[1;31m______________________________________________\n")
		time.sleep(1)
		print("\033[1;37mTool   : \033[1;34mSMS GRATIS UNLIMITED")
		time.sleep(1)
		print("\033[1;37mMOD    : \033[1;36mFAQIH ID")
		time.sleep(1)
		print("\033[1;37mCODE   : \033[1;37mSOBAT ANJAY")
		time.sleep(1)
		print("\033[1;37mFB   : \033[1;32mFAQIH ID")
		time.sleep(1)
		print("\033[1;37mYoutube: \033[1;33mILANGQWER")
		time.sleep(1)
		print("\033[1;31m______________________________________________\n")
		os.system('xdg-open https://youtube.com/ilangqwer')
		o=int(0)
		time.sleep(2)
		nomer=int(input("\033[1;37m[\033[1;32m?\033[1;37m] \033[1;37mNOMER TARGET: \033[1;32m"))
		pesan=input("\033[1;37m[\033[1;32m+\033[1;37m] \033[1;37mMASUKAN PESAN: \033[1;32m")
		jumlah=int(input("\033[1;37m[\033[1;32m*\033[1;37m] \033[1;37mJUMLAH KIRIMAN: \033[1;32m"))
		jun=pesan.split(' ')
		print("\033[1;31m______________________________________________")
		if jumlah > 100:
			exit("\033[1;37m[\033[1;31m!\033[1;37m] Jangan kebanyakan goblok, kasian !!\n\033[1;37m[\033[1;31m!\033[1;37m] Sekali ngirim 100 aja\n")
		else:
			for x in range(jumlah):
				self.main(nomer,jun)
				time.sleep(1.5)

	def main(self,nomer,jun):
		a=[]
		lol=BS(self.br.open(self.u),features="html.parser")
		for i in lol.find_all("span"):
			a.append(i.text)
		mek=int(str(a)[2])+int(str(a)[6])
		self.br.select_form(nr=0)
		self.br.form['nohp']=str(nomer)
		self.br.form['pesan']=str(jun)
		self.br.form['captcha']=str(mek)
		pek=self.br.submit().read()
		if 'PESAN GRATIS DIKIRIM' in str(pek):
			print("\033[1;37m[\033[1;31m!\033[1;37m] MENGIRIM PESAN KE",nomer,"\033[1;37m[\033[1;31mGAGAL\033[1;37m]")
		else:
			print("\033[1;37m[\033[1;32m+\033[1;37m] MENGIRIM SMS KE",nomer,"\033[1;37m[\033[1;32mSUKSES\033[1;37m]")

try:
	Sms()
except KeyboardInterrupt:
	print("\033[1;37m\nEXIT")
except Exception as E:
	print("\033[1;37m\nEXIT")
