# Pylou-s-macropad
A custom macropad for the awesome project hackpad! Using a screen 4 keys a knob and a bunch of LEDs, i'll try to develop a custom firmware with KMK to configure a bunch of things (that doesn't mean anything yet) from your PC!

## CAD
<img src=assets/cad.png width="300"/>
My beautiful Case for this keyboard :). top and bot part fits together with simple M3 screws and heatset inserts and all 4 corners and one screw for the pcb. (I didn't add extra photos to show how it'll fit because its='s pretty self explanatory)

There's also diffuser that'll be simple 1-2mm plane of white PLA, they'll be glued to the top part!

Made with SOLIDWORKS (superior to Fusion360 :)) and it's the first time im designing piece with it (in the pas t iwas using blender ;-;), I hope it works!

## PCB
I used KiCad (for the first time) and i tried to make a compact and clean pcb with small reference and private jokes with my friends!

<img src=assets/pcbsch.png width="300"/>

<img src=assets/pcb.png width="300"/>

## Firmware
Made in KMK by reading docs, tutorials from [this guy](https://www.youtube.com/watch?v=PKTRkv8d0NU&list=PLtl-yze0Zzkm5n2ajJRUL48EyCyUgsXf6) (he's great) and a bit of gemini.

It's pretty simple for the moment, but i plan on addings multiples features to configure what keys does what (from your pc), change whats on the screen, show the time, rgb modes etc when i'll build the pad. I'll update the code when everything will be done! 

## BOM
Here's the list of part for my project!

 - 1x Seeed XIAO RP2040
 - 4x Through-hole 1N4148 Diodes
 - 4x MX-Style switches
 - 1x EC11 Rotary encoders
 - 1x 0.91 inch OLED displays
 - 4x Blank DSA keycaps (White)
 - 10x SK6812 MINI-E LEDs
 - 5x M3x16mm screws
 - 5x M3x5mx4mm heatset inserts
 - 1x 3D printed case: top pink and the rest white
