from rest_framework.response import Response
from Application.models import *
from rest_framework.views import APIView
from BlogAPI.serializers import *
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Create your views here.
#USER API's
class UserAPI(APIView):
    def get(self, request,pk = None, format= None):
        id = pk 
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializers(user)
            return Response(serializer.data)

        user = User.objects.all()
        serializer = UserSerializers(user , many = True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format= None):
        id = pk 
        user = User.objects.get(pk = id)
        serializer = UserSerializers(user, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


#------------------------------------------------------------------------------------------------


#BLOG API's
class PostAPI(APIView):
    authentication_class=[TokenAuthentication]
    def get(self, request,pk = None, format= None):
        id = pk 
        if id is not None:
            post = Post.objects.get(id=id)
            serializer = PostSerializers(post)
            
            return Response(serializer.data)
        
        post = Post.objects.all()
        serializer = PostSerializers(post , many = True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        request.data.update({"user":request.user})
        # print(request.data)
        serializer = PostSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format= None):
        id = pk 
        post = Post.objects.get(pk = id)
        serializer = PostSerializers(post, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


    def delete(self, request, pk):
        id = pk 
        post = Post.objects.get(pk = id)
        serializer = PostSerializers(post, data=request.data, partial= True)
        if serializer.is_valid():
            post.soft_delete = True
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


#---------------------------------------------------------------------------------------


#CategoryAPI
class CategoryAPI(APIView):
    def get(self, request,pk = None, format= None):
        id = pk 
        if id is not None:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)

        category = Category.objects.all()
        serializer = CategorySerializer(category , many = True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format= None):
        id = pk 
        category = Category.objects.get(pk = id)
        serializer = CategorySerializer(category, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


#-------------------------------------------------------------------------------------------

#User-Access Token API