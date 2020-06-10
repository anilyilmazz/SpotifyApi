import api_data
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getgenres')
def getgenres():
    genrelist = api_data.getgenres()
    return jsonify(genrelist)

@app.route('/tracks/<genre>')
def tracks(genre):
    genrelist = api_data.getgenres()

    if genre in genrelist:
        accestoken = api_data.getaccesstoken()
        randomartist = api_data.getrandomartist(genre)
        artistid = api_data.getartistid(randomartist,accestoken)
        toptracklist = api_data.getartisttoptrack(artistid,accestoken)
        return jsonify({'artistname': randomartist, 'tracklist': toptracklist, 'result': True})
    else:
        return jsonify({'result': False, 'message' : 'Genre is not avaible.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=False)