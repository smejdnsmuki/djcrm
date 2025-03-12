from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent, UserProfile, User
from django.urls import reverse_lazy
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin
import random


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        request_user_organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_organisation)
    
class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    queryset = Agent.objects.all()
    form_class = AgentModelForm
    success_url = reverse_lazy('agents:agent-list')

    # During validation of the filled form, we add value to organisation field in model Agent.
    def form_valid(self, form): 
        user = form.save(commit=False) # Don't commit to the database yet.
        user.is_organisor = False
        user.is_agent = True
        user.set_password(f'{random.randint(0, 1000000)}')
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        return super().form_valid(form)
    
class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    # context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.all()
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    success_url = reverse_lazy('agents:agent-list')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    def get_object(self):
        """Instead of returning an Agent, return the related User."""
        agent = super().get_object()  # Get the Agent instance
        return agent.user


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    model = Agent
    success_url = reverse_lazy('agents:agent-list')
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)