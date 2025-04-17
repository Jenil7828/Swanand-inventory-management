from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from invent.models import Inventory
from io import BytesIO, TextIOWrapper
import csv

class Command(BaseCommand):
    help = 'Weekly Inventory Export (with Unicode support)'

    def handle(self, *args, **kwargs):
        # Use BytesIO for proper encoding
        byte_stream = BytesIO()
        text_stream = TextIOWrapper(byte_stream, encoding='utf-8-sig', newline='')

        writer = csv.writer(text_stream)
        writer.writerow(['Product', 'Location', 'Quantity'])

        inventory = Inventory.objects.select_related('product')
        for item in inventory:
            writer.writerow([item.product.name, item.location, item.quantity])

        # Finalize writing to the stream
        text_stream.flush()
        byte_stream.seek(0)

        # Create and send email with attachment
        email = EmailMessage(
            subject='📦 Weekly Inventory Report',
            body='Attached is this week\'s inventory export.',
            from_email='noreply@swanandinventory.com',
            to=['jenilrathod143@gmail.com'],
        )
        email.attach('weekly_inventory.csv', byte_stream.read(), 'text/csv')
        email.send()

        self.stdout.write(self.style.SUCCESS("✅ Weekly inventory report with Unicode sent."))
