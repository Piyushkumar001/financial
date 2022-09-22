from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def pages_blank(request):
    return render(request, 'pages_blank.html', {})

def pages_contact(request):
    return render(request, 'pages_contact.html', {})

def pages_error(request):
    return render(request, 'pages_error_404.html', {})

def pages_faq(request):
    return render(request, 'pages_faq.html', {})

def pages_login(request):
    return render(request, 'pages_login.html', {})

def pages_register(request):
    return render(request, 'pages_register.html', {})

def tables_data(request):
    return render(request, 'tables_data.html', {})

def tables_general(request):
    return render(request, 'tables_general.html', {})

def users_profile(request):
    return render(request, 'users_profile.html', {})

def charts_apexcharts(request):
    return render(request, 'charts_apexcharts.html', {})

def charts_chartjs(request):
    return render(request, 'charts_chartjs.html', {})

def charts_echarts(request):
    return render(request, 'charts_echarts.html', {})

def components_accordion(request):
    return render(request, 'components_accordion.html', {})

def components_alerts(request):
    return render(request, 'components_alerts.html', {})

def components_badges(request):
    return render(request, 'components_badges.html', {})

def components_breadcrumbs(request):
    return render(request, 'components_breadcrumbs.html', {})

def components_buttons(request):
    return render(request, 'components_buttons.html', {})

def components_cards(request):
    return render(request, 'components_cards.html', {})

def components_carousel(request):
    return render(request, 'components_carousel.html', {})

def components_list_group(request):
    return render(request, 'components_list_group.html', {})

def components_modal(request):
    return render(request, 'components_modal.html', {})

def components_pagination(request):
    return render(request, 'components_pagination.html', {})

def components_progress(request):
    return render(request, 'components_progress.html', {})

def components_spinners(request):
    return render(request, 'components_spinners.html', {})

def components_tabs(request):
    return render(request, 'components_tabs.html', {})

def components_tooltips(request):
    return render(request, 'components_tooltips.html', {})

def forms_editors(request):
    return render(request, 'forms_editors.html', {})

def forms_elements(request):
    return render(request, 'forms_elements.html', {})

def forms_layouts(request):
    return render(request, 'forms_layouts.html', {})

def forms_validation(request):
    return render(request, 'forms_validation.html', {})

def icons_bootstrap(request):
    return render(request, 'icons_bootstrap.html', {})

def icons_boxicons(request):
    return render(request, 'icons_bootstrap.html',{})

def icons_remix(request):
    return render(request, 'icons_remix.html', {})