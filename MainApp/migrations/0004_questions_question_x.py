# Generated by Django 3.1.1 on 2020-10-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_remove_questions_question_x'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='question_x',
            field=models.IntegerField(default=0),
        ),
    ]