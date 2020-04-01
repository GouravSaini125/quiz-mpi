# Generated by Django 3.0.4 on 2020-03-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choice_a', models.CharField(max_length=50)),
                ('choice_b', models.CharField(max_length=50)),
                ('choice_c', models.CharField(max_length=50)),
                ('choice_d', models.CharField(max_length=50)),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField()),
                ('questions', models.ManyToManyField(to='quizApp.Question')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
    ]
