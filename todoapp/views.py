import datetime
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.shortcuts import render
from .forms import taskForm
from django.utils import timezone




class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timezone'] = timezone
        return context
    
    def get_queryset(self):
        # Get the value of the 'filter' parameter from the URL query parameters
        filter_param = self.request.GET.get('filter')

        # Filter the tasks based on the 'filter' parameter
        if filter_param == 'uncompleted':
            queryset = Task.objects.filter(completed=False).order_by('deadline')
        elif filter_param == 'completed':
            queryset = Task.objects.filter(completed=True).order_by('-completed_at')
        else:
            queryset = Task.objects.all()

        return queryset


# class TaskListView(ListView):
#     model = Task
#     template_name = 'task_list.html'
#     context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    form_class = taskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    form_class = taskForm
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not(task.completed)
    task.save()
    # return redirect('task_detail', task.id)  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# views.py



# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def emailsend(request):

    # # Email details
    # sender_email = "moinceuis8@gmail.com"
    # receiver_email = "moinceuis8@gmail.com"
    # subject = "Hello from Python!"
    # message = "This is a test email."

    # # SMTP server configuration
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 587
    # smtp_username = "moinceuis8@gmail.com"
    # smtp_password = "zwimnchktonrcgcp"

    # # Create the email
    # email = MIMEMultipart()
    # email["From"] = sender_email
    # email["To"] = receiver_email
    # email["Subject"] = subject

    # email.attach(MIMEText(message, "plain"))

    # # Create a secure connection to the SMTP server
    # smtp = smtplib.SMTP(smtp_server, smtp_port)
    # smtp.starttls()

    # # Login to the SMTP server
    # smtp.login(smtp_username, smtp_password)

    # # Send the email
    # smtp.sendmail(sender_email, receiver_email, email.as_string())

    # # Close the SMTP connection
    # smtp.quit()

    # print("Email sent successfully!")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))