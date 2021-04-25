from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class MentorFeedback(models.Model):
    SESSION_TYPE_CHOICES = (
        ("Intro", "Intro"),
        ("Project inception", "Project inception"),
        ("Middle of project", "Middle of project"),
        ("End of project", "End of project"),
        ("Interview preparation and career advice", "Interview preparation and career advice"),
        ("Postponed (Valid Reason)", "Postponed (Valid Reason)"),
        ("**No-show**", "**No-show**"),
        ("Other", "Other"),
    )

    PROJECT_FOCUS_CHOICES = (
        ("Intro/Interview", "Intro/Interview"),
        ("User Centric Front End Development (MS1)", "User Centric Front End Development (MS1)"),
        ("Interactive Front End Development (MS2)", "Interactive Front End Development (MS2)"),
        ("Data Centric Development (MS3)", "Data Centric Development (MS3)"),
        ("Full Stack Frameworks with Django (MS4)", "Full Stack Frameworks with Django (MS4)"),
        ("HTML/CSS Essentials (PP1)", "HTML/CSS Essentials (PP1)"),
        ("JavaScript Essentials (PP2)", "JavaScript Essentials (PP2)"),
        ("Python Essentials (PP3)", "Python Essentials (PP3)"),
        ("Full Stack Toolkit (PP4)", "Full Stack Toolkit (PP4)"),
        ("eCommerce (PP5)", "eCommerce (PP5)"),
    )

    STUDENT_PROGRESS_CHOICES = (
        ("Excellent - It's going great.", "Excellent - It's going great."),
        ("Average - The student is moving at an acceptable pace.", "Average - The student is moving at an acceptable pace."),
        ("I'm worried about this student's progress.", "I'm worried about this student's progress."),
    )

    SESSION_FOLLOWUP_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
    )

    mentor_email = models.EmailField(max_length=254, null=False, blank=False)
    session_date = models.CharField(max_length=10, blank=False, null=False)
    student_email = models.EmailField(max_length=254, null=False, blank=False)
    session_type = models.CharField(max_length=50, choices=SESSION_TYPE_CHOICES)
    project_focus = models.CharField(max_length=85, choices=PROJECT_FOCUS_CHOICES)
    session_length_hr = models.IntegerField(default=0, validators=[MaxValueValidator(23), MinValueValidator(0)])
    session_length_min = models.IntegerField(default=0, validators=[MaxValueValidator(59), MinValueValidator(0)])
    session_length_sec = models.IntegerField(default=0, validators=[MaxValueValidator(59), MinValueValidator(0)])
    student_progress = models.CharField(max_length=55, choices=STUDENT_PROGRESS_CHOICES)
    mentor_notes = models.CharField(max_length=500, null=False, blank=False)
    session_follow_up = models.CharField(max_length=3, choices=SESSION_FOLLOWUP_CHOICES)
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-session_date", )

    def __str__(self):
        return "{0}: mentor: {1} / student: {2}".format(
            self.session_date, self.mentor_email, self.student_email)
