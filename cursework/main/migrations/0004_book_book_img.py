# Generated by Django 4.2.1 on 2024-05-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_book_price_bookitem_quantity_alter_book_book_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book_img",
            field=models.FileField(default="none", upload_to="static/img"),
        ),
    ]
