import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.combos import Combos, Chord
from kmk.extensions.display import Display, ImageEntry, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.rgb import RGB
from kmk.extensions.media_keys import MediaKeys

# Setup initialisation
keyboard = KMKKeyboard()

#2x2 Matrix, useless here but i wated to give it a shot!
keyboard.col_pins = (board.D8, board.D7)
keyboard.row_pins = (board.D3, board.D2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# strip of rgb for pure decoration
rgb_strip = RGB(
    pixel_pin=board.D6,
    num_pixels=6,
    animation_mode="rainbow"
)
keyboard.extensions.append(rgb_strip)

# leds on the keys
rgb_keys = RGB(
    pixel_pin=board.D10,
    num_pixels=4,
    animation_mode="reactive"
)
keyboard.extensions.append(rgb_keys)

# --- LAYERS & STATE for configurations ---
layers = Layers()
keyboard.modules.append(layers)

class State:
    current_profile = 0
    total_profiles = 5

state = State()

def change_profile(direction):
    if direction == "NEXT":
        state.current_profile = (state.current_profile + 1) % state.total_profiles
    elif direction == "PREV":
        state.current_profile = (state.current_profile - 1) % state.total_profiles

    keyboard.tap_key(KC.DF(state.current_profile))

KC_PROF_NEXT = make_key(on_press=lambda *args: change_profile("NEXT"))
KC_PROF_PREV = make_key(on_press=lambda *args: change_profile("PREV"))

# --- SCREEN ---
i2c_bus = busio.I2C(board.D5, board.D4)
driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(display=driver, width=128, height=32, brightness=1)
keyboard.extensions.append(display)

def draw_top_bar(display):
    for i in range(5):
        x = 10 + (i * 22)
        filled = 1 if i == state.current_profile else 0
        display.rect(x, 0, 15, 6, 1, filled=filled)

display.entries = [
    ImageEntry(image=draw_top_bar, x=0, y=0),
    TextEntry(text="Pylou", x=64, y=20, x_anchor='M', y_anchor='M'),
]

# --- KEYMAP ---
my_keymap = [[KC.A, KC.B, KC.C, KC.D], [KC.TRNS] * 4, [KC.TRNS] * 4, [KC.TRNS] * 4, [KC.TRNS] * 4]

my_keymap.append([
    KC.RGB_MOD,
    KC.RGB_ANI,
    KC.RGB_AND,
    KC.RGB_TOG
])
keyboard.keymap = my_keymap

# --- MEDIA KEYS ---
keyboard.extensions.append(MediaKeys())

# --- ENCODER ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D1, board.D0, board.D9),)

encoder_map = [((KC.VOLD, KC.VOLU, KC.MPLY),)] * 5
encoder_map.append(((KC_PROF_PREV, KC_PROF_NEXT, KC.MPLY),))
encoder_handler.map = encoder_map

# --- COMBOS to switch configurations ---
combos = Combos()
keyboard.modules.append(combos)
LAYER_CONTROL = 5
combos.combos = [Chord((my_keymap[0][0], my_keymap[0][1]), KC.MO(LAYER_CONTROL))]

if __name__ == '__main__':
    keyboard.go()