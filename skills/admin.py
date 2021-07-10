from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.http import urlencode

from .models import Department, Assessment, Skill, Employee, Result, Article, CommentReaction, CommentContent, Comment, Category

def fire(m, request, queryset):
    queryset.update(is_fired=True)
def unfire(m, request, queryset):
    queryset.update(is_fired=False)

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department

class AssessmentResource(resources.ModelResource):
    class Meta:
        model = Assessment

class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee

class ResultResource(resources.ModelResource):
    class Meta:
        model = Result

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article

class CommentReactionResource(resources.ModelResource):
    class Meta:
        model = CommentReaction

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CommentContentResource(resources.ModelResource):
    class Meta:
        model = CommentContent

class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    search_fields=["title"]
    list_display = ['title']

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
    search_fields=["title"]
    list_display = ['title']

@admin.register(Assessment)
class AssessmentAdmin(ImportExportModelAdmin):
    resource_class = AssessmentResource
    search_fields=["title"]
    list_display = ['title', 'created']

@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource
    search_fields=["title"]
    list_display = ['category', 'title']

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    search_fields=["name"]
    actions=[fire, unfire]
    list_filter=['is_fired']
    list_display = ['department', 'name', 'phone', 'age', 'sex', 'email', 'is_fired']

@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):
    resource_class = ResultResource
    list_display = ['assessment','evaluator','evaluatee','skill','value']

@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource
    search_fields=["title"]
    list_display = ['author', 'title', 'body', 'created']

@admin.register(CommentReaction)
class CommentReactionAdmin(ImportExportModelAdmin):
    resource_class = CommentReactionResource
    list_display = ['title']

@admin.register(CommentContent)
class CommentContentAdmin(ImportExportModelAdmin):
    resource_class = CommentContentResource
    list_display = ['reaction', 'image_url', 'body']

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource
    search_fields=["title"]
    list_display = ['author', 'content', 'title', 'article']