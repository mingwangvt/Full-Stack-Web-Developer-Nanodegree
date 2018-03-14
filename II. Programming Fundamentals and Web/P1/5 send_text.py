from Twilio.rest import TwilioRestClient
##from moduleName import specific attributes
##from gitHub can find twilio codes.
##from Twilio, a folder called rest; inside the rest, there is a class called TwilioRestClient.
##Also can rewrite as "from Twilio import rest"

#Twilio account number and token
account_id = ""
auth_token = ""
client = TwilioRestClient(account_id, authen_token)
        ##if"from Twilio import rest", here should be "client = rest.TwilioRestClient(account_id, authen_token)"
        ##rest:folder;   TwilioRestClient:class;  client:object/instance
        ##class:blue print     //instance:object of class
message = client.sms.messages.create(
    body = "Text content",
    to = "+1...",  #phone number
    from_ = "+1..."  #phone number provided by Twilio
    )

print message.sid
