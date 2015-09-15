
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
	HanduMan <HanduMan@savageclub.org>
	"

[file]
gfx = "a2phex/rivers"

[grid_main]

x_top_left = 31
y_top_left = 31
dx = 128
dy = 34
pixel_border = 1

tiles = { "row", "column","tag"
; river (as special type), and whether north, south, east, west, SE, NW also has river:
; (for terrain overlays, replace "tx.s_" with "t.")

 0,  0, "road.river_s_n1e0se0s0w0nw0"
 0,  1, "road.river_s_n0e1se0s0w0nw0"
 0,  2, "road.river_s_n0e0se0s1w0nw0"
 0,  3, "road.river_s_n0e0se0s0w1nw0"
 1,  0, "road.river_s_n1e1se0s0w0nw0"
 1,  1, "road.river_s_n0e1se0s1w0nw0"
 1,  2, "road.river_s_n0e0se0s1w1nw0"
 1,  3, "road.river_s_n1e0se0s0w1nw0"
 2,  0, "road.river_s_n1e1se0s1w0nw0"
 2,  1, "road.river_s_n0e1se0s1w1nw0"
 2,  2, "road.river_s_n1e0se0s1w1nw0"
 2,  3, "road.river_s_n1e1se0s0w1nw0"
 3,  0, "road.river_s_n0e0se0s0w0nw0"
 3,  1, "road.river_s_n1e0se0s1w0nw0"
 3,  2, "road.river_s_n0e1se0s0w1nw0"
 3,  3, "road.river_s_n1e1se0s1w1nw0"

 4,  0, "road.river_s_n1e0se0s0w0nw1"
 4,  1, "road.river_s_n0e1se0s0w0nw1"
 4,  2, "road.river_s_n0e0se0s1w0nw1"
 4,  3, "road.river_s_n0e0se0s0w1nw1"
 5,  0, "road.river_s_n1e1se0s0w0nw1"
 5,  1, "road.river_s_n0e1se0s1w0nw1"
 5,  2, "road.river_s_n0e0se0s1w1nw1"
 5,  3, "road.river_s_n1e0se0s0w1nw1"
 6,  0, "road.river_s_n1e1se0s1w0nw1"
 6,  1, "road.river_s_n0e1se0s1w1nw1"
 6,  2, "road.river_s_n1e0se0s1w1nw1"
 6,  3, "road.river_s_n1e1se0s0w1nw1"
 7,  0, "road.river_s_n0e0se0s0w0nw1"
 7,  1, "road.river_s_n1e0se0s1w0nw1"
 7,  2, "road.river_s_n0e1se0s0w1nw1"
 7,  3, "road.river_s_n1e1se0s1w1nw1"

 8,  0, "road.river_s_n1e0se1s0w0nw0"
 8,  1, "road.river_s_n0e1se1s0w0nw0"
 8,  2, "road.river_s_n0e0se1s1w0nw0"
 8,  3, "road.river_s_n0e0se1s0w1nw0"
 9,  0, "road.river_s_n1e1se1s0w0nw0"
 9,  1, "road.river_s_n0e1se1s1w0nw0"
 9,  2, "road.river_s_n0e0se1s1w1nw0"
 9,  3, "road.river_s_n1e0se1s0w1nw0"
10,  0, "road.river_s_n1e1se1s1w0nw0"
10,  1, "road.river_s_n0e1se1s1w1nw0"
10,  2, "road.river_s_n1e0se1s1w1nw0"
10,  3, "road.river_s_n1e1se1s0w1nw0"
11,  0, "road.river_s_n0e0se1s0w0nw0"
11,  1, "road.river_s_n1e0se1s1w0nw0"
11,  2, "road.river_s_n0e1se1s0w1nw0"
11,  3, "road.river_s_n1e1se1s1w1nw0"

12,  0, "road.river_s_n1e0se1s0w0nw1"
12,  1, "road.river_s_n0e1se1s0w0nw1"
12,  2, "road.river_s_n0e0se1s1w0nw1"
12,  3, "road.river_s_n0e0se1s0w1nw1"
13,  0, "road.river_s_n1e1se1s0w0nw1"
13,  1, "road.river_s_n0e1se1s1w0nw1"
13,  2, "road.river_s_n0e0se1s1w1nw1"
13,  3, "road.river_s_n1e0se1s0w1nw1"
14,  0, "road.river_s_n1e1se1s1w0nw1"
14,  1, "road.river_s_n0e1se1s1w1nw1"
14,  2, "road.river_s_n1e0se1s1w1nw1"
14,  3, "road.river_s_n1e1se1s0w1nw1"
15,  0, "road.river_s_n0e0se1s0w0nw1"
15,  1, "road.river_s_n1e0se1s1w0nw1"
15,  2, "road.river_s_n0e1se1s0w1nw1"
15,  3, "road.river_s_n1e1se1s1w1nw1"

;river outlets

 0, 4, "road.river_outlet_w"
 0, 5, "road.river_outlet_n"
 1, 4, "road.river_outlet_s"
 1, 5, "road.river_outlet_e"
 2, 4, "road.river_outlet_se"
 3, 4, "road.river_outlet_nw"

 }
