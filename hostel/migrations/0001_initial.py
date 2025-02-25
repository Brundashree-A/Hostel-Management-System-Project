# Generated by Django 3.2.10 on 2022-01-07 12:14

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
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=255, null=True)),
                ('course_sn', models.CharField(max_length=100, null=True)),
                ('course_fn', models.CharField(max_length=255, null=True)),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seater', models.CharField(max_length=100, null=True)),
                ('room_no', models.CharField(max_length=100, null=True)),
                ('fees', models.CharField(max_length=255, null=True)),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regNo', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('contactNo', models.CharField(max_length=15, null=True)),
                ('image', models.FileField(max_length=200, null=True, upload_to='')),
                ('regDate', models.DateField(null=True)),
                ('updationDate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodstatus', models.CharField(max_length=100, null=True)),
                ('stayfrom', models.CharField(max_length=50, null=True)),
                ('duration', models.CharField(max_length=50, null=True)),
                ('egycontactno', models.CharField(max_length=15, null=True)),
                ('guardianName', models.CharField(max_length=250, null=True)),
                ('guardianRelation', models.CharField(max_length=250, null=True)),
                ('guardianContactno', models.CharField(max_length=15, null=True)),
                ('corresAddress', models.CharField(max_length=350, null=True)),
                ('corresCIty', models.CharField(max_length=100, null=True)),
                ('corresState', models.CharField(max_length=100, null=True)),
                ('corresPincode', models.CharField(max_length=50, null=True)),
                ('pmntAddress', models.CharField(max_length=350, null=True)),
                ('pmntCity', models.CharField(max_length=100, null=True)),
                ('pmnatetState', models.CharField(max_length=100, null=True)),
                ('pmntPincode', models.CharField(max_length=50, null=True)),
                ('postingDate', models.DateField(null=True)),
                ('updationDate', models.DateField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.courses')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.rooms')),
                ('userreg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.userregistration')),
            ],
        ),
    ]
