
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
    Hogne Håskjold
    Daniel Speyer
    Yautja
    CapTVK
	HanduMan
"

[file]
gfx = "a2phex/terrain1"

[grid_main]

x_top_left = 31
y_top_left = 31
dx = 128
dy = 34
pixel_border = 1

tiles = { "row", "column","tag"

; terrain graphics shaped for (iso) hex by HanduMan
 0,  0, "t.l0.desert1"
 1,  0, "t.l0.plains1"
 2,  0, "t.l0.grassland1"
 3,  0, "t.l0.forest1"
 4,  0, "t.l0.hills1"
 5,  0, "t.l0.mountains1"
 6,  0, "t.l0.tundra1"
 7,  0, "t.l0.arctic1"
;7,  0, "t.l1.arctic1" not redrawn
;7,  0, "t.l2.arctic1" not redrawn
 8,  0, "t.l0.swamp1", "t.l0.arctic_forest1"
 9,  0, "t.l0.jungle1"
10,  0, "t.l0.ice1"

; Terrain special resources:

 0,  1, "ts.oasis"
 0,  2, "ts.oil"

 1,  1, "ts.buffalo"
 1,  2, "ts.wheat"

 2,  1, "ts.grassland_resources", "ts.river_resources"
 2,  2, "ts.horses"

 3,  1, "ts.pheasant"
 3,  2, "ts.silk"
 3,  3, "ts.forest_game"

 4,  1, "ts.coal"
 4,  2, "ts.wine"

 5,  1, "ts.gold"
 5,  2, "ts.iron"

 6,  1, "ts.tundra_game"
 6,  2, "ts.furs"

 7,  1, "ts.arctic_ivory"
 7,  2, "ts.arctic_oil"
 7,  3, "ts.seals"

 8,  1, "ts.peat"
 8,  2, "ts.spice"

 9,  1, "ts.gems"
 9,  2, "ts.fruit"

 10, 1, "ts.fish"	; Fresh fish by HanduMan
 10, 2, "ts.whales" ; 
; 11, 2, "ts.whales" ; New South Whales by HanduMan

;add-ons
; testing---> 4,  4, "tx.oil_mine"
 0,  3, "tx.oil_mine"
 1,  5, "tx.irrigation"	; re-shaped for (iso) hex by HanduMan
 2,  3, "tx.farmland"	; re-shaped for (iso) hex by HanduMan
 4,  3, "tx.mine"
 
 0,  4, "tx.village"
 ;1,  4, "tx.pollution"	; Original Amplio 2 (isotrident) pollution
 2,  4, "tx.pollution"	; Pollution! by HanduMan
 ;3,  4, "tx.fallout"	; Original Amplio 2 (isotrident) fallout
 4,  4, "tx.fallout"	; Fallout! by HanduMan
 

 ;roads
 12, 0, "road.road_isolated"
 12, 1, "road.road_n"
 12, 2, "road.road_ne"
 13, 0, "road.road_e"
 13, 1, "road.road_se"
 13, 2, "road.road_s"
 14, 0, "road.road_sw"
 14, 1, "road.road_w"
 14, 2, "road.road_nw"

;rails
 12, 3, "road.rail_isolated"
 12, 4, "road.rail_n"
 12, 5, "road.rail_ne"
 13, 3, "road.rail_e"
 13, 4, "road.rail_se"
 13, 5, "road.rail_s"
 14, 3, "road.rail_sw"
 14, 4, "road.rail_w"
 14, 5, "road.rail_nw"

;maglev (same as rail for now)
 12, 3, "road.maglev_isolated"
 12, 4, "road.maglev_n"
 12, 5, "road.maglev_ne"
 13, 3, "road.maglev_e"
 13, 4, "road.maglev_se"
 13, 5, "road.maglev_s"
 14, 3, "road.maglev_sw"
 14, 4, "road.maglev_w"
 14, 5, "road.maglev_nw"


 15,  0, "t.dither_tile"
 15,  2, "mask.tile"
 15,  2, "t.unknown1"
 15,  1, "t.blend.arctic" ;ice over neighbors
 15,  3, "t.blend.lake"
 15,  3, "t.blend.coast"
; 15,  3, "t.deep1"
; 15,  4, "user.attention" ; in grid.spec
}
