from django import forms

class CartAddForm(forms.Form):
    tedad = forms.IntegerField(min_value=1, max_value=9)   # tedadi ke karbar az un mahsul mitune bekhare ro entekhab kone