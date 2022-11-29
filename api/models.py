from django.db import models
from core.settings import MEDIA_ROOT


class BillsUpload(models.Model):
    file = models.FileField(upload_to=MEDIA_ROOT, blank=True, null=False)

    def __str__(self):
        return self.file

class Clients(models.Model):
    client_name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        duplicates = Clients.objects.filter(
            client_name=self.client_name,
        )
        if duplicates.exists() > 0:
            raise ValueError('This client_name already exists')
        else:
            super(Clients, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Bills(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    client_org = models.CharField(max_length=255)
    number = models.IntegerField()
    date = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    bills_sum = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        duplicates = Bills.objects.filter(
            client_org=self.client_org,
            number=self.number,
        )
        if duplicates.exists() > 0:
            raise ValueError('This client_org-number pair already exists')
        else:
            super(Bills, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.client} - {self.number}'

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'
        unique_together = [['client_org', 'number']]
