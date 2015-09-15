;
; The names for city tiles are not free and must follow the following rules.
; The names consists of style name, _ , size. The style name is as specified
; in cities.ruleset file. The size indicates which size city must
; have to be drawn with a tile. E.g. european_4 means that the tile is to be
; used for cities of size 4+ in european style. Obviously the first tile
; must be style_name_0. The sizes must be in ascending order.
; There must also be a style_name_wall tile used to draw the wall and
; an occupied tile to indicate a miltary units in a city.
; The maximum size supported now is 31, but there can only be MAX_CITY_TILES
; normal tiles. The constant is defined in common/city.h and set to 8 now.
;

[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
    Celtic style by Erwan, adapted to 96x48 by CapTVK
    Roman style by CapTVK
    City walls by Hogne Håskjold
"

[file]
gfx = "a2phex/westerncities"

[grid_main]

x_top_left = 31
y_top_left = 31
dx = 128
dy = 68
pixel_border = 1

tiles = { "row", "column", "tag"

; default tiles

 6,  4, "cd.city"
 7,  4, "cd.city_wall"
 6,  5, "cd.occupied"

; used by all city styles

 6,  0, "city.disorder"
 6,  1, "base.airbase_mg"
 7,  1, "tx.airbase_full"
 7,  2, "base.fortress_fg"
 6,  2, "base.fortress_bg"
 
 6,  3, "base.buoy_mg"
 7,  3, "base.ruins_mg"

;
; occupied
;

 0,  5, "city.classical_occupied_0"
 2,  5, "city.celtic_occupied_0"
 4,  5, "city.european_occupied_0"


;
; city tiles
;

 0,  0, "city.classical_city_0"
 0,  1, "city.classical_city_1"
 0,  2, "city.classical_city_2"
 0,  3, "city.classical_city_3"
 0,  4, "city.classical_city_4" 
 1,  0, "city.classical_wall_0"
 1,  1, "city.classical_wall_1"
 1,  2, "city.classical_wall_2"
 1,  3, "city.classical_wall_3"
 1,  4, "city.classical_wall_4" 
   

 2,  0, "city.celtic_city_0"
 2,  1, "city.celtic_city_1"
 2,  2, "city.celtic_city_2"
 2,  3, "city.celtic_city_3"
 2,  4, "city.celtic_city_4" 
 3,  0, "city.celtic_wall_0"
 3,  1, "city.celtic_wall_1"
 3,  2, "city.celtic_wall_2"
 3,  3, "city.celtic_wall_3"
 3,  4, "city.celtic_wall_4" 


 4,  0, "city.european_city_0"
 4,  1, "city.european_city_1"
 4,  2, "city.european_city_2"
 4,  3, "city.european_city_3"
 4,  4, "city.european_city_4"
 5,  0, "city.european_wall_0"
 5,  1, "city.european_wall_1"
 5,  2, "city.european_wall_2"
 5,  3, "city.european_wall_3"
 5,  4, "city.european_wall_4"

}
