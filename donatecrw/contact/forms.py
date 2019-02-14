from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Name", required= True, widget = forms.TextInput(
        attrs = {"class":"form-control", "placeholder":"Write you name"}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label = "Email", required= True, widget = forms.EmailInput(
        attrs = {"class":"form-control", "placeholder":"Write you email"}
    ), min_length=3, max_length=100)
    content = forms.CharField(label = "Content", required= True, widget = forms.Textarea(
        attrs = {"class":"form-control", "rows":4, "placeholder":"Description of project"}
    ))
    amount = forms.CharField(label = "Amount", required= False, widget = forms.TextInput(
        attrs = {"class":"form-control", "placeholder":"Amount needed on Crowns"}
    ), min_length=3, max_length=12)
    address_shop = forms.CharField(label = "Crown Address", required= False, widget = forms.TextInput(
        attrs = {"class":"form-control", "placeholder":"Address for shop"}
    ), min_length=3, max_length=100)
    references = forms.CharField(label = "References", required= False, widget = forms.TextInput(
        attrs = {"class":"form-control", "placeholder":"References"}
    ), min_length=3, max_length=100)