from django.core.management.base import BaseCommand
import imaplib, email, email.header, datetime

class Command(BaseCommand):

	def process_mailbox(self,box):
		rv, data = box.search(None, "ALL")
		if rv != 'OK':
			print "No messages found!"
		
		for num in data[0].split():
			rv, data = box.fetch(num, '(RFC822)')
			if rv != 'OK':
				print "ERROR getting message", num
			msg = email.message_from_string(data[0][1])
			decode_msg = email.header.decode_header(msg['Subject'])[0]
			str_decode = str(decode_msg[1])
			if str_decode != "None":
				subject = decode_msg[0].decode(str_decode)
			else:
				subject = str(decode_msg[0])	
			print u'Message %s: %s' % (num, subject)
			print u'Raw Date:', msg['Date']
			date_tuple = email.utils.parsedate_tz(msg['Date'])
			if date_tuple:
				local_date = datetime.datetime.fromtimestamp(
				email.utils.mktime_tz(date_tuple))
				print "Local Date:", \
				local_date.strftime("%a, %d %b %Y %H:%M:%S")


	def handle(self,*args,**options):
		EMAIL_ACCOUNT = raw_input("E-mail:")
		EMAIL_PASSWORD = raw_input("Password:")
		box = imaplib.IMAP4_SSL('imap.gmail.com')

		try:
			rv, data = box.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
		except imaplib.IMAP4.error:
			return "LOGIN FAILED!!! "
		print rv, data
		
		rv, data = box.select()
		if rv == 'OK':
			print "Processing mailbox...\n"
			self.process_mailbox(box)
			box.close()
		else:
			print "ERROR: Unable to open mailbox ", rv

		box.logout()