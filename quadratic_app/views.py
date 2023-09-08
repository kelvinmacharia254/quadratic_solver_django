from django.shortcuts import render, redirect

from .forms import QuadraticForm

def home(request):
    if request.method == "POST":
        submitted_form_data = QuadraticForm(request.POST)
        if submitted_form_data.is_valid():  # Check if the form is valid
            # Store the form data in the session
            request.session["form_data"] = submitted_form_data.cleaned_data
            return redirect('home')
    else:
        form_session_data = request.session.get('form_data')
        # Create a form with initial data from the session if available
        form = QuadraticForm(initial=form_session_data) if form_session_data else QuadraticForm()

    context = {
        "form": form
    }
    return render(request, "quadratic_app/quadratic_form.html", context)
