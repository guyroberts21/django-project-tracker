from django.db import models
from datetime import timedelta
from django.utils.timezone import now
from django.utils import timezone

class Project(models.Model):
    STATUS_CHOICES = [
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Completed'),
    ]

    RAG_CHOICES = [
        ('Red', 'Red'),
        ('Amber', 'Amber'),
        ('Green', 'Green'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Percentage progress (0.00 to 100.00)
    rag_status = models.CharField(max_length=6, choices=RAG_CHOICES, default='Green', editable=True)

    def __str__(self):
        return self.title[:50]

    def save(self, *args, **kwargs):
        # Auto-calculate RAG status based on conditions if not overridden
        if not self.pk or not self.rag_status:  # Only calculate if not overridden
            if self.progress < 50 and self.due_date <= now().date() + timedelta(weeks=1):
                self.rag_status = 'Red'
            elif self.progress < 80 and self.due_date <= now().date() + timedelta(weeks=1):
                self.rag_status = 'Amber'
            else:
                self.rag_status = 'Green'
        super().save(*args, **kwargs)

    def update_progress(self):
        tasks = self.task_set.all()
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(status=3).count()  # Assuming status 3 means completed
        if total_tasks > 0:
            self.progress = (completed_tasks / total_tasks) * 100
            self.save()


class Task(models.Model):
    STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Completed'),
    ]

    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2,
    )
    due_date = models.DateTimeField(default=timezone.now)
    completion_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title[:50]

    def mark_as_completed(self):
        self.status = 3
        self.completion_date = timezone.now()
        self.save()

