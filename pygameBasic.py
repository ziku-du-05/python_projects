from superwires import games, color
import random


class Pizza(games.Sprite):
    image = games.load_image("pizzaSprite.bmp")
    speed = 1
    
    def __init__(self, x, y = 90):
        super(Pizza, self).__init__(image = Pizza.image,
                                        x = x, y = y,
                                        dy = Pizza.speed)

    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)
    
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    
    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(value = "Game Over",
        size = 90,
        color = color.red,
        x = games.screen.width/2,
        y = games.screen.height/2,
        lifetime = 5 * games.screen.fps,
        after_death = games.screen.quit)
        games.screen.add(end_message)

class Pan(games.Sprite):
    image = games.load_image("bowl.png")
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image,
                                    x = games.mouse.x,
                                    bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, 
                                    color = color.black,
                                    top = 5, 
                                    right = games.screen.width - 10)
        games.screen.add(self.score)
    
    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for pizza in self.overlapping_sprites:
             self.score.value += 10
        self.score.right = games.screen.width - 10
        pizza.handle_caught()   

    def check_collide(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()
    


games.init(screen_width = 640, screen_height = 420,fps=20)
wall_image = games.load_image("wall.png", transparent = False)
games.screen.background = wall_image
    
pizza_image = games.load_image("pizzaSprite.bmp")
pizza_x =random.randrange(games.screen.width)
pizza_y = random.randrange(games.screen.height)
the_pizza = Pizza(image = pizza_image,
                        x = pizza_x,
                        y= pizza_y,
                        dx=1,
                        dy=1)
games.screen.add(the_pizza)


boul_image = games.load_image("bowl.png")
the_pan = Pan(image = boul_image,
                    x = 120,
                    y = 340,
                    )
games.screen.add(the_pan)

start_message = games.Message(value = "Game will start",
                                    size = 100,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 20,
                                    )
games.screen.add(start_message)


score = games.Text(value = 1756521,
                        size = 30,
                        color = color.gray,
                        x = 600,
                        y = 30)
games.screen.add(score)

games.screen.event_grab = True
games.mouse.is_visible = False
games.screen.mainloop()  
