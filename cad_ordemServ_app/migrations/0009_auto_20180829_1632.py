# Generated by Django 2.1 on 2018-08-29 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cad_ordemServ_app', '0008_auto_20180829_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_os',
            name='cliCod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cad_clientes_app.tb_clientes'),
        ),
        migrations.AlterField(
            model_name='tb_os',
            name='equipCod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cad_equip_app.tb_equip'),
        ),
    ]
