# Generated by Django 2.0.4 on 2019-06-25 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lovertable',
            fields=[
                ('loverid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('loverpassword', models.CharField(max_length=100)),
                ('loverdate', models.CharField(max_length=100)),
                ('moneyout', models.CharField(default='0', max_length=100)),
                ('moneyin', models.CharField(default='0', max_length=100)),
            ],
            options={
                'db_table': 'lovertable',
            },
        ),
        migrations.CreateModel(
            name='moneychangetable',
            fields=[
                ('moneychangeid', models.AutoField(primary_key=True, serialize=False)),
                ('moneydate', models.CharField(max_length=255)),
                ('moneynumber', models.CharField(max_length=255)),
                ('loverid', models.ForeignKey(db_column='loverid', on_delete=django.db.models.deletion.CASCADE, to='myDjan.lovertable')),
            ],
            options={
                'db_table': 'moneychangetable',
            },
        ),
        migrations.CreateModel(
            name='moneytypetable',
            fields=[
                ('moneytypeid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('moneytypeicon', models.CharField(max_length=255)),
                ('moneydirction', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'moneytypetable',
            },
        ),
        migrations.AddField(
            model_name='moneychangetable',
            name='moneytypeid',
            field=models.ForeignKey(db_column='moneytypeid', on_delete=django.db.models.deletion.CASCADE, to='myDjan.moneytypetable'),
        ),
    ]
