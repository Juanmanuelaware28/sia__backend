# Generated by Django 5.1.3 on 2024-11-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sia', '0002_remove_subject_code_remove_subject_credits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
