from django.db import models
from django.utils.timezone import now

class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title}"

class Department(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title}"

class Assessment(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateTimeField(auto_created=True)
    def __str__(self):
        return f"{self.title}"

class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.title}"

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default=18)
    sex = models.CharField(max_length=1)
    email = models.EmailField(null=True, blank=True)
    is_fired = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"

class Result(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='evaluator')
    evaluatee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='evaluatee')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.assessment}: {self.skill} ({self.value})"

class Article(models.Model):
    author = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_created=True)
    def __str__(self):
        return f"{self.title}"

class CommentReaction(models.Model):
    title = models.CharField(max_length=70)
    def __str__(self):
        return f"{self.title}"

class CommentContent(models.Model):
    reaction = models.ForeignKey(CommentReaction, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=1024, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.body}"

class Comment(models.Model):
    author = models.ForeignKey(Employee, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    content = models.ForeignKey(CommentContent, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.author}: {self.title}"