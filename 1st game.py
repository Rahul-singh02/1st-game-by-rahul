import arcade
import random


window = arcade.Window(width=1350,height=687,title="Snake game")
window.center_window()

start_color = (255,255,255,95)
class Snake:
    def __init__(self):
    
        self.center_x = 675
        self.center_y = 343
        self.width = 30
        self.height = 30
        self.speed_x = 0
        self.speed_y = 0
        self.color = arcade.color.GREEN
        self.angle = 0
        self.speed = 300
        
    def draw(self):
    
        square = arcade.draw_rectangle_filled(
        self.center_x,
        self.center_y, 
        self.width, 
        self.height,
        color = self.color,
        tilt_angle = self.angle,
        )
class Food:
    def __init__(self):
        self.app_x = random.random() * 1350
        self.app_y = random.random() * 687
    def draw(self):
        apple = arcade.draw_circle_filled(center_x = self.app_x, center_y = self.app_y, radius = 15, color = arcade.color.RED)
        
        
        
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
    
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
        if key == arcade.key.LEFT:
            self.snake.angle = 90
            self.snake.speed_x = -self.snake.speed
            self.snake.speed_y = 0
            
            
        elif key == arcade.key.RIGHT:
            self.snake.angle = -90
            self.snake.speed_x = self.snake.speed
            self.snake.speed_y = 0
            
        elif key == arcade.key.UP:
            self.snake.angle = 0
            self.snake.speed_x = 0
            self.snake.speed_y = self.snake.speed

        elif key == arcade.key.DOWN:
            self.snake.angle = 180
            self.snake.speed_x = 0
            self.snake.speed_y = -self.snake.speed

    
    def on_update(self, delta_time:float):
        if not self.game_over:
            self.snake.center_x += self.snake.speed_x*delta_time
            self.snake.center_y += self.snake.speed_y*delta_time
        
            if self.snake.center_x >= 1350 - self.snake.width/2:
                self.game_over = True
        
            elif self.snake.center_x <= self.snake.width/2:
                self.game_over = True
        
            elif self.snake.center_y >= 687 - self.snake.height/2:
                self.game_over = True
        
            elif self.snake.center_y <= self.snake.height/2:
                self.game_over = True
            
            dis = arcade.get_distance(self.food.app_x, self.food.app_y, self.snake.center_x, self.snake.center_y)
            if dis <= 25:
                self.food = Food()
    
game = GameView()
window.show_view(game)
arcade.run()