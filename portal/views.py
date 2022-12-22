from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from portal.models import News


class NewsListView(generic.ListView):
    model = News
    ordering = ["-created_time"]
    paginate_by = 5
    template_name = "portal/index.html"
    queryset = News.objects.all()
