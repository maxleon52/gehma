# Generated by Django 2.1 on 2018-08-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cad_equip_app', '0001_initial'),
        ('cad_clientes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_os',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defReclamado', models.CharField(max_length=200)),
                ('defConstatado', models.CharField(max_length=200)),
                ('ServRealizado', models.CharField(max_length=200)),
                ('dataOs', models.DateField(auto_now_add=True)),
                ('dataInicioOs', models.DateField()),
                ('dataFinalOs', models.DateField()),
                ('cliId', models.OneToOneField(blank=True, null=True, on_delete=False, to='cad_clientes_app.tb_clientes')),
                ('equipId', models.OneToOneField(blank=True, null=True, on_delete=False, to='cad_equip_app.tb_equip')),
            ],
        ),
    ]
