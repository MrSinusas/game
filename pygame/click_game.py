blob = Actor('character')
blob.pos = 100, 50

WIDTH = 500
HEIGHT = blob.height + 20

def draw():
    screen.fill((255, 0, 0))
    blob.draw()

def update():
    blob.left = blob.left + 5
    if blob.left > WIDTH:
        blob.right = 0
