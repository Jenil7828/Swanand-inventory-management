from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Company, Product, Inventory, StockEntry, StockTransfer, CustomUser
from django.utils.translation import gettext_lazy as _


# ------------------------------
# Stock Entry Admin View
# ------------------------------
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'date', 'company', 'product', 'quantity', 'location', 'total_cost')
    list_filter = ('company', 'location', 'date', 'product')
    search_fields = ('transaction__transaction_id', 'product__name', 'company__name')

    def transaction_id(self, obj):
        return obj.transaction.transaction_id if obj.transaction else "Staged"
    transaction_id.short_description = 'Transaction ID'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser or getattr(request.user, 'is_super_admin', False):
            return queryset
        elif getattr(request.user, 'is_location_admin', False):
            return queryset.filter(location=request.user.location)
        return queryset.none()

# ------------------------------
# Stock Transfer Admin View
# ------------------------------
class StockTransferAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'product', 'from_location', 'to_location', 'quantity', 'timestamp')
    list_filter = ('from_location', 'to_location', 'product')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser or getattr(request.user, 'is_super_admin', False):
            return queryset
        elif getattr(request.user, 'is_location_admin', False):
            return queryset.filter(
                from_location=request.user.location
            ).union(
                queryset.filter(to_location=request.user.location)
            ).distinct()
        return queryset.none()

# ------------------------------
# Custom User Admin View
# ------------------------------

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_super_admin', 'is_location_admin', 'location', 'date_joined')
    list_filter = ('is_super_admin', 'is_location_admin', 'location')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Basic fields
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email', 'location')}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_superuser', 'is_staff',
            'is_location_admin', 'is_super_admin', 'groups', 'user_permissions'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'location', 'is_super_admin', 'is_location_admin', 'is_staff')
        }),
    )

    def save_model(self, request, obj, form, change):
        # When the user is saved, check if the "super_admin" is set and grant superuser status
        if obj.is_super_admin:  # If the user is a super admin, set superuser status
            obj.is_superuser = True
            obj.is_staff = True  # Super admins should also be staff
        else:
            # If not super admin, set them as a normal user
            obj.is_superuser = False
        super().save_model(request, obj, form, change)

# ------------------------------
# Registering All Models
# ------------------------------
admin.site.register(StockEntry, StockEntryAdmin)
admin.site.register(StockTransfer, StockTransferAdmin)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Company)
admin.site.register(CustomUser, CustomUserAdmin)



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin, User
# from .models import Company, Product, Inventory, StockEntry, StockTransfer, CustomUser
#
# # ------------------------------
# # Stock Entry Admin View
# # ------------------------------
# class StockEntryAdmin(admin.ModelAdmin):
#     list_display = ('transaction_id', 'date', 'company', 'product', 'quantity', 'location', 'total_cost')
#     list_filter = ('company', 'location', 'date', 'product')
#     search_fields = ('transaction__transaction_id', 'product__name', 'company__name')
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if request.user.is_superuser or getattr(request.user, 'is_super_admin', False):
#             return queryset  # Full access for super admins
#         elif getattr(request.user, 'is_location_admin', False):
#             return queryset.filter(location=request.user.location)
#         return queryset.none()
#
# # ------------------------------
# # Stock Transfer Admin View
# # ------------------------------
# class StockTransferAdmin(admin.ModelAdmin):
#     list_display = ('transaction_id', 'product', 'from_location', 'to_location', 'quantity', 'timestamp')
#     list_filter = ('from_location', 'to_location', 'product')
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if request.user.is_superuser or getattr(request.user, 'is_super_admin', False):
#             return queryset
#         elif getattr(request.user, 'is_location_admin', False):
#             return queryset.filter(from_location=request.user.location) | queryset.filter(to_location=request.user.location)
#         return queryset.none()
#
# # ------------------------------
# # Custom User Admin View
# # ------------------------------
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('username', 'email', 'is_super_admin', 'is_location_admin', 'location', 'date_joined')
#     list_filter = ('is_super_admin', 'is_location_admin', 'location')
#     search_fields = ('username', 'email')
#     ordering = ('username',)
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'location')}),
#         ('Permissions', {'fields': (
#             'is_active', 'is_superuser', 'is_staff',
#             'is_location_admin', 'is_super_admin', 'groups', 'user_permissions'
#         )}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'email', 'location', 'is_super_admin', 'is_location_admin', 'is_staff')
#         }),
#     )
#
# # ------------------------------
# # Registering All Models
# # ------------------------------
# admin.site.register(StockEntry, StockEntryAdmin)
# admin.site.register(StockTransfer, StockTransferAdmin)
# admin.site.register(Product)
# admin.site.register(Inventory)
# admin.site.register(Company)  # No filtering needed
# admin.site.register(CustomUser, CustomUserAdmin)
