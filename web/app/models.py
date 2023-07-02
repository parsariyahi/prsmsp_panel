from django.db import models

PANELS = (
    ("kavenegar", "kavenegar"),
    ("smsdotir","smsdotir"),
    ("webonesms","webonesms"),
    ("melipayamak","melipayamak"),
    ("mediana","mediana"),
    ("ghasedaksms","ghasedaksms"),
    ("farazsms","farazsms"),
    ("niksms","niksms"),
    ("smsone","smsone"),
    ("sapak","sapak"),
)

class SmsPanel(models.Model):
    panel = models.CharField(max_length=250, choices=PANELS)
    api_key = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=250, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.panel
    

class Sms(models.Model):
    panel = models.ForeignKey(SmsPanel, on_delete=models.RESTRICT)
    originator = models.CharField(max_length=250, blank=True, null=True)
    receptor = models.CharField(max_length=250, blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    send_at = models.DateTimeField(auto_now_add=True)