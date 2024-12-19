# models.py
from django.db import models
from django.utils import timezone

class Project(models.Model):
    STATUS_CHOICES = [
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Percentage progress (0.00 to 100.00)

    def __str__(self):
        return self.title[:50]

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

