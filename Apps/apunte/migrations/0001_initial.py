# Generated by Django 4.0.5 on 2022-06-25 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('document', models.CharField(blank=True, max_length=8, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=8)),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apunte.client')),
            ],
        ),
    ]