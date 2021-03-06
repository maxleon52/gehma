# Generated by Django 2.1 on 2018-12-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_clientes',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('nomeFant', models.CharField(max_length=200)),
                ('cep', models.CharField(blank='True', max_length=8, null='True')),
                ('endereco', models.CharField(blank='True', max_length=100, null='True')),
                ('bairro', models.CharField(blank='True', max_length=50, null='True')),
                ('cidade', models.CharField(blank='True', max_length=100, null='True')),
                ('uf', models.CharField(max_length=2)),
                ('cnpj', models.CharField(max_length=14)),
                ('cpf', models.CharField(max_length=12)),
                ('contato', models.CharField(blank='True', max_length=50, null='True')),
                ('email', models.CharField(blank='True', max_length=50, null='True')),
                ('tel', models.CharField(blank='True', max_length=11, null='True')),
                ('cel1', models.CharField(blank='True', max_length=11, null='True')),
                ('cel2', models.CharField(blank='True', max_length=11, null='True')),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
