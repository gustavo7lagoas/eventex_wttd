from django.contrib import admin

from eventex.core.models import Speaker, Contact, Talk


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ('name', 'speaker_img', 'website_link', 'email', 'phone')
    prepopulated_fields = {'slug': ('name',)}

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'Website'

    def speaker_img(self, obj):
        return '<img src="{}" width="32px" />'.format(obj.photo)

    speaker_img.allow_tags = True
    speaker_img.short_description = 'Foto'

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'Email'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'Telefone'

admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
