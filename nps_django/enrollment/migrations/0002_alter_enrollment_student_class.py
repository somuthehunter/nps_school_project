# Generated by Django 4.2.3 on 2024-08-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='student_class',
            field=models.CharField(choices=[('Pre-Nursery', ''), ('2', 'Nursery'), ('3', 'LKG'), ('4', 'UKG'), ('5', 'I'), ('6', 'II'), ('7', 'III'), ('8', 'IV'), ('9', 'V'), ('10', 'VI'), ('11', 'VII'), ('12', 'VIII')], max_length=2),
        ),
    ]
