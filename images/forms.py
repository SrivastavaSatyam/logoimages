from django  import forms
from images.models import Upload
class EntryForm(forms.Form):
    class Meta:
        model=Upload
        fields=('image_svg','image_png','name' ,'description',)

