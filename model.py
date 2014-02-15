import web, datetime


def get_db():
  return web.database(dbn='mysql', db='blog', user='root')

def get_posts():
    return get_db().select('entries', order='id DESC')

def get_post(id):
    try:
        return get_db().select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    get_db().insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    get_db().delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    get_db().update('entries', where="id=$id", vars=locals(),
        title=title, content=text)