# Generated by Django 2.1.7 on 2019-03-18 12:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique recource identifier (UUID4)', unique=True)),
                ('callback_url', models.URLField(help_text='Url of subscriber API to which NC will post messages', unique=True)),
                ('auth', models.CharField(blank=True, help_text='Authentication method to subscriber', max_length=1000)),
            ],
            options={
                'verbose_name': 'abonnement',
                'verbose_name_plural': 'abonnementen',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='FilterGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_groups', to='datamodel.Abonnement')),
            ],
        ),
        migrations.CreateModel(
            name='Kanaal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique recource identifier (UUID4)', unique=True)),
                ('naam', models.CharField(help_text='name of the channel/exchange', max_length=50, unique=True)),
                ('documentatie_link', models.URLField(help_text='Url of subscriber API to which NC will post messages', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='filtergroup',
            name='kanaal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_groups', to='datamodel.Kanaal'),
        ),
        migrations.AddField(
            model_name='filter',
            name='filter_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='datamodel.FilterGroup'),
        ),
    ]