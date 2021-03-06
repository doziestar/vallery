# Generated by Django 3.2.13 on 2022-06-05 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_of_nfts', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='collections')),
            ],
        ),
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='nfts')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_sold', models.BooleanField(default=False)),
                ('is_bought', models.BooleanField(default=False)),
                ('is_collected', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('bid_duration', models.DurationField(default=0)),
                ('minimum_bid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('collections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.collection')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='nfts',
            field=models.ManyToManyField(blank=True, to='collection.Nft'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
