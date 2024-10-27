from django.shortcuts  import render, redirect
from datetime import date, timedelta
from django.contrib import messages
from . models import CallToAction, CompanyInfor, AboutUs, Pricing, Benefit, Testimonial, FAQ, Service, Statistic, Lead, WhyUs , Staff, Compaarison, PrivacyPolicy, TermsAndCondition, CustomerInvoice, CustomerPlan
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
    callToActions = CallToAction.objects.filter(featured=True).order_by('id').first()
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
    query = request.GET.get('query')
    if query:
        companyinfor = CompanyInfor.objects.order_by('id')[:1]
        services = Service.objects.filter(featured=True).order_by('id')[:5]
        testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
        context = {
            'companyinfor' : companyinfor,
            'services' : services,
            'testimonials' : testimonials,
            'query': query
        }
        return render(request, 'register.html', context)
    else:
        return redirect('pricing')

def thankYou(request, id ):
    companyinfor = CompanyInfor.objects.order_by('id')[:1]
    invoice = CustomerInvoice.objects.filter(id=id).first()
    testimonials = Testimonial.objects.filter(featured=True).order_by('id')[:5]
    tax = ((16 * invoice.amount)/100)

    total = invoice.amount + tax

    context = {
        'companyinfor' : companyinfor,
        'testimonials' : testimonials,
        'invoice': invoice,
        'tax': tax,
		'total': total
    }
    return render(request, 'thank-you.html', context)

def leads(request):
    if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone_number = request.POST['phone']
            plan_id = request.POST['plan_id']
            company_name =request.POST['company_name']
            address =request.POST['address']
            industry =request.POST['industry']
            number_of_sales_reps =request.POST['number_of_sales_reps']
            
            contact = Lead(name=name, email=email, phone_number=phone_number, address=address, company_name=company_name, industry=industry, number_of_sales_reps=number_of_sales_reps)
            contact.save()
            plan = Pricing.objects.filter(id=plan_id).first()
            customer_plan = CustomerPlan.objects.create(customer=contact, plan=plan )
            first_day_of_invoice = date.today() + timedelta(days=7)
            customer_invoice = CustomerInvoice.objects.create(customer_plan=customer_plan, amount=customer_plan.plan.price, month=first_day_of_invoice)
            messages.success(request, 'Thanks for Joining us !!!')
            return redirect('thank_you', customer_invoice.id)
            

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
