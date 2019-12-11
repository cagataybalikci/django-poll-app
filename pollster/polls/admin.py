from django.contrib import admin

from .models import Question, Choice

# Costumize Admin page
admin.site.site_header = "Pollz Admin"
admin.site.site_title = "Pollz Admin Area"
admin.site.index_title = "Welcome to Pollz Admin Area"


# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)

# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
