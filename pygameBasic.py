from superwires import games, color
import random


class Pizza(games.Sprite):
    # image = games.load_image("pizzaSprite.bmp")
    speed = 1
    
    def __init__(self, x, y = 90):
        self.image = games.load_image("pizzaSprite.bmp")
        super(Pizza, self).__init__(image = self.image,
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
    
    def __init__(self):
        self.image = games.load_image("bowl.png")
        super(Pan, self).__init__(image = self.image,
                                    x = games.mouse.x,
                                    bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, 
                                    color = color.purple,
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

class Chef(games.Sprite):
    
    
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        self.image = games.load_image("chef.png")  
        super(Chef, self).__init__(image = self.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
            self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
        
        self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1



def main():
    games.init(screen_width = 640, screen_height = 420,fps=20)
    wall_image = games.load_image("wall.png", transparent = False)
    games.screen.background = wall_image
        
    start_message = games.Message(value = "Game will start",
                                        size = 100,
                                        color = color.red,
                                        x = games.screen.width/2,
                                        y = games.screen.height/2,
                                        lifetime = 20,
                                        )
    games.screen.add(start_message)


    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan()
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
     


main() 
