from django.contrib import admin

from .models import Question,solution, testcase

admin.site.register(Question)
admin.site.register(solution)
admin.site.register(testcase)