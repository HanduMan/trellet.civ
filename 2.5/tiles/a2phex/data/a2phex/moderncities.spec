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
    Airfield, city walls and misc stuff Hogne Håskjold <hogne@freeciv.org>
    Modern, Post Modern and Electric Age by Smiley, www.firstcultural.com
    City walls by Hogne Håskjold
"

[file]
gfx = "a2phex/moderncities"

[grid_main]

x_top_left = 31
y_top_left = 31
dx = 128
dy = 68
pixel_border = 1

tiles = { "row", "column", "tag"

;
; occupied
;

 0,  5, "city.industrial_occupied_0"
 2,  5, "city.electricage_occupied_0"
 4,  5, "city.modern_occupied_0"
 6,  5, "city.postmodern_occupied_0"

;
; city tiles
;

 0,  0, "city.industrial_city_0"
 0,  1, "city.industrial_city_1"
 0,  2, "city.industrial_city_2"
 0,  3, "city.industrial_city_3"
 0,  4, "city.industrial_city_4" 
 1,  0, "city.industrial_wall_0"
 1,  1, "city.industrial_wall_1"
 1,  2, "city.industrial_wall_2"
 1,  3, "city.industrial_wall_3"
 1,  4, "city.industrial_wall_4" 


 2,  0, "city.electricage_city_0"
 2,  1, "city.electricage_city_1"
 2,  2, "city.electricage_city_2"
 2,  3, "city.electricage_city_3"
 2,  4, "city.electricage_city_4" 
 3,  0, "city.electricage_wall_0"
 3,  1, "city.electricage_wall_1"
 3,  2, "city.electricage_wall_2"
 3,  3, "city.electricage_wall_3"
 3,  4, "city.electricage_wall_4" 


 4,  0, "city.modern_city_0"
 4,  1, "city.modern_city_1"
 4,  2, "city.modern_city_2"
 4,  3, "city.modern_city_3"
 4,  4, "city.modern_city_4"
 5,  0, "city.modern_wall_0"
 5,  1, "city.modern_wall_1"
 5,  2, "city.modern_wall_2"
 5,  3, "city.modern_wall_3"
 5,  4, "city.modern_wall_4"


 6,  0, "city.postmodern_city_0"
 6,  1, "city.postmodern_city_1"
 6,  2, "city.postmodern_city_2"
 6,  3, "city.postmodern_city_3"
 6,  4, "city.postmodern_city_4" 
 7,  0, "city.postmodern_wall_0"
 7,  1, "city.postmodern_wall_1"
 7,  2, "city.postmodern_wall_2"
 7,  3, "city.postmodern_wall_3"
 7,  4, "city.postmodern_wall_4" 

}
