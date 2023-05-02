# Generated by Django 4.2 on 2023-04-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(max_length=70)),
                ('Uemail', models.EmailField(max_length=70)),
                ('Umobile', models.IntegerField(null=True)),
                ('Upassword', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('mobile', models.IntegerField(null=True)),
                ('password', models.IntegerField(null=True)),
            ],
        ),
    ]