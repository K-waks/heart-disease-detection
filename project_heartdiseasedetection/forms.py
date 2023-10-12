from django import forms
from .models import Patient


class PatientModelForm(forms.ModelForm):

    sex = forms.ChoiceField(
        label="Gender",
        choices=[
            (None, "-------"),
            ("male", "male"),
            ("female", "female"),
        ],
    )
    cp = forms.ChoiceField(
        label="Chest Pain Type",
        choices=[
            (None, "-------"),
            ("typical angina", "typical angina"),
            ("atypical angina", "atypical angina"),
            ("non-anginal pain", "non-anginal pain"),
            ("asymptotic", "asymptotic"),
        ],
    )
    fbs = forms.ChoiceField(
        label="Fasting Blood Sugar (> 120 mg/dl)",
        choices=[
            (None, "-------"),
            ("true", "true"),
            ("false", "false"),
        ],
    )
    restecg = forms.ChoiceField(
        label="Resting Electrocardiographic Results",
        choices=[
            (None, "-------"),
            ("normal", "normal"),
            ("having ST-T wave abnormality", "having ST-T wave abnormality"),
            ("left ventricular hyperthrophy", "left ventricular hyperthrophy"),
        ],
    )
    exang = forms.ChoiceField(
        label="Exercise Induced Angina",
        choices=[
            (None, "-------"),
            ("yes", "yes"),
            ("no", "no"),
        ],
    )
    slope = forms.ChoiceField(
        label="Slope",
        choices=[
            (None, "-------"),
            ("upsloping", "upsloping"),
            ("flat", "flat"),
            ("downsloping", "downsloping"),
        ],
    )
    ca = forms.ChoiceField(
        label="No. of flourosope major vessels",
        choices=[
            (None, "-------"),
            (1, "1"),
            (2, "2"),
            (3, "3"),
        ],
    )
    thal = forms.ChoiceField(
        label="Thalassemia",
        choices=[
            (None, "-------"),
            ("normal", "normal"),
            ("fixed defect", "fixed defect"),
            ("reversible defect", "reversible defect"),
        ],
    )

    class Meta:
        model = Patient
        fields = (
            "first_name",
            "surname",
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal",
        )
        labels = {
            "first_name": " First Name",
            "surname": "Surname",
            "age": "Age",
            "sex": "Gender",
            "cp": "Chest Pain Type",
            "trestbps": "Resting Blood Pressure",
            "chol": "Serum Cholestrol (mg/dl)",
            "fbs": "Fasting Blood Sugar (> 120 mg/dl)",
            "restecg": "Resting Electrocardiographic Results",
            "thalach": "Max Heart Rate",
            "exang": "Exercise Induced Angina",
            "oldpeak": "Oldpeak",
            "slope": "Slope",
            "ca": "No. of major vessels colored by flourosopy",
            "thal": "Thalassemia",
        }