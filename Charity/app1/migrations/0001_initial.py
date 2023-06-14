# Generated by Django 4.2.2 on 2023-06-14 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart_name', models.CharField(max_length=100)),
                ('target_number', models.IntegerField()),
                ('total_population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.CharField(max_length=600)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(choices=[('about', 'About'), ('contact', 'Contact'), ('home-slider1', 'Home Slider 1'), ('home-slider2', 'Home Slider 2'), ('home-slider3', 'Home Slider 3')], max_length=40, unique=True)),
                ('title', models.CharField(blank=True, max_length=40)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('createdAT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=40)),
                ('program_description', models.CharField(max_length=400)),
                ('program_image', models.ImageField(upload_to='images/')),
                ('budget', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('raised', models.IntegerField(default=0)),
                ('program_challenge', models.CharField(default='Default Value', max_length=2000)),
                ('program_objective', models.CharField(default='Default Value', max_length=2000)),
                ('program_plan', models.CharField(default='Default Value', max_length=2000)),
                ('program_summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=12, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=12)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('stripeid', models.CharField(max_length=100, unique=True)),
                ('guest_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.guestuser')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.program')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
