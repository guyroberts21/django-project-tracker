from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, F, Q
from .models import Project, Task

def home_view(request): 
    return render(request, "pages/home.html", {})

def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()

    # Metrics
    total_projects = projects.count()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status=3).count()
    pending_tasks = tasks.filter(status=1).count()
    overdue_tasks = tasks.filter(due_date__lt=timezone.now(), status__in=[1, 2]).count()

    # Progress Data (Pie chart)
    task_status_data = tasks.values('status').annotate(count=Count('id'))

    # Pass data to template
    context = {
        'projects': projects,
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'task_status_data': task_status_data,
    }
    return render(request, 'pages/dashboard.html', context)