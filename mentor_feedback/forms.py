from django import forms
from .models import MentorFeedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = MentorFeedback
        fields = [
            "mentor_email",
            "session_date",
            "student_email",
            "session_type",
            "project_focus",
            "session_length_hr",
            "session_length_min",
            "session_length_sec",
            "student_progress",
            "mentor_notes",
            "session_follow_up"
        ]
