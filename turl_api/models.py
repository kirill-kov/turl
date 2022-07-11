from django.db import models


class TurlAPI(models.Model):
    class Meta:
        db_table = 'main_urls'

    id = models.AutoField(primary_key=True)
    long_url = models.URLField(max_length=1000)
    short_url = models.URLField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
