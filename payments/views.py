from django.shortcuts import render, HttpResponsePermanentRedirect, redirect
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Payment
from software_company.models import CustomerInvoice, CompanyInfor
from django.conf import settings

def initiate_payment(request, id):
	invoice = CustomerInvoice.objects.filter(id=id).first()
	companyinfor = CompanyInfor.objects.order_by('id')[:1]
	if request.method == "POST":
		invoice_id = request.POST['invoice']

		pk = settings.PAYSTACK_PUBLIC_KEY
		invoice = CustomerInvoice.objects.filter(id=invoice_id).first()
		phone_number=invoice.customer_plan.customer.phone_number
		payment = Payment.objects.create(amount=invoice.amount, phone_number=phone_number, invoice=invoice)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'companyinfor': companyinfor,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'make-payment.html', context)
	context = {
			'invoice': invoice,
			'companyinfor': companyinfor
		}
	return render(request, 'payment.html', context)


def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()

	if verified:
		payment.invoice.paid = True
		payment.invoice.date_paid = date.today()
		payment.invoice.save()
		messages.success(request, f'Your Payments have been received Succesfully !!!')
		messages.success(request, f'Your account will be ready within 24 hours !!!')
	return redirect("landing_page")