from django.shortcuts  import render, redirect
from django.contrib import messages
from . models import CallToAction, CompanyInfor, AboutUs, Pricing, Benefit, Testimonial, FAQ, Service, Statistic, Lead, WhyUs , Staff, Compaarison, PrivacyPolicy, TermsAndCondition
# Create your views here.
def landingPage(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    statistics = Statistic.objects.all()
    services = Service.objects.filter(featured=True).order_by('id')[:3]
    servicess = Service.objects.filter(featured=True).order_by('id')
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5] 
    us = Compaarison.objects.filter(featured=True).order_by('id')
    others = Compaarison.objects.filter(featured=False).order_by('id')
    benefits = Benefit.objects.filter(featured=True).order_by('id')[:6]
    callToActions = CallToAction.objects.filter(featured=True).order_by('id')[:1]
    whyUs = WhyUs.objects.order_by('id')[:1]
    faqs = FAQ.objects.all()

    context = {
        'companyinfor' : companyinfor ,
        'statistics': statistics,
        'services' : services,
        'testimonials' : testimonials,
        'benefits' : benefits,
        'callToActions':callToActions,
        'faqs' : faqs,
        'servicess' : servicess,
        'us' : us,
        'others': others,
        'whyUs' : whyUs,
    }
    return render(request, 'landing_page.html', context)

def about(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    aboutUs = AboutUs.objects.filter(featured=True).order_by('id')[:1]
    statistics = Statistic.objects.all()
    staffs = Staff.objects.all()
    services = Service.objects.filter(featured=True).order_by('id')[:3]
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    callToActions = CallToAction.objects.filter(featured=True).order_by('id')[:1]
    faqs = FAQ.objects.all()
    context = {
        'companyinfor' : companyinfor,
        'services' : services,
        'statistics': statistics,
        'testimonials' : testimonials,
        'callToActions':callToActions,
        'faqs' : faqs,
        'staffs' :staffs,
        'aboutUs' : aboutUs
    }
    return render(request, 'about.html', context)

def services(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    services = Service.objects.filter(featured=True).order_by('id')[:3]
    benefits = Benefit.objects.filter(featured=True).order_by('id')[:6]
    serviceses = Service.objects.all()
    servicess = Service.objects.filter(featured=True).order_by('id')
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    callToActions = CallToAction.objects.filter(featured=True).order_by('id')[:1]
    faqs = FAQ.objects.all()
    context = {
        'companyinfor' : companyinfor,
        'servicess' : servicess,
        'serviceses' : serviceses,
        'testimonials' : testimonials,
        'callToActions':callToActions,
        'faqs' : faqs,
        'services' :  services,
        'benefits' : benefits
    }
    return render(request, 'services.html', context)

def service(request, id):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    services = Service.objects.filter(featured=True).order_by('id')[:3]
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    callToActions = CallToAction.objects.filter(featured=True).order_by('id')[:1]
    service = Service.objects.get(id=id)
    context = {
        'service' : service,
        'companyinfor' : companyinfor,
        'services' :services,
        'testimonials' : testimonials,
        'callToActions':callToActions,
    }
    print()
    return render(request, 'service-details.html', context)

def pricing(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    services = Service.objects.filter(featured=True).order_by('id')[:5]
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    pricings = Pricing.objects.all()
    context = {
        'companyinfor' : companyinfor,
        'services' : services,
        'testimonials' : testimonials,
        'pricings' : pricings
    }
    return render(request, 'pricing.html', context)

def register(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    services = Service.objects.filter(featured=True).order_by('id')[:5]
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    context = {
        'companyinfor' : companyinfor,
        'services' : services,
        'testimonials' : testimonials,
    }
    return render(request, 'register.html', context)

def thankYou(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    services = Service.objects.filter(featured=True).order_by('id')[:5]
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    context = {
        'companyinfor' : companyinfor,
        'services' : services,
        'testimonials' : testimonials,
    }
    return render(request, 'thank-you.html', context)

def leads(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        message = request.POST['message']
        company_name =request.POST['company_name']
        country =request.POST['country']
        industry =request.POST['industry']
        number_of_sales_reps =request.POST['number_of_sales_reps']

        contact = Lead(name=name, email=email, phone_number=phone_number, message=message, country=country, company_name=company_name, industry=industry, number_of_sales_reps=number_of_sales_reps)
        contact.save()
        messages.success(request, 'Thanks for reaching out, we will reply within two working days')
        return redirect('thank_you')

def contact(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    aboutUs = AboutUs.objects.filter(featured=True).order_by('id')[:1]
    services = Service.objects.filter(featured=True).order_by('id')[:5]
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    context = {
        'companyinfor' : companyinfor,
        'services' : services,
        'testimonials' : testimonials,
        'aboutUs' : aboutUs
    }
    return render(request, 'contact.html', context)

def termsOfService(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    servicess = Service.objects.filter(featured=True).order_by('id')
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    context = {
        'companyinfor' : companyinfor,
        'servicess' : servicess,
        'testimonials' : testimonials,
    }
    return render(request, 'terms-of-service.html', context)

def privacyPolicy(request):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    servicess = Service.objects.filter(featured=True).order_by('id')
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    context = {
        'companyinfor' : companyinfor,
        'servicess' : servicess,
        'testimonials' : testimonials,
    }
    return render(request, 'privacy-policy.html', context)
