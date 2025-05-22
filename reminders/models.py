from django.db import models

class Reminder(models.Model):
    REMINDER_TYPES = [
        ('health', 'Health'),
        ('meeting', 'Meeting'),
        ('birthday', 'Birthday'),
        ('other', 'Other'),
    ]

    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    reminder_type = models.CharField(max_length=50, choices=REMINDER_TYPES)

    def __str__(self):
        return f"{self.message} on {self.date} at {self.time}"
