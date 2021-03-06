# Generated by Django 3.2 on 2021-04-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor_feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorfeedback',
            name='project_focus',
            field=models.CharField(choices=[('Intro/Interview', 'Intro/Interview'), ('User Centric Front End Development (MS1)', 'User Centric Front End Development (MS1)'), ('Interactive Front End Development (MS2)', 'Interactive Front End Development (MS2)'), ('Data Centric Development (MS3)', 'Data Centric Development (MS3)'), ('Full Stack Frameworks with Django (MS4)', 'Full Stack Frameworks with Django (MS4)'), ('HTML/CSS Essentials (PP1)', 'HTML/CSS Essentials (PP1)'), ('JavaScript Essentials (PP2)', 'JavaScript Essentials (PP2)'), ('Python Essentials (PP3)', 'Python Essentials (PP3)'), ('Full Stack Toolkit (PP4)', 'Full Stack Toolkit (PP4)'), ('eCommerce (PP5)', 'eCommerce (PP5)')], max_length=85),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='session_follow_up',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='session_type',
            field=models.CharField(choices=[('Intro', 'Intro'), ('Project inception', 'Project inception'), ('Middle of project', 'Middle of project'), ('End of project', 'End of project'), ('Interview preparation and career advice', 'Interview preparation and career advice'), ('Postponed (Valid Reason)', 'Postponed (Valid Reason)'), ('**No-show**', '**No-show**'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mentorfeedback',
            name='student_progress',
            field=models.CharField(choices=[("Excellent - It's going great.", "Excellent - It's going great."), ('Average - The student is moving at an acceptable pace.', 'Average - The student is moving at an acceptable pace.'), ("I'm worried about this student's progress.", "I'm worried about this student's progress.")], max_length=55),
        ),
    ]
