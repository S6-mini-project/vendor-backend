from django.db import models


class Orders(models.Model):
    """A typical class defining a model, derived from the Model class."""
    o_id = models.AutoField(primary_key=True)
    qty = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    ...

    # Metadata
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.qty
    
class Stocks(models.Model):
    medicine_id  =  models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=255)
    medicine_qty = models.IntegerField()
    
    class Meta:
        ordering = ['medicine_id']