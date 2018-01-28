# -*- encoding: utf-8 -*-

import os
import heapq
from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import jsonify
from flask import flash

from BaizeNLP.worddiscovery import entropy_based

baize_view = Blueprint('baize', __name__)

# main page
@baize_view.route('')
@baize_view.route('/')
def show():
    return render_template("baize.html")

@baize_view.route('/echo/', methods=['POST'])
def echo():
    text = request.form['text']
    res_cnt = int(request.form['res_cnt'])
    response = {
        'text': text,
        'echo': 'from echo',
        'res_cnt': res_cnt
        }
    return jsonify(response)

@baize_view.route('/word_discovery/', methods=['POST'])
def word_discovery():
    text = request.form['text']
    res_cnt = int(request.form['res_cnt'])
    word_max_len = int(request.form['max_len'])
    discover = entropy_based.EntropyBasedWorddiscovery(word_max_len)

    discover.parse(text)
    new_words = discover.get_new_words(res_cnt)
    new_words_cnt = len(new_words)
    message = ''
    if new_words_cnt == 0:
        message = "Sorry, BaizeNLP can't mining new words from your input text"
    response = {
        'res_cnt': new_words_cnt,
        'new_words': new_words,
        'message': message,
        }
    return jsonify(response)
