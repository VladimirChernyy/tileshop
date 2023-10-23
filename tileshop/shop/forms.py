from django import forms

from shop.models import Review


class ReviewCreateForm(forms.ModelForm):
    text = forms.CharField(label='',
                           widget=forms.Textarea(
                               attrs={'class': 'form-control'}))

    class Meta:
        model = Review
        fields = ('text',)
