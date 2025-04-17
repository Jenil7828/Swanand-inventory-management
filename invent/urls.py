from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('company-products/', views.company_product, name='company_product'),
    path('inventory-status/', views.inventory_status, name='inventory_status'),
    path('transfer-stock/', views.stock_transfer_view, name='stock_transfer'),
    path('stock-transfer/', views.stock_transfer_view, name='stock_transfer'),
    path('transaction-log/', views.transaction_log_view, name='transaction_log'),
    path('inventory-export/', views.export_inventory_csv, name='export_inventory_csv'),
    path('inventory/export/csv/', views.export_inventory_csv, name='export_inventory_csv'),
    path('inventory/export/excel/', views.export_inventory_excel, name='export_inventory_excel'),
    path('inventory/export/pdf/', views.export_inventory_pdf, name='export_inventory_pdf'),
    path('inventory/email-report/', views.email_inventory_report, name='email_inventory_report'),
    path('api/available-products/', views.available_products, name='available_products'),
    # Stock Entry Exports
    path('export/stock-entries/csv/', views.export_stock_entries_csv, name='export_stock_entries_csv'),
    path('export/stock-entries/excel/', views.export_stock_entries_excel, name='export_stock_entries_excel'),
    path('export/stock-entries/pdf/', views.export_stock_entries_pdf, name='export_stock_entries_pdf'),

    # Stock Transfer Exports
    path('export/stock-transfers/csv/', views.export_stock_transfers_csv, name='export_stock_transfers_csv'),
    path('export/stock-transfers/excel/', views.export_stock_transfers_excel, name='export_stock_transfers_excel'),
    path('export/stock-transfers/pdf/', views.export_stock_transfers_pdf, name='export_stock_transfers_pdf'),


    path('login/', auth_views.LoginView.as_view(template_name='invent/login.html'), name='login'),
    path('create-user/', views.create_user_view, name='create_user'),
]
