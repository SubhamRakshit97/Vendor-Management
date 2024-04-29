from django.db import models
from django.db.models import Count, Avg, F
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0, null=True)
    average_response_time = models.FloatField(default=None, null=True)
    fulfillment_rate = models.FloatField(default=0)

    def update_performance_metrics(self):
        completed_orders_count = self.purchase_orders.filter(status='completed').count()
        on_time_delivery_count = self.purchase_orders.filter(status='completed', delivery_date__lte=F('acknowledgment_date')).count()
        quality_rating_avg = self.purchase_orders.filter(status='completed').aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
        average_response_time = self.purchase_orders.filter(acknowledgment_date__isnull=False).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time']

        if completed_orders_count > 0:
            self.on_time_delivery_rate = (on_time_delivery_count / completed_orders_count) * 100
            self.quality_rating_avg = quality_rating_avg
            self.average_response_time = average_response_time
            self.fulfillment_rate = (completed_orders_count / self.purchase_orders.count()) * 100
            self.save()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, related_name='purchase_orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.update_performance_metrics()

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
