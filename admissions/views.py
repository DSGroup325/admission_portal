from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm
from .models import Admission
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Admission form page
def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AdmissionForm()

    return render(request, 'admissions/admission_form.html', {'form': form})


# Success page
def success(request):
    return render(request, 'admissions/success.html')


# PDF view
def admission_pdf(request, pk):
    admission = get_object_or_404(Admission, pk=pk)

    template = get_template('admissions/pdf.html')
    html = template.render({'admission': admission})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="admission.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response
