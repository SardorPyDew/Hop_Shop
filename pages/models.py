from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    massage = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
