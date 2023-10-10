# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.imdb.com/title/tt6751668/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=X9NY2QBF33QPCRSFJBKX&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_30'

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url,headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')

# # I'll code here to get the meta tag first.

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.imdb.com/title/tt6751668/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=X9NY2QBF33QPCRSFJBKX&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_30'

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url,headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')

# # Masukkan kode disini untu mendapatkan meta tag terlebih dahulu.


# og_image = soup.select_one('meta[property="og:image"]')
# og_title = soup.select_one('meta[property="og:title"]')
# og_description = soup.select_one('meta[property="og:description"]')

# print(og_image)
# print(og_title)
# print(og_description)


# image = og_image['content']
# title = og_title['content']
# desc = og_description['content']

# doc = {
#         'image':image,
#         'title':title,
#         'description':desc,
#         'star':star_receive,
#         'comment':comment_receive
#      }
 
# db.movies.insert_one(doc)

#     return jsonify({'msg':'POST request!'})

# @app.route("/movie", methods=["GET"])
# def movie_get():
#     return jsonify({'msg':'GET request!'})

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)

# # print(image)
# # print(title)
# # print(desc)

from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('mongodb+srv://alifwrdhh111:sparta@cluster0.gaybq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    image = og_image['content']
    title = og_title['content']
    desc = og_description['content']

    doc = {
        'image':image,
        'title':title,
        'description':desc,
        'star':star_receive,
        'comment':comment_receive
    }

    db.movies.insert_one(doc)

    return jsonify({'msg':'POST request!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
