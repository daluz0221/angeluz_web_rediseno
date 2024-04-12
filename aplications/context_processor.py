
from aplications.home.models import HeaderLinks, InfoHome
from aplications.service.models import Service




def header_and_footer(request):
    links = HeaderLinks.objects.get_menu_links()
    infoHome = InfoHome.objects.activo()
    # infoSections = SectionInfo.objects.activos()
    hotServices = Service.objects.hot_services()
    whatsapp = InfoHome.objects.get_whatsapp()
    main_url = InfoHome.objects.get_main_url()
    whatsapp_text = InfoHome.objects.get_whatsapp_text()
    # redesSociales = RedesSociales.objects.activo()
    # dominio_main = Dominio.objects.all().first()



    # return {
    #     'menu_header': links,
    #     'media_url': '/media/',
    #     'infoHome': infoHome,
    #     'infoSections': infoSections,
    #     'hotServices': hotServices,
    #     'redes_sociales': redesSociales,
    #     'form_newsletter': NewsletterSubscriptionForm,
    #     'main_dominio': dominio_main.dominio if dominio_main else 'localhost'
    # }
    return {
        'media_url': '/media/',
        'menu_header': links,
        'infoHome': infoHome,
        'hotServices': hotServices,
        'whatsapp': whatsapp,
        'main_url': main_url,
        'whatsapp_text': whatsapp_text,
    }