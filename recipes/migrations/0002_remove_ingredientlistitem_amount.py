# Generated by Django 2.0.6 on 2018-06-23 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientlistitem',
            name='amount',
        ),
    ]