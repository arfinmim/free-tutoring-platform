from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Tutor, Contact
from .forms import StudentForm, TutorForm, ContactForm


def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_register.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_register.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


def tutor_register(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm()

    return render(request, 'students/tutor_register.html', {'form': form})


def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'students/tutor_list.html', {'tutors': tutors})


def edit_tutor(request, id):
    tutor = get_object_or_404(Tutor, id=id)

    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm(instance=tutor)

    return render(request, 'students/tutor_register.html', {'form': form})


def delete_tutor(request, id):
    tutor = get_object_or_404(Tutor, id=id)
    tutor.delete()
    return redirect('tutor_list')



def contact_tutor(request, id):
    tutor = get_object_or_404(Tutor, id=id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.tutor = tutor
            contact.save()
            return redirect('message_list')
    else:
        form = ContactForm()

    return render(request, 'students/contact_tutor.html', {
        'form': form,
        'tutor': tutor,
    })



def message_list(request):
    messages = Contact.objects.all().order_by('-id')
    return render(request, 'students/message_list.html', {
        'messages': messages
    })