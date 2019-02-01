
if __name__ == "__main__":
    from DataBase.db_scrapping import * 
    from ScrappingGithub.scrapping import *
    from API.api import *
    # -------------------
    app = App().app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+base_dir+'/database.db'
    db = SQLAlchemy(app)
    db.init_app(app)
    api = Api(app)
    api.add_resource(GitUser,'/<string:nameacc>')
    app.run(port=3000, debug=True)