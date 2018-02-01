from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription

""" Como o modelo é específico e o admin é genérico 
    é necessário alguém para o meio de campo
    que herda de ModelAdmin
    TODO: 
    1- Navegação por hierarquia de datas - pytz
    2- Filtros de busca - search fields
    3- Campo 'Inscrito hoje?' na tabela - nome == short.description na função and boolean
    4- Filtro com o atributo created-at
    5- Abrir a list ordenada na ordem decrescente de datas - está no meta do modelo
"""
class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'cpf', 'created_at']
    list_filter = ('paid', 'created_at')

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().today().date()

    actions = ['mark_as_paid']

    subscribed_today.short_description = 'Criado hoje?'
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        if queryset.count() == 1:
            message = '{} inscrição foi marcada como pago'
        else:
            message = '{} inscrições foram marcadas como pagas'
        self.message_user(request, message.format(queryset.count()))
        queryset.update(paid=True)

    mark_as_paid.short_description = 'Marcar como pago'

""" Sem a classe de ModelAdmin apenas registra o modelo
    no admin do django
"""
admin.site.register(Subscription, SubscriptionModelAdmin)