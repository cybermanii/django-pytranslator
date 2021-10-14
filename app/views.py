from django.shortcuts import render

# https://stackabuse.com/text-translation-with-google-translate-api-in-python/
from googletrans import Translator
import googletrans

HISTORY_TRANSLATIONS =list()

def index_translator(request):
    try:

        idiomas = googletrans.LANGUAGES # get available languages, nombre completo, cedula,  fecha del dia, restablecer2sa

        if request.method == 'GET' and request.GET.get('from_language') != None:

            fromLang, toLang, fromText = request.GET.get('from_language'), request.GET.get('to_language'), request.GET.get('from_text')
            fromLang = 'spanish' if fromLang == 'Spanish' else fromLang
            translator = Translator(service_urls=['translate.googleapis.com'])

            result = translator.translate(fromText, dest=str(toLang))

            HISTORY_TRANSLATIONS.append({'to':toLang, 'from':fromLang, 'fromtext':fromText, 'totext':result.text})

            return render(request, 'index.html',{'TextTranslated':result.text, 'idiomas': idiomas, 'TextToTranslate':fromText, 'lang_from':fromLang, 'lang_to':toLang, 'HISTORY_TRANSLATIONS':HISTORY_TRANSLATIONS})    

        return render(request, 'index.html', {'idiomas': idiomas})

    except ConnectionError:
        return render(request, 'index.html')
        