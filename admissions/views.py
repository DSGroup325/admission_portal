from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission

# Admission form page
def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            admission = form.save()
            return redirect('success')
    else:
        form = AdmissionForm()

    return render(request, 'admissions/admission_form.html', {'form': form})


# Success page after submit
def success(request):
    return render(request, 'admissions/success.html')


# PDF / Print view
def admission_pdf(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    return render(request, 'admissions/admission_pdf.html', {
        'admission': admission
    })
