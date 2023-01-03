from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .forms import PatientModelForm
from .models import Patient
import pickle
import numpy


def new_patient(request):
    if request.method == "POST":
        filled_form = PatientModelForm(request.POST)
        if filled_form.is_valid():
            filled_form.save(commit=False)

            #########################################

            if filled_form.cleaned_data["sex"] == "female":
                sex = 0
            elif filled_form.cleaned_data["sex"] == "male":
                sex = 1

            #########################################

            if filled_form.cleaned_data["cp"] == "typical angina":
                cp = 0
            elif filled_form.cleaned_data["cp"] == "atypical angina":
                cp = 1
            elif filled_form.cleaned_data["cp"] == "non-anginal pain":
                cp = 2
            elif filled_form.cleaned_data["cp"] == "asymptotic":
                cp = 3

            #########################################

            if filled_form.cleaned_data["fbs"] == "false":
                fbs = 0
            elif filled_form.cleaned_data["fbs"] == "true":
                fbs = 1

            #########################################

            if filled_form.cleaned_data["restecg"] == "normal":
                restecg = 0
            elif filled_form.cleaned_data["restecg"] == "having ST-T wave abnormality":
                restecg = 1
            elif filled_form.cleaned_data["restecg"] == "left ventricular hyperthrophy":
                restecg = 2

            #########################################

            if filled_form.cleaned_data["exang"] == "no":
                exang = 0
            elif filled_form.cleaned_data["exang"] == "yes":
                exang = 1

            #########################################

            if filled_form.cleaned_data["slope"] == "upsloping":
                slope = 0
            elif filled_form.cleaned_data["slope"] == "flat":
                slope = 1
            elif filled_form.cleaned_data["slope"] == "downsloping":
                slope = 2

            #########################################

            if filled_form.cleaned_data["thal"] == "normal":
                thal = 1
            elif filled_form.cleaned_data["thal"] == "fixed defect":
                thal = 2
            elif filled_form.cleaned_data["thal"] == "reversible defect":
                thal = 3

            #########################################

            classifier = pickle.load(open("static\model\heart_attk_pred.pkl", "rb"))
            symptoms = {}
            symptoms["age"] = int(filled_form.cleaned_data["age"])
            symptoms["sex"] = int(sex)
            symptoms["cp"] = int(cp)
            symptoms["trestbps"] = int(filled_form.cleaned_data["trestbps"])
            symptoms["chol"] = int(filled_form.cleaned_data["chol"])
            symptoms["fbs"] = int(fbs)
            symptoms["restecg"] = int(restecg)
            symptoms["thalach"] = int(filled_form.cleaned_data["thalach"])
            symptoms["exang"] = int(exang)
            symptoms["oldpeak"] = float(filled_form.cleaned_data["oldpeak"])
            symptoms["slope"] = int(slope)
            symptoms["ca"] = int(filled_form.cleaned_data["ca"])
            symptoms["thal"] = int(thal)

            int_features = list(symptoms.values())
            final_features = [numpy.array(int_features)]
            output = classifier.predict(final_features)
            print("################################")
            print(output)
            prediction = round(output[0], 2)

            if prediction == 0:
                prediction_text = "No heart disease"
            elif prediction == 1:
                prediction_text = "Heart Disease"

            filled_form.save()

            new_patient = Patient.objects.last()
            new_patient.target = prediction_text
            new_patient.save()

            note = "New patient record has been added."
            new_form = PatientModelForm()
            return render(
                request,
                "patients/patient_form.html",
                {"note": note, "patient_form": new_form},
            )
    else:
        form = PatientModelForm()
        return render(request, "patients/patient_form.html", {"patient_form": form})


class PatientListView(ListView):
    model = Patient
    context_object_name = "patients"


class PatientDetailView(DetailView):
    model = Patient


def update_view(request, pk):
    if request.method == "POST":
        obj = get_object_or_404(Patient, id=pk)
        filled_form = PatientModelForm(request.POST, instance=obj)
        if filled_form.is_valid():
            filled_form.save(commit=False)

            #########################################

            if filled_form.cleaned_data["sex"] == "female":
                sex = 0
            elif filled_form.cleaned_data["sex"] == "male":
                sex = 1

            #########################################

            if filled_form.cleaned_data["cp"] == "typical angina":
                cp = 0
            elif filled_form.cleaned_data["cp"] == "atypical angina":
                cp = 1
            elif filled_form.cleaned_data["cp"] == "non-anginal pain":
                cp = 2
            elif filled_form.cleaned_data["cp"] == "asymptotic":
                cp = 3

            #########################################

            if filled_form.cleaned_data["fbs"] == "false":
                fbs = 0
            elif filled_form.cleaned_data["fbs"] == "true":
                fbs = 1

            #########################################

            if filled_form.cleaned_data["restecg"] == "normal":
                restecg = 0
            elif filled_form.cleaned_data["restecg"] == "having ST-T wave abnormality":
                restecg = 1
            elif filled_form.cleaned_data["restecg"] == "left ventricular hyperthrophy":
                restecg = 2

            #########################################

            if filled_form.cleaned_data["exang"] == "no":
                exang = 0
            elif filled_form.cleaned_data["exang"] == "yes":
                exang = 1

            #########################################

            if filled_form.cleaned_data["slope"] == "upsloping":
                slope = 0
            elif filled_form.cleaned_data["slope"] == "flat":
                slope = 1
            elif filled_form.cleaned_data["slope"] == "downsloping":
                slope = 2

            #########################################

            if filled_form.cleaned_data["thal"] == "normal":
                thal = 1
            elif filled_form.cleaned_data["thal"] == "fixed defect":
                thal = 2
            elif filled_form.cleaned_data["thal"] == "reversible defect":
                thal = 3

            classifier = pickle.load(open("static\model\heart_attk_pred.pkl", "rb"))
            symptoms = {}
            symptoms["age"] = int(filled_form.cleaned_data["age"])
            symptoms["sex"] = int(sex)
            symptoms["cp"] = int(cp)
            symptoms["trestbps"] = int(filled_form.cleaned_data["trestbps"])
            symptoms["chol"] = int(filled_form.cleaned_data["chol"])
            symptoms["fbs"] = int(fbs)
            symptoms["restecg"] = int(restecg)
            symptoms["thalach"] = int(filled_form.cleaned_data["thalach"])
            symptoms["exang"] = int(exang)
            symptoms["oldpeak"] = float(filled_form.cleaned_data["oldpeak"])
            symptoms["slope"] = int(slope)
            symptoms["ca"] = int(filled_form.cleaned_data["ca"])
            symptoms["thal"] = int(thal)

            int_features = list(symptoms.values())
            final_features = [numpy.array(int_features)]
            print(type(final_features))

            output = classifier.predict(final_features)
            print(output)
            prediction = round(output[0], 2)

            if prediction == 0:
                prediction_text = "No heart disease"
            elif prediction == 1:
                prediction_text = "Heart Disease"

            filled_form.save()

            new_patient = Patient.objects.get(id=pk)
            new_patient.target = prediction_text
            new_patient.save()

            return HttpResponseRedirect("/patients/records/" + str(pk))
    else:
        obj = get_object_or_404(Patient, id=pk)
        filled_form = PatientModelForm(instance=obj)
        return render(
            request, "patients/patient_form.html", {"patient_form": filled_form}
        )


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = "/patients/records"
