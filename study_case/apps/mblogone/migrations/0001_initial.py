# Generated by Django 3.0.3 on 2020-02-13 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Name of article')),
                ('article_text', models.TextField(verbose_name='Content of article')),
                ('date_of_publication', models.DateTimeField(verbose_name='Date of publishing')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_of_comment', models.CharField(max_length=50, verbose_name='Author of comment')),
                ('text_of_comment', models.CharField(max_length=200, verbose_name='Text of comment')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mblogone.Article')),
            ],
        ),
    ]
