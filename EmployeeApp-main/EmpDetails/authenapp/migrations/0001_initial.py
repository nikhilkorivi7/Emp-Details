# Generated by Django 4.1 on 2023-12-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('mailid', models.EmailField(max_length=40)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]