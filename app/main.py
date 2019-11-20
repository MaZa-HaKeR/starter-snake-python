import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))


    color= "#000000"
    return start_response(color)


@bottle.post('/move')
def move(x,y,width,height,health):
    data = bottle.request.json  
    
    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))
    if move=='up':directions = ['down', 'left', 'right']
    elif move== 'down':directions =['up', 'left', 'right']
    elif move=='right':directions =['up', 'down', 'left']
    elif move == 'left':directions=['up', 'down', 'right']
    
    if x!=0|y!=0|x!=width-1|y!=height-1 : direction = random.choice(directions)
    if (x=="width"-1):
        if move== 'down':directions =['left', 'right']
        direction = random.choice(directions)
        pass
    elif y=="height"-1:
        move=='right':directions =['up', 'down']
        direction = random.choice(directions)
        pass
    elif x==0&y==0:
        directions =['up','down', 'left', 'right']
        direction =  directions[3]
        pass
    elif x==width-1&y==height-1:
        directions =['up','down', 'left', 'right']
        direction =  directions[0]
        pass
    elif x==0&y==height-1:
        directions =['up','down', 'left', 'right']
        direction =  directions[1]
        pass
    elif x==width-1&y==0:
        directions =['up','down', 'left', 'right']
        direction =  directions[0]
        pass
    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
