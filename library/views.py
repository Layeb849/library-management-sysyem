
from django.shortcuts import render, redirect
from .models import Review
from django.contrib import messages



# def home(request):
#     return render(request, 'heroSection.html')

def contact(request):
    return render(request, 'contact.html')

def footer(request):
    return render(request, 'footer.html')

# def about(request):
#     return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def admission(request):
    return render(request, 'form/addmision.html')

# def community(request):
#     return render(request, 'form/community.html')

def student_list(request):
    return render(request, 'form/student.html')

def achivement(request):
    return render(request, 'form/achievement.html')

def achivementDetails(request):
    return render(request, 'form/achiveDetails.html')

def studentDetails(request):
    return render(request, 'form/studentDetails.html')

def newcollection(request):
    return render(request, 'form/newcollection.html')

def collectionDetails(request):
    return render(request, 'form/collectionDetails.html')

def write_review(request):
    return render(request, 'form/review.html')

    



def review_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        image = request.FILES.get('image') 

        if name and comment:
            Review.objects.create(
                name=name,
                comment=comment,
                image=image
            )
            messages.success(request, "Thank you for your feedback!")
            return redirect('home') 
        else:
            messages.error(request, "Please fill in all required fields.")
            
    return redirect('review_create')

def home(request):

    content = Review.objects.all().order_by('-created_at')[:6]
    return render(request, 'heroSection.html', {'content': content})




# yearly achievement view

from .models import YearlyAchivement

def about(request):
    achievements = YearlyAchivement.objects.all().order_by('-year')

    return render(request, 'about.html', {
        'achievements': achievements
    })


# Add yearly achievement (manual form handling)
def add_yearly_achievement(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        title = request.POST.get('title')
        description = request.POST.get('description')

        YearlyAchivement.objects.create(
            year=year,
            title=title,
            description=description
        )

        return redirect('about')  # Redirect to the timeline list after adding

    return render(request, 'dashboard/about/add_achievement.html')




# committee data upload view



from django.shortcuts import render, redirect
from .models import CommitteeMember, CommitteeDocument


def upload_committee(request):
    if request.method == 'POST':
        upload_type = request.POST.get('type')

        if upload_type == 'member':
            CommitteeMember.objects.update_or_create(
                role=request.POST.get('role'),  # president / secretary
                defaults={
                    'name': request.POST.get('name'),
                    'image': request.FILES.get('image'),
                    'phone': request.POST.get('phone'),
                    'email': request.POST.get('email'),
                }
            )

        elif upload_type == 'pdf':
            CommitteeDocument.objects.create(
                title=request.POST.get('title'),
                pdf_file=request.FILES.get('pdf_file')
            )

        return redirect('community')

    return render(request, 'dashboard/commitee/commitee_add.html')


def community_view(request):
    president = CommitteeMember.objects.filter(role='president').first()
    secretary = CommitteeMember.objects.filter(role='secretary').first()
    latest_docs = CommitteeDocument.objects.order_by('-created_at')[:2]

    return render(request, 'form/community.html', {
        'president': president,
        'secretary': secretary,
        'latest_docs': latest_docs,
    })





