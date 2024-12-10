from django import forms
from Post.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image"]
        labels = {
            "title": "عنوان",
            "body": "متن",
            "image": "تصویر",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "background-color: #e8f5e9; font-size: 14px; border: 1px solid #c8e6c9; padding: 8px; border-radius: 4px;",
                    "placeholder": "عنوان را وارد کنید",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control font1 text-1xl",
                    "style": "background-color: #fbe9e7; font-size: 14px; border: 1px solid #ffab91; padding: 10px; border-radius: 6px;",
                    "placeholder": "توضیحات خود را اضافه کنید...",
                }
            ),
            "image": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "style": "background-color: #e3f2fd; font-size: 14px; border: 1px solid #90caf9; padding: 8px; border-radius: 4px;",
                    "placeholder": "لینک تصویر را وارد کنید",
                }
            ),
        }
        error_messages = {
            "title": {
                "required": "لطفاً عنوان را وارد کنید.",
                "max_length": "عنوان نمی‌تواند طولانی‌تر از مقدار مجاز باشد.",
            },
            "body": {
                "required": "لطفاً متن را وارد کنید.",
            },
            "image": {
                "required": "لطفاً لینک تصویر را وارد کنید.",
                "invalid": "لینک تصویر معتبر نیست.",
            },
        }
