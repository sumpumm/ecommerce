from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .pagination import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import *
from django_filters import rest_framework as filters
from .filters import ProductFilter
from rest_framework import filters as f 
from django.db.models import Count
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer
    permission_classes=(
        IsAuthenticatedOrReadOnly,
        IsAdminOrNot
    )
    
    def get_queryset(self):
        return Category.objects.prefetch_related('products').annotate(total_product=Count('products')).all()
    
    
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class =ProductSerializer
    pagination_class=CustomPagination
    filter_backends = (filters.DjangoFilterBackend,f.SearchFilter)
    #filterset_fields=('category',)
    filterset_class=ProductFilter
    search_fields=('name',)
  
    
class CustomerViewSet(viewsets.GenericViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=(IsAuthenticated,)
    
    
    def get_queryset(self,request):
        user=self.request.user
        return Customer.objects.filter(user=user)
    
    def list(self,request,*args, **kwargs):
        customer=self.get_queryset().first()
        serializer=self.serializer_class(customer)
        return Response(serializer.data)
    
    def update(self,request,*args, **kwargs):
        customer=self.get_queryset().first()
        context={}
        context['request']=request
        serializer=self.serializer_class(data=request.data,instance=customer,context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    
    
    
    
    
    

# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
        
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    


# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
        
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# @api_view(['GET','POST'])
# def Category_list(request):
    
#     if request.method=='GET':
#         categories=Category.objects.all()
#         serializer=CategorySerializer(categories,many=True)
#         return Response(serializer.data)
    
#     else:
        
#         serializer=CategorySerializer(data=request.data)    

#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#                     'details':"New Category created",
#                 },
#                 status=status.HTTP_201_CREATED
#                         )
        

# @api_view(['GET','DELETE','PUT'])
# def category_detail(request,pk):
#         category=get_object_or_404(Category,pk=pk)
#         if request.method=="GET":
#             serializer=CategorySerializer(category)
#             return Response(serializer.data)
#         if request.method=="DELETE":
#             category.delete()
#             return Response(
#                 status=status.HTTP_204_NO_CONTENT
#             )
#         if request.method=="PUT":
#             serializer=CategorySerializer(category,data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({
#                 'details':'data has been updated'
#             })


# @api_view(['GET','POST'])
# def ProductList(request):
#     if request.method=='GET':
#         product=Product.objects.all()
#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data)
#     else:
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#                      'details':"New Category created",
#                  },
#                  status=status.HTTP_201_CREATED
#                          )


# @api_view(['GET','DELETE','PUT'])
# def Product_Details(request,pk):
#     product=get_object_or_404(Product,pk=pk)
#     if request.method=='GET':
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
    
#     if request.method=='DELETE':
#         product.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
#     if request.method=="PUT":
#         serializer=ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'details':'data has been updated'
#         })

# class Product_Details(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
    
    
# class ProductList(APIView):
#     def get(self,request):
#         product=Product.objects.all()
#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data)
        
#     def post(self,request):
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#                      'details':"New Category created",
#                  },
#                  status=status.HTTP_201_CREATED
#                          )

        