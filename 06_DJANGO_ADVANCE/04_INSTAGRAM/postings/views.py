from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .forms import PostingForm, ImageForm
from .models import Posting


# Create your views here.

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'posting/posting_detail.html', {
        'posting':posting,
    })

@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'posting/posting_list.html',{
        'postings':postings,
    })


@require_http_methods(['GET', 'POST'])
def create_posting(request):
    images = request.FILES.getlist('file')
    if request.method=='POST':
        posting_form = PostingForm(request.POST)    
        if posting_form.is_valid() and len(images) <=5:
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()
            for image in images:
                request.FILES['file'] = image 
                image_form = ImageForm(files=request.FILES) # Form류는 request로 시작하는 객체여야만 사용가능.
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting
                    image.save()
            return redirect(posting)





       

            
        
    else:
        posting_form = PostingForm()
        image_form = ImageForm()
    return render(request, 'postings/posting_form.html',{
        'posting_form':posting_form,
        'image_form' : image_form,
    })
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id = posting_id)
    if request.method=='POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect(posting)
    else:
        form = PostingForm(instance=posting)
    return render(request, 'postings/posting_form.html',{
        'form':form,
    })
@require_GET
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id = posting_id)
    posting_delete()
    return redirect('postings:posting_list')
