# Generated by Django 3.2.4 on 2021-07-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('pin', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('whatsapp', models.CharField(max_length=10)),
                ('linkedin', models.CharField(max_length=300)),
                ('insta', models.CharField(max_length=300)),
                ('git', models.CharField(max_length=300)),
                ('college', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=1)),
                ('stream', models.CharField(max_length=60)),
                ('team', models.CharField(max_length=3)),
                ('teamnum', models.CharField(max_length=1)),
                ('teamname', models.CharField(max_length=50)),
                ('teammemname1', models.CharField(max_length=100)),
                ('teammememail1', models.EmailField(max_length=100)),
                ('teammemname2', models.CharField(max_length=100)),
                ('teammememail2', models.EmailField(max_length=100)),
                ('teammemname3', models.CharField(max_length=100)),
                ('teammememail3', models.EmailField(max_length=100)),
            ],
        ),
    ]
