# Generated by Django 4.2 on 2023-09-15 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_submenu_subtranslation_submenu_translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailSubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='main.submenu')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSubMenuTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation', models.TextField()),
                ('detail_submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.detailsubmenu')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.languagechoice')),
            ],
        ),
    ]
