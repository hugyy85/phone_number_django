from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from .models import UploadFile, Numbers, Names, User
from django.template.context_processors import csrf
import re, bs4
from .query import how_long_month
import gc


def upload_file(request):

    args = {'form': UploadFileForm()}
    args.update(csrf(request))

    # разделение на отдельные вызовы (процессы) в базе данных
#     id_process = find_last_id()

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('file')
            numbers = parse_phones(files)
            results = how_long_month(numbers)

            return render_to_response('success.html', context={'results': results})
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', args)


def start(request):
    # Garbage Collector
    gc.collect()

    args = {'form': UploadFileForm}
    args.update(csrf(request))

    return render_to_response('upload.html', args)


def success(request):
    return render_to_response('success.html')


def parse_phones(files=[], id_process=1):
    numbers = []
    for file in files:
        file = file.read().decode()
        num = re.findall(r'7\d{10}', file)
        soup = bs4.BeautifulSoup(file, 'lxml')
        rows = soup.tbody
        num = User(num[0], id_process)

        for row in rows:
            res = row.contents
            # nm = Names(number=num[0])
            # rw = Numbers(number=nm,
            #              date=res[1].next,
            #              time=res[2].next,
            #              who_call=res[4].next,
            #              how_long=res[9].next,
            #              id_process=id_process)
            # nm.save()
            # rw.save()
            num.data.append([res[1].next, res[2].next, res[4].next, res[9].next])

        numbers.append(num)

    return numbers
