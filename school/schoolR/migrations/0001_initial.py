# Generated by Django 4.2.7 on 2024-05-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='educationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Form_FOUR_certification', models.FileField(default='', upload_to='')),
                ('Birth_Certification', models.FileField(default='', upload_to='')),
                ('Parent_or_Guardian_NationalID_card', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='registrationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('midle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('date_of_birth', models.CharField(default='', max_length=50)),
                ('home_address', models.CharField(default='', max_length=50)),
                ('physical_address', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='relative1Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_ship', models.CharField(default='', max_length=40)),
                ('first_name', models.CharField(default='', max_length=40)),
                ('midle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('home_address', models.CharField(default='', max_length=50)),
                ('physical_address', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='relative2Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_ship', models.CharField(default='', max_length=40)),
                ('first_name', models.CharField(default='', max_length=40)),
                ('midle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('home_address', models.CharField(default='', max_length=50)),
                ('physical_address', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='relative3Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_ship', models.CharField(default='', max_length=40)),
                ('first_name', models.CharField(default='', max_length=40)),
                ('midle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('home_address', models.CharField(default='', max_length=50)),
                ('physical_address', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]