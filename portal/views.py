from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
import textwrap

from django.views.generic.edit import FormMixin

from .models import News, Redactor, Comments
from .forms import (NewsSearchForm,
                    NewsForm,
                    CommentsForm,
                    NewsUpdateForm)


class NewsListView(generic.ListView):
    model = News
    ordering = ["-published_date"]
    paginate_by = 6
    template_name = "portal/index.html"
    queryset = News.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = NewsSearchForm(initial={"title": title},)

        return context

    def get_queryset(self):
        queryset = News.objects.all()
        form = NewsSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])

        return queryset


class NewsDetailView(FormMixin, generic.DetailView):
    model = News
    form_class = CommentsForm

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "portal:news-detail",
            kwargs={"pk": self.get_object().id}
        )

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        post_id = self.request.POST.get('topic')
        form.instance.post_id = self.get_object().id
        form.save()
        return super().form_valid(form)


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("portal:news-list")

    def form_valid(self, form):
        form.instance.publishers_id = self.request.user.id
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = News
    form_class = NewsUpdateForm
    success_url = reverse_lazy("portal:news-list")

    def form_valid(self, form):
        form.instance.publishers_id = self.request.user.id
        return super().form_valid(form)


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("news")


class NewsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = News

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "portal:user-detail",
            kwargs={"pk": self.request.user.id}
        )


@login_required
def comment_remove(request, pk):
    news_id = Comments.objects.get(pk=pk).post.id
    if request.user == Comments.objects.get(pk=pk).user:
        Comments(id=pk).delete()
    return HttpResponseRedirect(reverse_lazy("portal:news-detail", args=[news_id]))
