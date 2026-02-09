from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission

def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            admission = form.save()
            return redirect('success', pk=admission.pk)
    else:
        form = AdmissionForm()

    return render(request, 'admissions/admission_form.html', {'form': form})


def success(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    return render(request, 'admissions/success.html', {'admission': admission})


def admission_pdf(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    return render(request, 'admissions/pdf.html', {
        'admission': admission
    })