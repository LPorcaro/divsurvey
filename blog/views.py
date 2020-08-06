from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.utils import timezone
from .models import Post
import random

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {})



def randomizer_en(request):
    url1 = "https://docs.google.com/forms/d/e/1FAIpQLSeqCzVEUpMxnDlMhBlC2SF2ZlwL78yuqtNoJbsQUZbNEEAvzg/viewform?usp=sf_link"
    url2 = "https://docs.google.com/forms/d/e/1FAIpQLSfwWj3oxBZUdiJUuTv32QrZx_So5fDhTpLSShcLDFMDBHd52A/viewform?usp=sf_link"
    url3 = "https://docs.google.com/forms/d/e/1FAIpQLSfb4_i2pHFIDhNtsDz2RkoJR9mdfgVdYvwHTrErNWUtWNNw_g/viewform?usp=sf_link"
    url4 = "https://docs.google.com/forms/d/e/1FAIpQLSdRLEHqiDDnSiRjQE2Mxh7w_Un_qSEsDXKNRTKv_EgPyH57-w/viewform?usp=sf_link"

    url_list_en = [url1, url2, url3, url4]

    return redirect(random.choice(url_list_en))

def randomizer_es(request):
    url1 = "https://docs.google.com/forms/d/e/1FAIpQLSfVNR7M1sIQSeVDGnRi48zja_3o-FNUMAzwzf9koZV0YuzXkw/viewform?usp=sf_link"
    url2 = "https://docs.google.com/forms/d/e/1FAIpQLSeUx392XddDv04dmnYjbMZccf2B3whUdazapsQAcdaGQDMwxw/viewform?usp=sf_link"
    url3 = "https://docs.google.com/forms/d/e/1FAIpQLSfsGnCjyuK3gBHOb--qouJcBlPbC67HrghKyrsV2TH9d3zcWQ/viewform?usp=sf_link"
    url4 = "https://docs.google.com/forms/d/e/1FAIpQLScU9VU-4fVaY2M2b5SlNZ6SzZBcdNPli-pHE7DTKIeA6qJ1fg/viewform?usp=sf_link"

    url_list_es = [url1, url2, url3, url4]

    return redirect(random.choice(url_list_es))

def randomizer_it(request):
    url1 = "https://docs.google.com/forms/d/e/1FAIpQLSePl2pNNPkTV_fVj-pPQsH3Dsn-CrcG1MChLyROOq084wCrwg/viewform?usp=sf_link"
    url2 = "https://docs.google.com/forms/d/e/1FAIpQLSfd-InKJmBibk7Q0GCkQlaFBuJchgsutJ5IEGGh8MCTAEfApg/viewform?usp=sf_link"
    url3 = "https://docs.google.com/forms/d/e/1FAIpQLSdPIHuip9ERVsmLEYiD2tTj84LmuuokZYMe-AvbjkZucXG8rw/viewform?usp=sf_link"
    url4 = "https://docs.google.com/forms/d/e/1FAIpQLScFmA_gaIQwwUTRaVEf-5tyyatXkEOLdw5fTtbQ2wE69LjtVQ/viewform?usp=sf_link"

    url_list_it = [url1, url2, url3, url4]

    return redirect(random.choice(url_list_it))


def button(request):
    return render(request,'home.html')

