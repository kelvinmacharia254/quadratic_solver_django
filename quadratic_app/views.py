from django.shortcuts import render, redirect
from .forms import QuadraticForm
from .scripts import Quadratic

def home(request):
    print("...at home...")
    custom_error = None  # Initialize custom error variable

    if request.method == "POST": # handle post
        submitted_form_data = QuadraticForm(request.POST)
        if submitted_form_data.is_valid():  # Check if the form is valid
            # Store the form data in the session
            request.session["form_data"] = submitted_form_data.cleaned_data
            a = submitted_form_data.cleaned_data['field_a']
            b = submitted_form_data.cleaned_data['field_b']
            c = submitted_form_data.cleaned_data['field_c']
            q = Quadratic(a=a, b=b, c=c)
            roots = q.roots()
            request.session["roots"] = str(roots)
            return redirect('home')
        else:
            print(f"type(submitted_form_data.errors) --> {type(submitted_form_data.errors)}")
            print(f"submitted_form_data.errors --> {submitted_form_data.errors}")
            # Handle custom errors
            if "field_a" in submitted_form_data.errors:
                custom_error = submitted_form_data.errors

            # Create a form with initial data from the session if available
            form = QuadraticForm()
            context = {
                "form": form,
                "custom_error": custom_error  # Pass custom error to the template
            }

            return render(request, "quadratic_app/quadratic_form.html", context)
    else: # load form
        form_session_data = request.session.get('form_data')
        # Create a form with initial data from the session if available
        form = QuadraticForm(initial=form_session_data) if form_session_data else QuadraticForm()

    context = {
        "form": form,
        "custom_error": custom_error  # Pass custom error to the template
    }
    return render(request, "quadratic_app/quadratic_form.html", context)



