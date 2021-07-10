from django.contrib import admin
from django.urls import path, include
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as djangofilters
from rest_framework import routers, serializers, viewsets, filters

from .models import Result, Category, Department, Assessment, Skill, Employee, Article

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = EmployeeSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Skill
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    assessment = AssessmentSerializer()
    evaluator = EmployeeSerializer()
    evaluatee = EmployeeSerializer()
    skill = SkillSerializer()
    class Meta:
        model = Result
        fields = '__all__'

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

class EmployeesFilter(djangofilters.FilterSet):
    min_age = djangofilters.NumberFilter(field_name="age", lookup_expr='gte')
    max_age = djangofilters.NumberFilter(field_name="age", lookup_expr='lte')
    class Meta:
        model = Employee
        fields = ['is_fired', 'sex', 'department__title']

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = EmployeesFilter
    search_fields = ['name']

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    def get_queryset(self):
        queryset = Result.objects.all()
        evaluatee_id = self.request.query_params.get('evaluatee_id')
        if evaluatee_id is not None:
            queryset = queryset.filter(evaluatee__id=evaluatee_id)
        return queryset

router = routers.DefaultRouter()

router.register(r'departments', DepartmentsViewSet)
router.register(r'employees', EmployeesViewSet)
router.register(r'articles', ArticlesViewSet)
router.register(r'results', ResultsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', admin.site.urls)
]