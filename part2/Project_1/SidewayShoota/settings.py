class Settings:
    """a Class to store all settings for SideShoota"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.7
        self.bullet_width = 15
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ali settings
        self.ali_speed = 0.4
        self.alis_left_speed = 0.075
        self.alis_horizontal_speed = -1

    #fleet_direction of 1 represent down, -1 represent up.
        self.alis_direction = 1