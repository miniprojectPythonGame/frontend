from frontend.src.globals.const_values import *
from frontend.src.components.ColorSchemes import ColorSchemes

from .Button import Button

# WINDOW PARAMETERS
size_factor = SIZE_FACTOR
window_width = SCREEN_WIDTH * size_factor
window_height = SCREEN_HEIGHT * size_factor
margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12 * 0.5)

# NAVBAR MEASURES
navbar_width = 80
navbar_height = window_height
navbar_padding_vert = 20
navbar_padding_hori = 15
buttons_size = navbar_width - 2 * navbar_padding_hori

navbar = {
    "colors": ColorSchemes(),
    "x": 0,
    "y": 0,
    "width": navbar_width,
    "height": navbar_height,
}

# BUTTON: Character Profile
bt_profile = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": navbar_padding_vert,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/user_white.png',
}

# BUTTON: Settings
bt_settings = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": 2 * navbar_padding_vert + buttons_size,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/settings_white.png',
}

# BUTTON: World map
bt_world_map = {
    "color": ColorSchemes(),
    "x": navbar_padding_hori,
    "y": 3 * navbar_padding_vert + 2 * buttons_size,
    "width": buttons_size,
    "height": buttons_size,
    "path": '../images/icons/map_white.png',
}


class Navbar():
    def __init__(self, screen):
        self.colorSchemes = ColorSchemes()
        self.color = self.colorSchemes.inactive
        self.x = navbar['x']
        self.y = navbar['y']
        self.width = navbar['width']
        self.height = navbar['height']
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bt_profile = Button(bt_profile['color'], bt_profile['x'], bt_profile['y'],
                                 bt_profile['width'], bt_profile['height'], self.screen,
                                 path=bt_profile['path'])
        self.bt_settings = Button(bt_settings['color'], bt_settings['x'], bt_settings['y'],
                                  bt_settings['width'], bt_settings['height'], self.screen,
                                  path=bt_settings['path'])
        self.bt_world_map = Button(bt_world_map['color'], bt_world_map['x'], bt_world_map['y'],
                                   bt_world_map['width'], bt_world_map['height'], self.screen,
                                   path=bt_world_map['path'])

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.bt_profile.draw()
        self.bt_settings.draw()
        self.bt_world_map.draw()
