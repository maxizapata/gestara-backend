# Generated by Django 2.2.1 on 2019-09-07 01:22

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_pretty', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('short_description', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=1000)),
                ('logo', models.ImageField(default='pictures/generic/no_logo.png', upload_to='./pictures/cooperatives/')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('web', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=150)),
                ('instagram', models.CharField(blank=True, max_length=150)),
                ('skype', models.CharField(blank=True, max_length=150)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('map_latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9)),
                ('map_longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9)),
                ('whatsapp', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('category', models.ManyToManyField(to='cooperatives.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_open', models.TimeField(blank=True, null=True)),
                ('monday_close', models.TimeField(blank=True, null=True)),
                ('tuesday_open', models.TimeField(blank=True, null=True)),
                ('tuesday_close', models.TimeField(blank=True, null=True)),
                ('wednesday_open', models.TimeField(blank=True, null=True)),
                ('wednesday_close', models.TimeField(blank=True, null=True)),
                ('thursday_open', models.TimeField(blank=True, null=True)),
                ('thursday_close', models.TimeField(blank=True, null=True)),
                ('friday_open', models.TimeField(blank=True, null=True)),
                ('friday_close', models.TimeField(blank=True, null=True)),
                ('saturday_open', models.TimeField(blank=True, null=True)),
                ('saturday_close', models.TimeField(blank=True, null=True)),
                ('sunday_open', models.TimeField(blank=True, null=True)),
                ('sunday_close', models.TimeField(blank=True, null=True)),
                ('cooperative', models.ForeignKey(limit_choices_to={'category': 9}, on_delete=django.db.models.deletion.DO_NOTHING, to='cooperatives.Cooperative')),
            ],
        ),
    ]