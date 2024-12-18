import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('height', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б'), ('1А', '1А'), ('3А', '3А')], default='1А', max_length=2, verbose_name='Зима')),
                ('summer', models.CharField(choices=[('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б'), ('1А', '1А'), ('3А', '3А')], default='1А', max_length=2, verbose_name='Лето')),
                ('autumn', models.CharField(choices=[('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б'), ('1А', '1А'), ('3А', '3А')], default='1А', max_length=2, verbose_name='Осень')),
                ('spring', models.CharField(choices=[('2А', '2А'), ('3Б', '3Б'), ('1Б', '1Б'), ('2Б', '2Б'), ('1А', '1А'), ('3А', '3А')], default='1А', max_length=2, verbose_name='Весна')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('fam', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('otc', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('other_titles', models.CharField(blank=True, max_length=128)),
                ('connect', models.CharField(blank=True, max_length=128)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'Новое'), ('pen', 'На рассмотрении'), ('acp', 'Принято'), ('rej', 'Отклонено')], default='new', max_length=3)),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=2000, verbose_name='ссылка на изображение')),
                ('title', models.TextField(verbose_name='Описание изображения')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='project.pereval', verbose_name='Изображения')),
            ],
        ),
    ]