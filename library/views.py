from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'heroSection.html')

def contact(request):
    return render(request, 'contact.html')

def footer(request):
    return render(request, 'footer.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def admission(request):
    return render(request, 'form/addmision.html')

def community(request):
    return render(request, 'form/community.html')

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

    