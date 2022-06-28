from django.shortcuts import render
from django.http import Http404
from addBook.models import Book
from recommendationsystem.recommendation import initRecommend
from .models import HomeSlide
from django.views.generic import DetailView
from registration.models import Profile

    
class BookDetailSlugView(DetailView):
    queryset=Book.objects.all()

    template_name="detail.html"
    def get_object(self,*args,**kwargs):
        slug=self.kwargs.get('slug')
        try:
            instance=Book.objects.get(slug=slug)

            if self.request.user.is_authenticated:
                profile=Profile.objects.get(id=self.request.user.id)
                profile.recommendFor=instance.bname
                profile.save()
            
        except Book.DoesNotExist:
            raise Http404("Not found....")
        except Book.MultipleObjectsReturned:
            qs=Book.objects.filter(slug=slug,active=True)
            instance=qs.first()
        except:
            raise Http404("Looks some error occured.")
        
        return instance


def book_list_view(request):

    instance=Book.objects
    slide=HomeSlide.objects.all()
    extra=Book.objects.filter(category='Extra',donation=False).order_by('-id')[:4]
    last_four = Book.objects.filter(donation=False).order_by('-id')[:4]
    featured=Book.objects.filter(featured=True)
    
    d_of_day = []
    for book in Book.objects.order_by('?')[0:5]:
        d_of_day.append(book)
    try:
        recommended = None

        if request.user.is_authenticated:
            
            recommendFor=Profile.objects.get(id=request.user.id).recommendFor
            if recommendFor and Book.objects.filter(bname__iexact = recommendFor).exists():
                recommendedBookIdList=initRecommend(recommendFor)
                querySet=Book.objects.in_bulk(recommendedBookIdList)
                recommended=[querySet[recom] for recom in recommendedBookIdList]
    except Exception as e:
        pass
    context={
        'object':instance,
        'homeslide':slide,
        'latest':last_four,
        'featured':featured,
        'recommended': recommended,
        'extra':extra,
        'd_of_day':d_of_day,

    }
    return render(request,"home.html",context)



def plustwo(request):
    book=Book.objects.filter(category='+2')
    title="Plus two books"
    return render(request,"category.html",{'title':title,'book':book}) 
    
def bachelor(request):
    book=Book.objects.filter(category='Bachelor' , donation=False)
    title="Bachelor books"
    return render(request,"category.html",{'title':title,'book':book})     

def diploma(request):
    book=Book.objects.filter(category='Diploma',  donation=False)
    title="Diploma Books"
    return render(request,"category.html",{'title':title,'book':book})     

def see(request):
    book=Book.objects.filter(category='SEE',  donation=False  )
    title="SEE Books"
    return render(request,"category.html",{'title':title,'book':book})     

def school(request):
    book=Book.objects.filter(category='School',  donation=False)
    title="School Books"
    return render(request,"category.html",{'title':title,'book':book})     

def master(request):
    book=Book.objects.filter(category='Master', donation=False)
    title="Master Books"
    return render(request,"category.html",{'title':title,'book':book})     

def extra(request):
    book=Book.objects.filter(category='Extra',  donation=False)
    title="Extra Books"
    return render(request,"category.html",{'title':title,'book':book})   


def new_collections(request):
    book=Book.objects.all().exclude(donation=True).order_by('-id')
    return render(request,"new_collections.html",{'new':book})    

def donations(request):
    
    book=Book.objects.filter(donation=True).order_by('-id')
    return render(request,"donations.html",{'donations':book})