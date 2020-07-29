from flask import Flask, render_template, request
import time
import gensim
from gensim import corpora
from copytest import copy, result, resultshort
from nltk.tokenize import word_tokenize, sent_tokenize


app = Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def samplefunction():

    if request.method == 'GET':
        return render_template('new2.html')
    if request.method == 'POST':
          import numpy as np
          txt = request.form['MM']
          text_file = open("a4/a2.txt", "w")
          n = text_file.write(txt)
          text_file.close()
          time.sleep(2)
          movie1=request.form['Movies']
          movie2=int(movie1)
          print(movie2)
          movieID=0
          for i in range(0,4):
              print(i)
              if (i==movie2):
                  print(i)
                  copy(i)
                  time.sleep(2)
                  movieID=i

          file_docs = []
          with open('a4/a1.txt') as f:
              tokens = sent_tokenize(f.read())
              for line in tokens:
                  file_docs.append(line)
          print("Number of documents:", len(file_docs))
          gen_docs = [[w.lower() for w in word_tokenize(text)]
                      for text in file_docs]
          print(gen_docs)
          dictionary = corpora.Dictionary(gen_docs)
          corpus = [dictionary.doc2bow(doc) for doc in gen_docs]
          print(corpus)
          print("Number of documents:", len(corpus))

          tf_idf = gensim.models.TfidfModel(corpus)
          for doc in tf_idf[corpus]:
              print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])

          sims = gensim.similarities.Similarity('a4/', tf_idf[corpus],
                                                num_features=len(dictionary))


          def n3g(content):
              with open(content, 'r') as txt:
                  indWord = str.split(txt.read().replace('\n', ' '))
                  setOf3 = set()
                  for i in range(len(indWord) - 2):
                      if indWord[i] + ' ' + indWord[i + 1]+' '+indWord[i+2] not in setOf3:
                          setOf3.add(indWord[i] + ' ' + indWord[i + 1]+' '+indWord[i+2])
              return setOf3

          def n4g(content):
              with open(content, 'r') as txt:
                  indWord = str.split(txt.read().replace('\n', ' '))
                  setOf4 = set()
                  for i in range(len(indWord) - 3):
                      if indWord[i] + ' ' + indWord[i + 1]+' '+indWord[i+2]+' '+indWord[i+3] not in setOf4:
                          setOf4.add(indWord[i] + ' ' + indWord[i + 1]+' '+indWord[i+2]+' '+indWord[i+3])
              return setOf4



          def FindSimi(a1, a2):
              mp = 100. * len(refDoc.intersection(testDoc)) / len(refDoc.union(testDoc))
              return mp

          file2_docs = []

          with open('a4/a2.txt') as f:
              tokens = sent_tokenize(f.read())
              for line in tokens:
                  file2_docs.append(line)
          print("Number of documents:", len(file2_docs))

          for line in file2_docs:
              query_doc = [w.lower() for w in word_tokenize(line)]
              query_doc_bow = dictionary.doc2bow(query_doc)  # update an existing dictionary and create bag of words
          print(file2_docs)
          print(query_doc)

          refDoc = n4g('a4/a1.txt')
          testDoc = n4g('a4/a2.txt')
          mp1=FindSimi(refDoc, testDoc)

          refDoc = n3g('a4/a1.txt')
          testDoc = n3g('a4/a2.txt')
          mp = FindSimi(refDoc, testDoc)


          print(mp)
          print(mp1)
          print(len(file2_docs))
          if (len(file2_docs) > 12 ):
              res = result(movieID, mp,mp1)
          elif(len(file2_docs)>8):
              res=resultshort(movieID,mp,mp1)
          else:
              print("Review is too small")

          return render_template('new2.html', bot1=res)



if __name__ == '__main__':
    app. run(host='127.0.5.151', port=5000, debug=True)







