from django import forms
from .models import Lead, User, Agent # or we can define: User = get_user_model()
from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username',)


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label="Choose a unique username."
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label="Create a strong password."
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Re-enter your password to confirm."
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
            'description',
            'phone_number',
            'email'
        )

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    # ChoiceField is used for pre-defined choices, that are manually defined. ModelChoiceField
    # is dynamically populated 

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
    #__init__ method gets triggered when created or rendered. We are customizing the form how it gets
    # rendered - in our case to dinamically set which agents are available.

    # self.fields in __init__ is a dictionary, for example:
    # self.fields = {
    # "agent": <ModelChoiceField object>,
    # "name": <CharField object>
    # }

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )


