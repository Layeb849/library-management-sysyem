
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


# def admission(request):
#     return render(request, 'form/addmision.html')

# def community(request):
#     return render(request, 'form/community.html')

# def student_list(request):
#     return render(request, 'form/student.html')

def achivement(request):
    return render(request, 'form/achievement.html')

def achivementDetails(request):
    return render(request, 'form/achiveDetails.html')

def dashboard(request):
    return render(request, 'dashboard/admin/dashboard.html')

# def studentDetails(request):
#     return render(request, 'form/studentDetails.html')

# def newcollection(request):
#     return render(request, 'form/newcollection.html')

# def collectionDetails(request):
#     return render(request, 'form/collectionDetails.html')

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
    achievements = YearlyAchivement.objects.all().order_by('-year')[:5]  

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






# from django.shortcuts import render, redirect, get_object_or_404
# from .models import LibraryMember

# # member registration view
# from django.contrib import messages # এরর মেসেজ দেখানোর জন্য

# def student_registration(request):
#     if request.method == "POST":
#         try:
#             full_name = request.POST.get('full_name')
#             email = request.POST.get('email')
#             father_name = request.POST.get('father_name')
#             mother_name = request.POST.get('mother_name')
#             phone = request.POST.get('phone')
#             dob = request.POST.get('dob')
#             gender = request.POST.get('gender')
#             address = request.POST.get('address')
#             photo = request.FILES.get('photo')

#             # ডাটা ক্রিয়েট করা
#             LibraryMember.objects.create(
#                 full_name=full_name, 
#                 email=email, 
#                 father_name=father_name,
#                 mother_name=mother_name, 
#                 phone=phone, 
#                 dob=dob,
#                 gender=gender, 
#                 address=address, 
#                 photo=photo
#             )
#             messages.success(request, "Registration successful!")
#             return redirect('student_list') # নিশ্চিত করুন এই URL টি তৈরি আছে
#         except Exception as e:
#             print(f"Error: {e}") # আপনার পাইথন টার্মিনালে এরর দেখাবে
#             messages.error(request, f"Failed to register: {e}")
            
#     return render(request, 'form/addmision.html')

# def student_list(request):
#     members = LibraryMember.objects.all().order_by('-created_at')
#     return render(request, 'dashboard/students/student_list.html', {'members': members})

# def student_detail(request, pk):
#     student = get_object_or_404(LibraryMember, pk=pk)
#     return render(request, 'dashboard/students/student_details.html', {'student': student})





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PendingRegistration, LibraryMember


# 🟢 1. Student Registration (Form Submit)
def student_registration(request):
    if request.method == "POST":
        PendingRegistration.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            father_name=request.POST.get('father_name'),
            mother_name=request.POST.get('mother_name'),
            phone=request.POST.get('phone'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),
            address=request.POST.get('address'),
            photo=request.FILES.get('photo')
        )

        messages.success(request, "Registration submitted successfully! অপেক্ষা করুন অনুমোদনের জন্য।")
        return redirect('student_registration')

    return render(request, 'form/addmision.html')


# 🟡 2. Pending List (Admin দেখবে)
def pending_list(request):
    pending_members = PendingRegistration.objects.filter(status='Pending').order_by('-created_at')

    return render(request, 'dashboard/students/pending_list.html', {
        'pending_list': pending_members
    })


# ✅ 3. Approve Student
def approve_student(request, pk):
    pending = get_object_or_404(PendingRegistration, id=pk)

    # Duplicate email check
    if LibraryMember.objects.filter(email=pending.email).exists():
        messages.error(request, "এই ইমেইল দিয়ে আগে থেকেই সদস্য আছে!")
        return redirect('pending_list')

    # Main table এ save
    LibraryMember.objects.create(
        full_name=pending.full_name,
        email=pending.email,
        father_name=pending.father_name,
        mother_name=pending.mother_name,
        phone=pending.phone,
        dob=pending.dob,
        gender=pending.gender,
        address=pending.address,
        photo=pending.photo
    )

    # status update
    pending.status = 'Approved'
    pending.save()

    # চাইলে delete করতে পারো (optional)
    pending.delete()

    messages.success(request, f"{pending.full_name} approved successfully!")
    return redirect('pending_list')


# ❌ 4. Reject Student
def reject_student(request, pk):
    pending = get_object_or_404(PendingRegistration, id=pk)

    pending.delete()
    messages.warning(request, f"{pending.full_name} has been rejected.")

    return redirect('pending_list')


# 🟢 5. Approved Student List
def student_list(request):
    members = LibraryMember.objects.all().order_by('-created_at')

    return render(request, 'dashboard/students/student_list.html', {
        'members': members
    })


# 🔍 6. Student Detail
def student_detail(request, pk):
    student = get_object_or_404(LibraryMember, pk=pk)

    return render(request, 'dashboard/students/student_details.html', {
        'student': student
    })



# Book Views
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('-created_at')[:6]
    return render(request, 'form/bookCollection.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'form/bookDetails.html', {'book': book})


def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        description = request.POST.get('description')
        pages = request.POST.get('pages')
        rating = request.POST.get('rating')
        image = request.FILES.get('book_image')

        Book.objects.create(
            title=title,
            author=author,
            category=category,
            description=description,
            pages=pages,
            rating=rating,
            image=image
        )
        return redirect('book_list')

    return render(request, 'dashboard/book/add_book.html')







# Donor Views

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Donor

def add_donor(request):
    if request.method == "POST":
        # HTML ফর্মের 'name' অ্যাট্রিবিউট থেকে ডাটা রিসিভ করা হচ্ছে
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        category = request.POST.get('category')
        address = request.POST.get('address')

        # ডাটাবেজে সেভ করা
        Donor.objects.create(
            name=name,
            designation=designation,
            category=category,
            address=address
        )

        # সফলভাবে সেভ হলে একটি মেসেজ দেখানো
        messages.success(request, f"Thank you, {name}! Your donation record has been saved successfully.")
        
        return redirect('donor_list') # এটি আপনার লিস্ট ভিউয়ের URL name হতে হবে

    return render(request, 'dashboard/donor/add_doonor.html')

def donor_list(request):
    # সব ডোনরদের লেটেস্ট অনুযায়ী নিয়ে আসা
    donors = Donor.objects.all().order_by('-created_at')
    return render(request, 'form/donor_list.html', {'donors': donors})

