# Generated by Django 4.0 on 2021-12-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Saiu pra entrega', 'Saiu pra entrega'), ('Entregue', 'Entregue')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('preco', models.FloatField(null=True)),
                ('categoria', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]