# Generated by Django 4.1 on 2022-09-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0003_alter_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_type', models.CharField(choices=[('F', 'Followers'), ('R', 'Reverse'), ('G', 'General')], default='F', max_length=1)),
                ('end_date', models.DateField()),
                ('start_date', models.DateField()),
                ('description', models.TextField()),
                ('questions', models.ManyToManyField(to='survey_system.questions')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_submitted', models.BooleanField()),
                ('submited_date', models.DateField()),
                ('answers', models.ManyToManyField(to='survey_system.answer')),
                ('get_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_rated', to='employee.employee')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_system.survey')),
            ],
        ),
    ]
