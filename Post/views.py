from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = 'سلام، به وب سایت ما خوش آمدید!'
        return context
