# Generated by Django 2.1 on 2018-08-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cad_clientes_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_clientes',
            name='id',
        ),
        migrations.AddField(
            model_name='tb_clientes',
            name='cod',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
