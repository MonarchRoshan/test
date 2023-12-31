from django.db import models

# Create your models here.

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    data_type = models.CharField(max_length=1000, db_column='type')
    data_json = models.JSONField()



    class Meta:
        db_table ='stripe_events'

