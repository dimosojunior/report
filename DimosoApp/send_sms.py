from twilio.rest import Client
from DimosoApp.models import *
from DimosoApp.forms import *


def sendsms():
	#form = ReportForm()
	#name = request.POST['name']
	#phone = request.POST['phone']
	account_sid = "AC8d65d3310f680df6905c512df6690afb"
	auth_token = "b6c2b89770b828083644d3ad215a1d7c"
	client = Client(account_sid, auth_token)
	message = client.messages \
						.create(
							body="name-----",
							from_='+17692248509',
							to='+255628431507'
							#to =phone
									)
	print("message sent successfully")
					