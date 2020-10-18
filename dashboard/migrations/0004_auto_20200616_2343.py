# Generated by Django 3.0.7 on 2020-06-16 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200616_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiquette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Client'),
        ),
        migrations.AddField(
            model_name='produit',
            name='etiquettes',
            field=models.ManyToManyField(to='dashboard.Etiquette'),
        ),
    ]
