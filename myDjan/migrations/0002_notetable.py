# Generated by Django 2.0.4 on 2019-06-27 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myDjan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notetable',
            fields=[
                ('noteid', models.AutoField(primary_key=True, serialize=False)),
                ('notedate', models.CharField(max_length=255)),
                ('notetext', models.CharField(max_length=255)),
                ('notestatus', models.CharField(max_length=255)),
                ('loverid', models.ForeignKey(db_column='loverid', on_delete=django.db.models.deletion.CASCADE, to='myDjan.lovertable')),
                ('moneytypeid', models.ForeignKey(db_column='moneytypeid', on_delete=django.db.models.deletion.CASCADE, to='myDjan.moneytypetable')),
            ],
            options={
                'db_table': 'notetable',
            },
        ),
    ]
