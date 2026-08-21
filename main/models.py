from django.db import models


SERVICE_CHOICES = [
    ('insurance', 'Insurance Policy Sales'),
    ('consultancy', 'Consultancy Services (B2B & B2C)'),
    ('financing', 'Financing & Mortgage Assistance'),
    ('real_estate', 'Real Estate Marketing & Branding'),
    ('relocation', 'Relocation & Concierge Services'),
    ('other', 'Other / General Enquiry'),
]


class ConsultationEnquiry(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Consultation Enquiry'
        verbose_name_plural = 'Consultation Enquiries'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.full_name} — {self.get_service_display()} ({self.submitted_at.strftime('%d %b %Y')})"


class CallbackRequest(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    preferred_time = models.CharField(max_length=100, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Callback Request'
        verbose_name_plural = 'Callback Requests'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} — {self.phone} ({self.submitted_at.strftime('%d %b %Y')})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} — {self.subject} ({self.submitted_at.strftime('%d %b %Y')})"
