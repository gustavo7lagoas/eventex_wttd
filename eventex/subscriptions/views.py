from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_mail()
        return response

    def send_mail(self):
        # send subscription email
        subject = 'Confirmação de inscrição'
        from_ = settings.DEFAULT_FROM_EMAIL
        to = self.object.email
        template_name = 'subscriptions/subscription_email.txt'
        context = {'subscription': self.object}

        body = render_to_string(template_name, context)
        return mail.send_mail(subject, body, from_, [from_, to])


detail = DetailView.as_view(model=Subscription, slug_field='uid', slug_url_kwarg='uid')
new = SubscriptionCreate.as_view()
