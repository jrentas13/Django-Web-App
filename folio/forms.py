from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name"
    )
    email = forms.EmailField(label="Email Address")
    subject = forms.CharField(max_length=150)
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 6,
                "placeholder": "Tell me about your project..."
            }
        )
    )