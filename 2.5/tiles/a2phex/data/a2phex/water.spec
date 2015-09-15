
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
    Hogne Håskjold
    Tim F. Smith <yoohootim@hotmail.com>
    Yautja
    Daniel Speyer
    Eleazar
"

[file]
gfx = "a2phex/water"

[grid_main]

x_top_left = 31
y_top_left = 31
dx = 64
dy = 17
pixel_border = 1

tiles = { "row", "column","tag"
 
; ==========================
; shallow ocean cell sprites
; ==========================

; match with land
  0, 0,  "t.l0.coast_cell_u_s_s_s" ;vacant cell
  0, 1,  "t.l0.coast_cell_u_l_s_s"
  0, 2,  "t.l0.coast_cell_u_s_l_s"
  0, 3,  "t.l0.coast_cell_u_l_l_s"
  0, 4,  "t.l0.coast_cell_u_s_s_l"
  0, 5,  "t.l0.coast_cell_u_l_s_l"
  0, 6,  "t.l0.coast_cell_u_s_l_l"
  0, 7,  "t.l0.coast_cell_u_l_l_l"
 
  1, 0,  "t.l0.coast_cell_d_s_s_s" ;vacant cell
  1, 1,  "t.l0.coast_cell_d_l_s_s"
  1, 2,  "t.l0.coast_cell_d_s_l_s"
  1, 3,  "t.l0.coast_cell_d_l_l_s"
  1, 4,  "t.l0.coast_cell_d_s_s_l"
  1, 5,  "t.l0.coast_cell_d_l_s_l"
  1, 6,  "t.l0.coast_cell_d_s_l_l"
  1, 7,  "t.l0.coast_cell_d_l_l_l"

  2, 0,  "t.l0.coast_cell_l_s_s_s" ;vacant cell
  2, 1,  "t.l0.coast_cell_l_l_s_s"
  2, 2,  "t.l0.coast_cell_l_s_l_s"
  2, 3,  "t.l0.coast_cell_l_l_l_s"
  2, 4,  "t.l0.coast_cell_l_s_s_l"
  2, 5,  "t.l0.coast_cell_l_l_s_l"
  2, 6,  "t.l0.coast_cell_l_s_l_l"
  2, 7,  "t.l0.coast_cell_l_l_l_l"

  3, 0,  "t.l0.coast_cell_r_s_s_s"
  3, 1,  "t.l0.coast_cell_r_l_s_s"
  3, 2,  "t.l0.coast_cell_r_s_l_s"
  3, 3,  "t.l0.coast_cell_r_l_l_s"
  3, 4,  "t.l0.coast_cell_r_s_s_l"
  3, 5,  "t.l0.coast_cell_r_l_s_l"
  3, 6,  "t.l0.coast_cell_r_s_l_l"
  3, 7,  "t.l0.coast_cell_r_l_l_l"

; deep ocean sprites macth with us, point to empty sprite here
 12, 0,  "t.l1.coast_cell_u" ;vacant cell
 12, 0,  "t.l1.coast_cell_d" ;vacant cell
 12, 0,  "t.l1.coast_cell_l" ;vacant cell
 12, 0,  "t.l1.coast_cell_r" ;vacant cell

; match with ice
 16, 0,  "t.l2.coast_cell_u_w_w_w" ;vacant cell
 16, 1,  "t.l2.coast_cell_u_i_w_w"
 16, 2,  "t.l2.coast_cell_u_w_i_w"
 16, 3,  "t.l2.coast_cell_u_i_i_w"
 16, 4,  "t.l2.coast_cell_u_w_w_i"
 16, 5,  "t.l2.coast_cell_u_i_w_i"
 16, 6,  "t.l2.coast_cell_u_w_i_i"
 16, 7,  "t.l2.coast_cell_u_i_i_i"
 
 17, 0,  "t.l2.coast_cell_d_w_w_w" ;vacant cell
 17, 1,  "t.l2.coast_cell_d_i_w_w"
 17, 2,  "t.l2.coast_cell_d_w_i_w"
 17, 3,  "t.l2.coast_cell_d_i_i_w"
 17, 4,  "t.l2.coast_cell_d_w_w_i"
 17, 5,  "t.l2.coast_cell_d_i_w_i"
 17, 6,  "t.l2.coast_cell_d_w_i_i"
 17, 7,  "t.l2.coast_cell_d_i_i_i"

 18, 0,  "t.l2.coast_cell_l_w_w_w" ;vacant cell
 18, 1,  "t.l2.coast_cell_l_i_w_w"
 18, 2,  "t.l2.coast_cell_l_w_i_w"
 18, 3,  "t.l2.coast_cell_l_i_i_w"
 18, 4,  "t.l2.coast_cell_l_w_w_i"
 18, 5,  "t.l2.coast_cell_l_i_w_i"
 18, 6,  "t.l2.coast_cell_l_w_i_i"
 18, 7,  "t.l2.coast_cell_l_i_i_i"

 19, 0,  "t.l2.coast_cell_r_w_w_w"
 19, 1,  "t.l2.coast_cell_r_i_w_w"
 19, 2,  "t.l2.coast_cell_r_w_i_w"
 19, 3,  "t.l2.coast_cell_r_i_i_w"
 19, 4,  "t.l2.coast_cell_r_w_w_i"
 19, 5,  "t.l2.coast_cell_r_i_w_i"
 19, 6,  "t.l2.coast_cell_r_w_i_i"
 19, 7,  "t.l2.coast_cell_r_i_i_i" 

; ========================
; deep ocean cell sprites:
; ========================

; match with land
  4, 0,  "t.l0.floor_cell_u_d_d_d" ;vacant cell
  4, 1,  "t.l0.floor_cell_u_l_d_d"
  4, 2,  "t.l0.floor_cell_u_d_l_d"
  4, 3,  "t.l0.floor_cell_u_l_l_d"
  4, 4,  "t.l0.floor_cell_u_d_d_l"
  4, 5,  "t.l0.floor_cell_u_l_d_l"
  4, 6,  "t.l0.floor_cell_u_d_l_l"
  4, 7,  "t.l0.floor_cell_u_l_l_l"
 
  5, 0,  "t.l0.floor_cell_d_d_d_d" ;vacant cell
  5, 1,  "t.l0.floor_cell_d_l_d_d"
  5, 2,  "t.l0.floor_cell_d_d_l_d"
  5, 3,  "t.l0.floor_cell_d_l_l_d"
  5, 4,  "t.l0.floor_cell_d_d_d_l"
  5, 5,  "t.l0.floor_cell_d_l_d_l"
  5, 6,  "t.l0.floor_cell_d_d_l_l"
  5, 7,  "t.l0.floor_cell_d_l_l_l"

  6, 0,  "t.l0.floor_cell_l_d_d_d" ;vacant cell
  6, 1,  "t.l0.floor_cell_l_l_d_d"
  6, 2,  "t.l0.floor_cell_l_d_l_d"
  6, 3,  "t.l0.floor_cell_l_l_l_d"
  6, 4,  "t.l0.floor_cell_l_d_d_l"
  6, 5,  "t.l0.floor_cell_l_l_d_l"
  6, 6,  "t.l0.floor_cell_l_d_l_l"
  6, 7,  "t.l0.floor_cell_l_l_l_l"

  7, 0,  "t.l0.floor_cell_r_d_d_d"
  7, 1,  "t.l0.floor_cell_r_l_d_d"
  7, 2,  "t.l0.floor_cell_r_d_l_d"
  7, 3,  "t.l0.floor_cell_r_l_l_d"
  7, 4,  "t.l0.floor_cell_r_d_d_l"
  7, 5,  "t.l0.floor_cell_r_l_d_l"
  7, 6,  "t.l0.floor_cell_r_d_l_l"
  7, 7,  "t.l0.floor_cell_r_l_l_l"

; match with shallow ocean
 12, 0,  "t.l1.floor_cell_u_d_d_d" ;vacant cell
 12, 1,  "t.l1.floor_cell_u_s_d_d"
 12, 2,  "t.l1.floor_cell_u_d_s_d"
 12, 3,  "t.l1.floor_cell_u_s_s_d"
 12, 4,  "t.l1.floor_cell_u_d_d_s"
 12, 5,  "t.l1.floor_cell_u_s_d_s"
 12, 6,  "t.l1.floor_cell_u_d_s_s"
 12, 7,  "t.l1.floor_cell_u_s_s_s"
 
 13, 0,  "t.l1.floor_cell_d_d_d_d" ;vacant cell
 13, 1,  "t.l1.floor_cell_d_s_d_d"
 13, 2,  "t.l1.floor_cell_d_d_s_d"
 13, 3,  "t.l1.floor_cell_d_s_s_d"
 13, 4,  "t.l1.floor_cell_d_d_d_s"
 13, 5,  "t.l1.floor_cell_d_s_d_s"
 13, 6,  "t.l1.floor_cell_d_d_s_s"
 13, 7,  "t.l1.floor_cell_d_s_s_s"

 14, 0,  "t.l1.floor_cell_l_d_d_d" ;vacant cell
 14, 1,  "t.l1.floor_cell_l_s_d_d"
 14, 2,  "t.l1.floor_cell_l_d_s_d"
 14, 3,  "t.l1.floor_cell_l_s_s_d"
 14, 4,  "t.l1.floor_cell_l_d_d_s"
 14, 5,  "t.l1.floor_cell_l_s_d_s"
 14, 6,  "t.l1.floor_cell_l_d_s_s"
 14, 7,  "t.l1.floor_cell_l_s_s_s"

 15, 0,  "t.l1.floor_cell_r_d_d_d"
 15, 1,  "t.l1.floor_cell_r_s_d_d"
 15, 2,  "t.l1.floor_cell_r_d_s_d"
 15, 3,  "t.l1.floor_cell_r_s_s_d"
 15, 4,  "t.l1.floor_cell_r_d_d_s"
 15, 5,  "t.l1.floor_cell_r_s_d_s"
 15, 6,  "t.l1.floor_cell_r_d_s_s"
 15, 7,  "t.l1.floor_cell_r_s_s_s"

; match with ice
 16, 0,  "t.l2.floor_cell_u_w_w_w" ;vacant cell
 16, 1,  "t.l2.floor_cell_u_i_w_w"
 16, 2,  "t.l2.floor_cell_u_w_i_w"
 16, 3,  "t.l2.floor_cell_u_i_i_w"
 16, 4,  "t.l2.floor_cell_u_w_w_i"
 16, 5,  "t.l2.floor_cell_u_i_w_i"
 16, 6,  "t.l2.floor_cell_u_w_i_i"
 16, 7,  "t.l2.floor_cell_u_i_i_i"
 
 17, 0,  "t.l2.floor_cell_d_w_w_w" ;vacant cell
 17, 1,  "t.l2.floor_cell_d_i_w_w"
 17, 2,  "t.l2.floor_cell_d_w_i_w"
 17, 3,  "t.l2.floor_cell_d_i_i_w"
 17, 4,  "t.l2.floor_cell_d_w_w_i"
 17, 5,  "t.l2.floor_cell_d_i_w_i"
 17, 6,  "t.l2.floor_cell_d_w_i_i"
 17, 7,  "t.l2.floor_cell_d_i_i_i"

 18, 0,  "t.l2.floor_cell_l_w_w_w" ;vacant cell
 18, 1,  "t.l2.floor_cell_l_i_w_w"
 18, 2,  "t.l2.floor_cell_l_w_i_w"
 18, 3,  "t.l2.floor_cell_l_i_i_w"
 18, 4,  "t.l2.floor_cell_l_w_w_i"
 18, 5,  "t.l2.floor_cell_l_i_w_i"
 18, 6,  "t.l2.floor_cell_l_w_i_i"
 18, 7,  "t.l2.floor_cell_l_i_i_i"

 19, 0,  "t.l2.floor_cell_r_w_w_w"
 19, 1,  "t.l2.floor_cell_r_i_w_w"
 19, 2,  "t.l2.floor_cell_r_w_i_w"
 19, 3,  "t.l2.floor_cell_r_i_i_w"
 19, 4,  "t.l2.floor_cell_r_w_w_i"
 19, 5,  "t.l2.floor_cell_r_i_w_i"
 19, 6,  "t.l2.floor_cell_r_w_i_i"
 19, 7,  "t.l2.floor_cell_r_i_i_i" 

; ==========
; lake tiles
; ==========

; match with land
  8, 0,  "t.l0.lake_cell_u_s_s_s" ;vacant cell
  8, 1,  "t.l0.lake_cell_u_l_s_s"
  8, 2,  "t.l0.lake_cell_u_s_l_s"
  8, 3,  "t.l0.lake_cell_u_l_l_s"
  8, 4,  "t.l0.lake_cell_u_s_s_l"
  8, 5,  "t.l0.lake_cell_u_l_s_l"
  8, 6,  "t.l0.lake_cell_u_s_l_l"
  8, 7,  "t.l0.lake_cell_u_l_l_l"
 
  9, 0,  "t.l0.lake_cell_d_s_s_s" ;vacant cell
  9, 1,  "t.l0.lake_cell_d_l_s_s"
  9, 2,  "t.l0.lake_cell_d_s_l_s"
  9, 3,  "t.l0.lake_cell_d_l_l_s"
  9, 4,  "t.l0.lake_cell_d_s_s_l"
  9, 5,  "t.l0.lake_cell_d_l_s_l"
  9, 6,  "t.l0.lake_cell_d_s_l_l"
  9, 7,  "t.l0.lake_cell_d_l_l_l"

 10, 0,  "t.l0.lake_cell_l_s_s_s" ;vacant cell
 10, 1,  "t.l0.lake_cell_l_l_s_s"
 10, 2,  "t.l0.lake_cell_l_s_l_s"
 10, 3,  "t.l0.lake_cell_l_l_l_s"
 10, 4,  "t.l0.lake_cell_l_s_s_l"
 10, 5,  "t.l0.lake_cell_l_l_s_l"
 10, 6,  "t.l0.lake_cell_l_s_l_l"
 10, 7,  "t.l0.lake_cell_l_l_l_l"

 11, 0,  "t.l0.lake_cell_r_s_s_s"
 11, 1,  "t.l0.lake_cell_r_l_s_s"
 11, 2,  "t.l0.lake_cell_r_s_l_s"
 11, 3,  "t.l0.lake_cell_r_l_l_s"
 11, 4,  "t.l0.lake_cell_r_s_s_l"
 11, 5,  "t.l0.lake_cell_r_l_s_l"
 11, 6,  "t.l0.lake_cell_r_s_l_l"
 11, 7,  "t.l0.lake_cell_r_l_l_l"
 
}
