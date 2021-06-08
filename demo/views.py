from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):

    books = Book.objects.all()
    output1 = ""
    for book in books:
        output1 += f"<p>We have '{book.title}' with ID {book.id} in DB.<p/>"

    output2 = f"<h1>We have {len(books)} books in DB.<h1/>"

    def get(self, request):
        return HttpResponse(self.output1 + self.output2)


def first(request):
    return HttpResponse('First message from views')
