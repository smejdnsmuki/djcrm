# Generated by Django 5.1.6 on 2025-03-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_lead_date_added_lead_description_lead_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
