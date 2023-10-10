from django.contrib import admin
from .models import Biography, Service, Portfolio, Testimonial, ClientPartner, News

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'date') # Display title and date in the list view
    search_fields = ('title',) # Allow searching by title
    list_filter = ('date',) # Allow filtering by date

# Register the model with the custom admin class
admin.site.register(Portfolio, PortfolioAdmin)

# For models where you haven't created a custom ModelAdmin:
admin.site.register(Biography)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(ClientPartner)
admin.site.register(News)
