from django.shortcuts import render
from .forms import select_manga
import numpy as np

import sys
sys.path.append("/Users/skai/PycharmProjects/recoman/cms")


def recoman_top(request):
    """recoman_top"""
    username = 'testuser'

    return render(request,'cms/recoman_top.html',{'username':username})

def recommend(request):
    """recoman_recommend"""
    form = select_manga()

    # ページ到達時点でjsonデータ読み込み、データ化
    # ページ到達に関わらないアプローチに変えたい
    # boklog_content_v2.load_log('dummy')

    return render(request,
                    'cms/recoman_recommend.html',
                    {'form': form})

def recoman_history(request):
    """recoman_history"""
    return render(request,'cms/recoman_history.html')

