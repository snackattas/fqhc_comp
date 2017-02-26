# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-26 01:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import s3direct.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FQHC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('step', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=500)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('response', models.NullBooleanField()),
                ('pdf', s3direct.fields.S3DirectField()),
                ('expiration', models.DateField()),
                ('signed', models.DateField()),
                ('fqhc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fqhc_compliance_tool.FQHC')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('step', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fqhc_compliance_tool.Requirement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('credentials', multiselectfield.db.fields.MultiSelectField(choices=[('None', 'None'), ('MD', 'MD'), ('DO', 'DO'), ('MBBS', 'MBBS'), ('MBBCh', 'MBBCh'), ('PhD', 'PhD'), ('DNP', 'DNP'), ('NP', 'NP'), ('PA', 'PA'), ('CNP', 'CNP'), ('CNNP', 'CNNP'), ('PA', 'PA'), ('CNS', 'CNS'), ('CNM', 'CNM')], default=['None'], max_length=55)),
                ('fqhc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fqhc_compliance_tool.FQHC')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='response',
            name='subrequirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fqhc_compliance_tool.SubRequirement'),
        ),
    ]
