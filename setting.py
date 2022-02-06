# Will change the map and implement more items

level_map = [
    '                            ',
    '                            ',
    '                            ',
    '       XXXX           XX    ',
    '   P                        ',
    'XXXXX         XX         XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  ']

# Size of the UI - can be modified
tile_size = 64
screen_width = 1280
screen_height = tile_size * len(level_map)

# colors
# ! Will implement chracter
bg_color = 'black'
player_color = '#FFFFFF'
tile_color = "#94D7F2"

# camera
camera_padding = {
    "left": 150,
    "right": 250,
    "top": 150,
    "bottom": 200,
}
