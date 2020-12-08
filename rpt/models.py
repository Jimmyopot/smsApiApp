from django.db import models


class Book(models.Model):
    message = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):     
        
        with open(r'C:/Users/user/projects/sendCemanet_sms/rpt/templates/rpt/safaricom.html', 'r') as f:
            file_content = f.read()
            print(file_content)
            f.close()
    
        return super(Book, self).save(*args, **kwargs)