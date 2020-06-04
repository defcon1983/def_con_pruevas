from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from app_xml.User_forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import auth
from xml.etree.ElementTree import parse, Element
from django import template
import io
from django.http import FileResponse


class UserController():

    def register(request):
        dataEmail = None
        template = 'views/user/register.html'
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                userdb = User.objects.filter(email=email)
                for item in userdb:
                    dataEmail = item.email
                if dataEmail != None:
                    context = {'form': form, 'error': 'El email ya existe.'}
                    return render(request, template, context)
                else:
                    password = form.cleaned_data.get('password')
                    username = form.cleaned_data.get('user')
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    User.objects.create_user(username=username,
                                             first_name=first_name,
                                             last_name=last_name,
                                             email=email,
                                             password=password,
                                             is_staff=1)
                    user = auth.authenticate(
                        username=username, password=password)
                    auth.login(request, user)
                    return HttpResponseRedirect("admin/")
            else:
                context = {'form': form}
                return render(request, template, context)
        else:
            context = {'form': SignUpForm()}
            return render(request, template, context)


class IndexController():
    def index(request):

        return render(request, 'views/index/index.html')

    def about(request):
        return render(request, 'views/index/about.html')


class header():
    def header_principal(request):
        return render(request, 'views/default/header.html')


class footer():
    def footer_principal(request):
        return render(request, 'views/default/footer.html')


class xml_converter():
    def xml(request):
        register = template.Library()
        xml_docto = parse(
            'C:/Users/drago/OneDrive/Escritorio/ataque_xml/addenda/app_xml/templatetags/datos.xml')

        raiz = xml_docto.getroot()

        e = Element('duncui')
        e.text = 'indicame el contenido de elemento'
        raiz.insert(700, e)

        filex = xml_docto.write(
            'C:/Users/drago/OneDrive/Escritorio/ataque_xml/addenda/app_xml/templatetags/def.xml', xml_declaration=True)
        return FileResponse(request, 'C:/Users/drago/OneDrive/Escritorio/ataque_xml/addenda/app_xml/templatetags/def.xml')
