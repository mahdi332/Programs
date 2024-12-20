from django.contrib import admin
from .models import Question , Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class Questionadmin(admin.ModelAdmin):
    search_fields=["question_text"]
    list_display=[
        "question_text",
        "pub_date",
        "was_published_recently"
    ]
    list_filter=["pub_date"]
    fieldsets=[ 
        (None , {"fields":["question_text"]}),
        ("Date information",{"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question,Questionadmin)