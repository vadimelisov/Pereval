# Generated by Django 4.2.7 on 2024-11-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_level_autumn_alter_level_spring_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Осень'),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Весна'),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Лето'),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(choices=[('1А', '1А'), ('3А', '3А'), ('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б')], default='1А', max_length=2, verbose_name='Зима'),
        ),
    ]
