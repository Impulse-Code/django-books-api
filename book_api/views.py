from django.shortcuts import render
from book_api.models import Book
from rest_framework.decorators import api_view
from book_api.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

# @api_view(['GET','POST'])
# def book_list(request):
#     if request.method == 'GET':
#         try:
#             books=Book.objects.all()
#             serializer = BookSerializer(books,many=True)
#             return Response(data=serializer.data,status=status.HTTP_200_OK)
#         except Book.DoesNotExist:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'POST':
#         try:
#             serializer=BookSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors)
#         except:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# # @api_view(['POST'])
# # def create_book(request):
# #     if request.method == 'POST':
# #         serializer=BookSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
# #         else:
# #             return Response(serializer.errors)
# #     else:
# #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def book(request,pk):
#     if request.method == 'GET':
#         book = Book.objects.get(id=pk)
#         serializer=BookSerializer(book)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     if request.method == 'PUT':
#         try:
#             book = Book.objects.get(id=pk)
#             serializer=BookSerializer(book,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data,status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors)
#         except:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         try:
#             book = Book.objects.get(id=pk)
#             book.delete()
#             return Response(data=f'Book {book.title} has been deleted',status=status.HTTP_204_NO_CONTENT)
#         except Book.DoesNotExist:
#             return Response(data='Specified book does not exist',status=status.HTTP_400_BAD_REQUEST)


class Books_View(APIView):

    def get_books(self):
        try:
            books = Book.objects.all()
        except Book.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND


    def get(self,request):
        # books=Book.objects.all()
        try:
            books=self.get_books()
            serializer = BookSerializer(books,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

   
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data="An error has occurred Please try again.",status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        try:
            book = Book.objects.get(id=request.data['id'])
            serializer=BookSerializer(book,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data="Specified Book could not be updated please try again")
        except:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    

class Get_Book(APIView):
    def get(self,request,pk):
        book=Book.objects.get(id=pk)
        try:
            serializer = BookSerializer(book)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(data=f'Specified book {book.title} has been deleted',status=status.HTTP_410_GONE)
        except Exception as e:
            return Response('An error has occurred')

