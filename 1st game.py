import arcade
import random

window = arcade.Window(width=1350,height=687,title="Snake game")
window.center_window()

start_color = (255,255,255,95)
class Snake:
    def __init__(self):
        self.body = [[523,124]]
        self.center_x = 675
        self.center_y = 343
        self.width = 30
        self.height = 30
        self.speed_x = 0
        self.speed_y = 300
        self.color = arcade.color.GREEN
        self.angle = 0
        self.speed = 300
        
    def draw(self):
        for body in self.body:
            arcade.draw_rectangle_filled(
            body[0],
            body[1],
            self.width,
            self.height,
            color = self.color,
            tilt_angle = self.angle,
            )
class Food:
    def __init__(self):
        self.app_x = (random.randint(1,44) * 30)+15
        self.app_y = (random.randint(1,22) * 30)+15
    def draw(self):
        apple = arcade.draw_circle_filled(center_x = self.app_x, center_y = self.app_y, radius = 15, color = arcade.color.RED)
        
        
        
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.move_timer = 0
        self.move_interval = 0.15
        self.pop = arcade.load_sound(r"D:\Coodes\pop.mp3")
    def on_draw(self):
        self.clear()
        self.food.draw()
        if self.game_over:
            self.clear()
            arcade.draw_text(
                "GAME OVER",
                start_x=675,
                start_y=343,
                color=arcade.color.RED,
                font_size=50,
                anchor_x="center",
                anchor_y="center")
        else:
            self.snake.draw()
    def on_key_press(self, key, modifiers):
        if self.snake.speed_x == -self.snake.speed or self.snake.speed_x == self.snake.speed:
            if key == arcade.key.W or key == arcade.key.UP:
                self.snake.angle = 90
                self.snake.speed_x = 0
                self.snake.speed_y = self.snake.speed
            elif key == arcade.key.S or key == arcade.key.DOWN:
                self.snake.angle = -90
                self.snake.speed_x = 0
                self.snake.speed_y = -self.snake.speed
        elif self.snake.speed_y == self.snake.speed or self.snake.speed_y == -self.snake.speed:
            if key == arcade.key.A or key == arcade.key.LEFT:
                self.snake.angle = 180
                self.snake.speed_x = -self.snake.speed
                self.snake.speed_y = 0
            elif key == arcade.key.D or key == arcade.key.RIGHT:
                self.snake.angle = 0
                self.snake.speed_x = self.snake.speed
                self.snake.speed_y = 0

    
    def on_update(self, delta_time:float):
        if not self.game_over:
        
            self.move_timer += delta_time
            if self.move_timer < self.move_interval:
                return
            self.move_timer = 0
            
            
            currnt_head = self.snake.body[0]
            step = self.snake.width
            new_head_x = currnt_head[0] + (self.snake.speed_x/self.snake.speed)*step
            new_head_y = currnt_head[1] + (self.snake.speed_y/self.snake.speed)*step
            
            
            if new_head_x >= 1350 - self.snake.width/2 or new_head_x <= self.snake.width/2:
                self.game_over = True
                return
            elif new_head_y >= 687 - self.snake.height/2 or new_head_y <= self.snake.height/2:
                self.game_over = True
                return
                
            new_head = [new_head_x, new_head_y]
            
            if new_head in self.snake.body:
                self.game_over = True
                return
                
                
            self.snake.body.insert(0, new_head)
                
                
            dis = arcade.get_distance(self.food.app_x, self.food.app_y, new_head_x, new_head_y)
            if dis <= 25:
                self.food = Food()
                arcade.play_sound(self.pop)
            else :
                if len(self.snake.body) > 1:
                    self.snake.body.pop()
    
game = GameView()
window.show_view(game)
arcade.run()