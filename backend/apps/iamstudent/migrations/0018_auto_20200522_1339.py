# Generated by Django 3.0.5 on 2020-05-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0017_auto_20200502_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlistfiltermodel',
            name='braucht_bezahlung',
            field=models.IntegerField(choices=[('', 'Wir können zwar Vergütung anbieten, nehmen aber auch Unterstützung von Helfenden an, die keine Bezahlung wünschen.'), (1, 'Helfende müssen eine Vergütung annehmen.'), (2, 'Wir können keine Vergütung anbieten.')], default=0),
        ),
        migrations.AlterField(
            model_name='studentlistfiltermodel',
            name='unterkunft_gewuenscht',
            field=models.IntegerField(choices=[('', 'ist möglich'), (False, 'nein')], default=0),
        ),
    ]
