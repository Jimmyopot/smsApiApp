from django.db import models

import base64
import json
import requests


class CemanetEndpoint(models.Model):
    api_key = models.CharField(max_length=200, blank=True, null=True)
    api_secret = models.CharField(max_length=200, blank=True, null=True)
    unique_ref = models.CharField(max_length=200, blank=True, null=True)
    clientId = models.CharField(max_length=200, blank=True, null=True)
    dlrEndpoint = models.CharField(max_length=200, blank=True, null=True)
    productId = models.CharField(max_length=200, blank=True, null=True)
    phone_no = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return f"My ID is {self.clientId}, {self.productId}"
    
    
    def save(self, *args, **kwargs):     
        
        api_key      = self.api_key
        api_secret    = self.api_secret
          
        # Get Bearer  
        token = api_key + api_secret

        message_bytes = token.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        bearer = base64_bytes.decode('ascii')

            
        # Handle data and send to API enpoint
        post_dict = {
            "unique_ref": self.unique_ref,
            "clientId": self.clientId, 
            # "dlrEndpoint": "https://51d0a4568722.ngrok.io/callback/index.php",
            "dlrEndpoint": "http://abb8da1bad4d.ngrok.io/rpt/callback_report/",
            "productId": self.productId,
            "msisdn":  self.phone_no,
            "message": self.message,
        }

        data = json.dumps(post_dict) # converts data to json

        url = 'https://api.cemanet.co.ke:8445/Cemanet/api/CemanetBulkApi'  # set url  
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + bearer} # set headers
        
        r = requests.get(url=url, headers=headers, data=data)
        my_data = r.json() # converts the request into json format
        with open(r'C:/Users/user/projects/sendCemanet_sms/credit/templates/credit/report.html', 'w') as f:
            f.write(r.text)
            print(f)
           
        with open(r'C:/Users/user/projects/sendCemanet_sms/credit/templates/credit/callback.html', 'w') as outfile:
            json.dump(my_data, outfile)

        print(my_data) # makes the request and prints to terminal
        return super(CemanetEndpoint, self).save(*args, **kwargs)



class CallbackUrl(models.Model):
    text = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        
        url = 'https://api.cemanet.co.ke:8445/Cemanet/api/CemanetBulkApi'
        files = {'file': open(r'C:/Users/user/projects/sendCemanet_sms/callback.html', 'wb')}
        my_files = requests.post(url=url, files=files)
        
        return super(CallbackUrl, self).save(*args, **kwargs)
