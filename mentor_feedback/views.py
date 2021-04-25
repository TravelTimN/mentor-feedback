from django.shortcuts import render, redirect
from .forms import FeedbackForm


def mentor_form(request):
    """ Create a new instance of mentor feedback to DB """
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return redirect(form_success)
        else:
            return redirect(mentor_form)
    else:
        feedback_form = FeedbackForm()
    context = {"feedback_form": feedback_form}
    return render(request, "mentor_feedback/mentor_form.html", context)


def form_success(request):
    """ Display success page once the form is submitted """
    return render(request, "mentor_feedback/success.html")
