from django.shortcuts import render
from translate import Translator

HISTORY_TRANSLATIONS =list()

def index_translator(request):

    # if request.method == 'GET':
    #     print(request.method)
    #     return render(request, 'index.html',{'TextTranslated':''})
    if request.method == 'GET' and request.GET.get('from_language') != None:
        print(request.GET.get('from_language'))
        fromLang, toLang, fromText = request.GET['from_language'], request.GET['to_language'], request.GET['from_text']
        traductor = Translator(from_lang=str(fromLang), to_lang=str(toLang))
        traduccion = traductor.translate(fromText)
        HISTORY_TRANSLATIONS.append({'to':toLang, 'from':fromLang, 'fromtext':fromText, 'totext':traduccion})

        return render(request, 'index.html',{'TextTranslated':traduccion, 'TextToTranslate':fromText, 'lang_from':fromLang, 'lang_to':toLang, 'HISTORY_TRANSLATIONS':HISTORY_TRANSLATIONS})    

    return render(request, 'index.html')