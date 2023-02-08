blob = Actor('character')
blob.topright = 0, 10

WIDTH = 500
HEIGHT = blob.height + 20

def draw():
    screen.clear()
    blob.draw()

def update():
    blob.left = blob.left + 2
    if blob.left > WIDTH:
        blob.right = 0
