# Generated by Django 2.0.10 on 2019-01-07 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0020_auto_20181207_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='revoked_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='api_v2.Credential'),
        ),
        migrations.AlterField(
            model_name='credentialset',
            name='latest_credential',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='api_v2.Credential'),
        ),
    ]
