# Generated by Django 3.2.3 on 2021-08-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answer', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
        ),
    ]
