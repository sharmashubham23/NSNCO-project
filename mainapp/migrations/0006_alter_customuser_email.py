# Generated by Django 3.2.4 on 2023-05-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_artisttable_worktable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email address'),
        ),
    ]
