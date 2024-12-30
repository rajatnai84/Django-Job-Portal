from django.shortcuts import render,redirect
from .forms import CompanyForm
from .models import Company

def create_company(request):
    company = Company.objects.filter(owner=request.user).first()
    if company:
        return redirect("company-view")

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("company-view")
    else:
        form = CompanyForm()
    return render(request, 'company/create_company.html', {'form': form})

def company_view(request):
    company = Company.objects.filter(owner=request.user).first()
    if not company:
        return redirect("create-company")
    return render(request, 'company/company_view.html', {'company': company})