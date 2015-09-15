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
    Asian style by CapTVK
    Polynesian style by CapTVK
    City walls by Hogne Håskjold
"

[file]
gfx = "a2phex/easterncities"

[grid_main]

x_top_left = 31
y_top_left = 31
dx = 128
dy = 68
pixel_border = 1

tiles = { "row", "column", "tag"

; used by all city styles

 0,  5, "city.asian_occupied_0"
 2,  5, "city.tropical_occupied_0"
 4,  5, "city.babylonian_occupied_0"


;
; city tiles
;

 0,  0, "city.asian_city_0"
 0,  1, "city.asian_city_1"
 0,  2, "city.asian_city_2"
 0,  3, "city.asian_city_3"
 0,  4, "city.asian_city_4" 
 1,  0, "city.asian_wall_0"
 1,  1, "city.asian_wall_1"
 1,  2, "city.asian_wall_2"
 1,  3, "city.asian_wall_3"
 1,  4, "city.asian_wall_4" 
   

 2,  0, "city.tropical_city_0"
 2,  1, "city.tropical_city_1"
 2,  2, "city.tropical_city_2"
 2,  3, "city.tropical_city_3"
 2,  4, "city.tropical_city_4" 
 3,  0, "city.tropical_wall_0"
 3,  1, "city.tropical_wall_1"
 3,  2, "city.tropical_wall_2"
 3,  3, "city.tropical_wall_3"
 3,  4, "city.tropical_wall_4" 


 4,  0, "city.babylonian_city_0"
 4,  1, "city.babylonian_city_1"
 4,  2, "city.babylonian_city_2"
 4,  3, "city.babylonian_city_3"
 4,  4, "city.babylonian_city_4"
 5,  0, "city.babylonian_wall_0"
 5,  1, "city.babylonian_wall_1"
 5,  2, "city.babylonian_wall_2"
 5,  3, "city.babylonian_wall_3"
 5,  4, "city.babylonian_wall_4"

}
