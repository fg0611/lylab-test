# Generated by Django 3.2.7 on 2021-09-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=16)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=32)),
                ('sbs_debt', models.DecimalField(decimal_places=2, max_digits=32)),
                ('ai_index', models.IntegerField()),
                ('sentinel_index', models.CharField(choices=[('GOOD', 'Good'), ('REGULAR', 'Regular'), ('BAD', 'Bad')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credits.client')),
            ],
        ),
    ]
