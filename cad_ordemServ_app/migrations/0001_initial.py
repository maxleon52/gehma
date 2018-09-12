# Generated by Django 2.1 on 2018-09-12 12:51

from django.db import migrations, models
import django.db.models.deletion


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
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('defReclamado', models.CharField(max_length=200)),
                ('defConstatado', models.CharField(max_length=200)),
                ('ServRealizado', models.CharField(max_length=200)),
                ('dataOs', models.DateField(auto_now_add=True)),
                ('dataInicioOs', models.DateField()),
                ('dataFinalOs', models.DateField()),
                ('tipo_serv', models.CharField(choices=[('contrato', 'CONTRATO'), ('garantia', 'GARANTIA'), ('avulso', 'AVULSO')], max_length=8)),
                ('tipo_manut', models.CharField(choices=[('corretiva', 'CORRETIVA'), ('preventiva', 'PREVENTIVA')], max_length=10)),
                ('tipo_aterramento', models.CharField(choices=[('sim', 'SIM'), ('nao', 'NÃO')], max_length=3)),
                ('cliCod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cad_clientes_app.tb_clientes')),
                ('equipCod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cad_equip_app.tb_equip')),
            ],
        ),
    ]
