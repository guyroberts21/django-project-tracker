# helpers.py (or you can define this at the top of views.py)
from django.db.models import Count

def get_project_stats(projects_qs):
    """
    Given a queryset of Project objects, returns a dictionary
    of all required dashboard metrics (counts, sub-queries, etc.).
    """
    total_projects = projects_qs.count()
    completed_projects = projects_qs.filter(status='Completed').count()
    pending_projects = projects_qs.filter(status='In Progress').count()
    overdue_projects = projects_qs.filter(rag_status='Red').count()
    program_list = projects_qs.distinct('program_name')
    projectsPerProgram = (
        projects_qs
        .values('program_name__title')
        .annotate(project_count=Count('id'))
        .order_by('program_name__title')
    )

    return {
        "total_projects": total_projects,
        "completed_projects": completed_projects,
        "pending_projects": pending_projects,
        "overdue_projects": overdue_projects,
        "program_list": program_list,
        "projectsPerProgram": projectsPerProgram,
    }


# ========================

# views.py
from django.shortcuts import render
from .models import Project
from .helpers import get_project_stats

def dashboard_view(request):
    # 1. Start with a base queryset (include order_by as needed)
    projects_qs = Project.objects.all().order_by('due_date')

    # 2. Check if there's a search query
    search_query = request.GET.get('q')  # or request.GET.get('q', '')

    if search_query:
        # Apply a filter if the user searched for something
        projects_qs = projects_qs.filter(title__icontains=search_query)

    # 3. Get the computed stats from our helper
    stats = get_project_stats(projects_qs)

    # 4. Build the context, passing in the Projects queryset + stats
    context = {
        "projects": projects_qs,  # Pass the actual queryset if you need to list them
        **stats,                  # Unpack the dictionary from get_project_stats()
    }

    # 5. Render
    return render(request, "pages/dashboard.html", context)
