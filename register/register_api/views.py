from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RegisterSerializer
from register.models import Register
from rest_framework.generics import ListAPIView


@api_view(['GET',])
def api_detail_view(request,pk):
    try:
        register = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegisterSerializer(register)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_view(request,pk):
    try:
        register = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RegisterSerializer(register, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE',])
def api_delete_view(request,pk):
    try:
        register = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = register.delete()
        data={}
        if operation:
            data['success'] = "Delete Successful"
        else:
            data['failure'] = "Delete failed"
        return Response(data=data)


@api_view(['POST',])
def api_create_view(request):
    register = Register()
    if request.method == 'POST':
        serializer = RegisterSerializer(register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ApiRegisterView(ListAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

