class Settings:
    """Class to store all the settings fpr the rockets"""

    def __init__(self):
        """Initialize the agme's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Rocket settings
        self.rocket_x_speed = 1.5
        self.rocket_y_speed = 1.5

