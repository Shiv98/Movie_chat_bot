from flask import Flask
app = Flask(__name__) 
def get_detail(name):
    import json
    from imdb import IMDb
    ia = IMDb()
    movies = ia.search_movie(name)
    movid=movies[0].movieID
    movie = ia.get_movie(movid)
    return movie
#movie.infoset2keys

@app.route('/<name>') 
def normal_des(name):
    import json
    movie= get_detail(name)
    data=json.dumps({"genre": movie['genres'],"year":movie['year']})
    return data

@app.route('/language/<name>')     
def get_lang(name):
    import json
    movie= get_detail(name)
    l=json.dumps({"language":movie['languages']})
    return l

@app.route('/director/<name>') 
def get_director(name):
    import json
    movie= get_detail(name)
    d=json.dumps({"director":movie['director']})
    return d

@app.route('/rank/<name>') 
def get_rank(name):
    import json
    movie= get_detail(name)
    r=json.dumps({"rank":movie['top 250 rank']})
    return r

if __name__ == '__main__': 
  
    app.run() 
