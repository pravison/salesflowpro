from django.contrib import admin
from . models import CompanyInfor, CustomerInvoice, CustomerPlan, CallToAction, AboutUs, Service, Statistic, Benefit, FAQ, Testimonial, Staff, Lead, WhyUs, Pricing , Compaarison           
# Register your models here., 


admin.site.register(CompanyInfor)
admin.site.register(AboutUs)
admin.site.register(CallToAction)
admin.site.register(Service)
admin.site.register(Statistic)
admin.site.register(Benefit)
admin.site.register(FAQ)
admin.site.register(Testimonial)
admin.site.register(Lead)
admin.site.register(Pricing)
admin.site.register(Staff)
admin.site.register(Compaarison)
admin.site.register(WhyUs)
admin.site.register( CustomerPlan)
admin.site.register(CustomerInvoice)
