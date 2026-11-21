from django.shortcuts import render
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teachers,Courses,Students
from .pagination import CustomPadination
from .search import search_filter
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='post',
    request_body=TeachersSerializer,
    responses={201: "Created", 400: "Validation error"}
)
@api_view(['GET','POST'])
def tea_list(request):
    if request.method=='GET':
        queryset=Teachers.objects.all()
        paginator=CustomPadination()
        paginated_queryset=paginator.paginate_queryset(queryset,request)
        serializer=TeachersSerializer(paginated_queryset,many=True).data
        return paginator.get_paginated_response(serializer)

    if request.method=='POST':
        serializer=TeachersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(['GET'])
def get_tea_by_id(request,pk):
    try:
        item = Teachers.objects.get(pk=pk)
    except:
        return Response(status=404)

    serializer=TeachersSerializer(item)
    return Response(serializer.item)


@api_view(['PUT'])
def update_tea(request,pk):
    try:
        item=Teachers.objects.get(pk=pk)
    except:
        raise Response(status=404)

    serializer=TeachersSerializer(item,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)

@api_view(['DELETE'])
def del_tea(request,pk):
    try:
        item =Teachers.objects.get(pk=pk)
    except:
        return Response(status=404)
    item.delete()
    return Response(status=204)



@api_view(['GET','POST'])
def cour_list(request):
    if request.method=='GET':
        queryset=Courses.objects.all()
        queryset=search_filter(queryset,request.GET)
        serializer=CoursesSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(['GET'])
def get_cour_by_id(request,pk):
    try:
        item = Courses.objects.get(pk=pk)
    except:
        return Response(status=404)

    serializer=CoursesSerializer(item)
    return Response(serializer.item)


@api_view(['PUT'])
def update_cour(request,pk):
    try:
        item=Courses.objects.get(pk=pk)
    except:
        raise Response(status=404)

    serializer=CoursesSerializer(item,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)

@api_view(['DELETE'])
def del_cour(request,pk):
    try:
        item =Courses.objects.get(pk=pk)
    except:
        return Response(status=404)
    item.delete()
    return Response(status=204)

@api_view(['GET','POST'])
def stud_list(request):
    if request.method=='GET':
        queryset=Students.objects.all()
        paginator=CustomPadination()
        paginated_queryset=paginator.paginate_queryset(queryset,request)
        serializer=StudentsSerializer(paginated_queryset,many=True).data
        return paginator.get_paginated_response(serializer)

    if request.method=='POST':
        serializer=StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


@api_view(['GET'])
def get_stud_by_id(request,pk):
    try:
        item = Students.objects.get(pk=pk)
    except:
        return Response(status=404)

    serializer=StudentsSerializer(item)
    return Response(serializer.item)


@api_view(['PUT'])
def update_stud(request,pk):
    try:
        item=Students.objects.get(pk=pk)
    except:
        raise Response(status=404)

    serializer=StudentsSerializer(item,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)

@api_view(['DELETE'])
def del_stud(request,pk):
    try:
        item =Students.objects.get(pk=pk)
    except:
        return Response(status=404)
    item.delete()
    return Response(status=204)