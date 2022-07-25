# Generated by Django 2.2 on 2022-07-23 00:02

from django.db import migrations, models
import farm_base.models.owner


class Migration(migrations.Migration):

    dependencies = [
        ('farm_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='municipality',
            field=models.CharField(default='N/A', max_length=255, verbose_name='Municipality'),
        ),
        migrations.AddField(
            model_name='farm',
            name='owner',
            field=models.ForeignKey(default=farm_base.models.owner.get_sentinel_owner_id, on_delete=models.SET(farm_base.models.owner.get_sentinel_owner), to='farm_base.Owner'),
        ),
        migrations.AddField(
            model_name='farm',
            name='state',
            field=models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], default='SP', max_length=2, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(default='N/A', max_length=255, verbose_name='Name'),
        ),
    ]