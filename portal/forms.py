from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import Textarea

from portal.models import News, Comments


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = News
        exclude = ["publishers"]


class NewsSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by news..."})
    )


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
        self.fields["content"].widget = Textarea(attrs={"rows": 7})


class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ["publishers"]
