from .models import *
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField,ValidationError,SerializerMethodField

class TeachersSerializer(ModelSerializer):
    course_count=SerializerMethodField()
    class Meta:
        model=Teachers
        fields=['id','name','experience','course_count']

    def validate(self, data):
        if data['experience']<0:
            raise ValidationError('a bacha devonii ee')
        if len(data['name'])<=3:
            raise ValidationError('nomt qlay?')
        return data

    def get_course_count(self,obj):
        return Courses.objects.filter(teacher=obj).count( )


class CoursesSerializer(ModelSerializer):
    student_count=SerializerMethodField()
    class Meta:
        model=Courses
        fields=['title','price','teacher','teacher_id','student_count']
    teacher=TeachersSerializer(read_only=True)
    teacher_id=PrimaryKeyRelatedField(
        queryset=Teachers.objects.all(),
        source='teacher',
        write_only=True
    )
    def get_student_count(self,obj):
        return Students.objects.filter(course=obj).count()

    def validate(self, data):
        if data['price']<=0:
            raise ValidationError('sart zadagiyay?')
        if len(['title'])<=3:
            raise ValidationError('i chi nomaeee?')
        return data


class StudentsSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields=['name','age',"course","course_id"]
    course=CoursesSerializer(read_only=True)
    course_id=PrimaryKeyRelatedField(
        queryset=Courses.objects.all(),
        source='course',
        write_only=True
    )
    def valdate(self,data):
        if data['age']<10:
            raise ValidationError('ita pir bday ')
        if len(data['name'])<=3:
            raise ValidationError('nomt darozi bad')
        