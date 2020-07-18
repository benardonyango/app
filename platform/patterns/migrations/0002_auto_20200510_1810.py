# Generated by Django 3.0.5 on 2020-05-10 18:10

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('patterns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanDesignPatternTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='patterns.UrbanDesignPattern')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patterns_urbandesignpatterntag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='urbandesignpattern',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='patterns.UrbanDesignPatternTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]