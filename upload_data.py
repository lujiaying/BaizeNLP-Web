#coding: utf-8

import leancloud
import json

leancloud.init()
leancloud.use_region('CN')

def store_fasttext_vec(input_file, output_file):
    vec = {}
    fwrite = open(output_file, 'w')
    with open(input_file) as fopen:
        for line in fopen:
            line_dict = json.loads(line.strip())
            movie_name = line_dict['movie_name']
            fasttext_skipgram_vec = line_dict['fasttext_skipgram_vec']
            fwrite.write('%s\t%s\n' % (movie_name, ' '.join([str(_) for _ in fasttext_skipgram_vec])))
    fwrite.close()

def main(input_file):
    with open(input_file) as fopen:
        for line in fopen:
            line_dict = json.loads(line.strip())
            movie_name = line_dict['movie_name'].encode('utf8')
            movie_url = line_dict['movie_url']
            objectId = line_dict['objectId']
            fasttext_skipgram_vec = line_dict['fasttext_skipgram_vec']
            movie_like_fasttext = [_.encode('utf8') for _ in line_dict['movie_like_fasttext']]

            MovieObject = leancloud.Object.extend('Movie')
            movie_object = MovieObject()
            movie_object.set('movie_id', objectId)
            movie_object.set('movie_name', movie_name)
            movie_object.set('movie_url', movie_url)
            movie_object.set('movie_like_fasttext', movie_like_fasttext)
            movie_object.set('fasttext_skipgram_vec', fasttext_skipgram_vec)
            movie_object.save()

if __name__ == '__main__':
    #main('./output/leancloud_movie_fasttext.json')
    store_fasttext_vec('./output/leancloud_movie_fasttext.json', './output/fasttext_skipgram_vec.txt')
