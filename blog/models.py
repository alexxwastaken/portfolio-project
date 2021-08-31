from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 100:
            return str(self.body[:100] + '...')
        return self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
