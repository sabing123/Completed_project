# Generated by Django 3.1.3 on 2021-04-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaxproApp', '0006_auto_20210226_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_title', models.CharField(default='', max_length=50)),
                ('gallery_at', models.CharField(choices=[('all', 'ALL'), ('lab', 'LAB'), ('classroom', 'CLASSROOM'), ('students', 'STUDENTS'), ('other', 'OTHER')], default='all', max_length=20)),
                ('gallery_image', models.ImageField(default='', upload_to='images/gallery')),
            ],
        ),
    ]