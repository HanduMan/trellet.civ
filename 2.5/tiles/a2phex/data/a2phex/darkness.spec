[info]
general = "
	darkness.png	contains images for each different 'encroaching darkness' overlay based 
					on whether the adjacent tiles are known or unknown
	darkness.spec	gives the coordinates to those images
	"
copyright = "
	Copyright 2008, 2009 HanduMan for hex conversion
	see Amplio files for copyrights of original Amplio tileset
	"
copying = "
    This file is part of a-phex, a Freeciv tileset.

    a-phex is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    a-phex is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Freeciv. You should be able to find it in data/COPYING.
	If not, see <http://www.gnu.org/licenses/>.
	"

artists = "
	HanduMan <HanduMan@savageclub.org>
	"

[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
	HanduMan <HanduMan@savageclub.org>
	"

[file]
gfx = "a2phex/darkness"

[grid_main]

x_top_left = 31
y_top_left = 8
dx = 128
dy = 34
pixel_border = 8

tiles = { "row", "column","tag"
 
; Basic fog
 0,  5, "tx.fog" ; Use with fogstyle = 0, recommended for GTK client
;1,  5, "tx.fog" ; Use with fogstyle = 1, recommended for SDL client

 ; Whether north, south, east, west, SE, NW is unknown

 0,  0, "tx.darkness_n1e0se0s0w0nw0"
 0,  1, "tx.darkness_n0e1se0s0w0nw0"
 0,  2, "tx.darkness_n0e0se0s1w0nw0"
 0,  3, "tx.darkness_n0e0se0s0w1nw0"
 1,  0, "tx.darkness_n1e1se0s0w0nw0"
 1,  1, "tx.darkness_n0e1se0s1w0nw0"
 1,  2, "tx.darkness_n0e0se0s1w1nw0"
 1,  3, "tx.darkness_n1e0se0s0w1nw0"
 2,  0, "tx.darkness_n1e1se0s1w0nw0"
 2,  1, "tx.darkness_n0e1se0s1w1nw0"
 2,  2, "tx.darkness_n1e0se0s1w1nw0"
 2,  3, "tx.darkness_n1e1se0s0w1nw0"
 3,  0, "tx.darkness_n0e0se0s0w0nw0"
 3,  1, "tx.darkness_n1e0se0s1w0nw0"
 3,  2, "tx.darkness_n0e1se0s0w1nw0"
 3,  3, "tx.darkness_n1e1se0s1w1nw0"

 4,  0, "tx.darkness_n1e0se0s0w0nw1"
 4,  1, "tx.darkness_n0e1se0s0w0nw1"
 4,  2, "tx.darkness_n0e0se0s1w0nw1"
 4,  3, "tx.darkness_n0e0se0s0w1nw1"
 5,  0, "tx.darkness_n1e1se0s0w0nw1"
 5,  1, "tx.darkness_n0e1se0s1w0nw1"
 5,  2, "tx.darkness_n0e0se0s1w1nw1"
 5,  3, "tx.darkness_n1e0se0s0w1nw1"
 6,  0, "tx.darkness_n1e1se0s1w0nw1"
 6,  1, "tx.darkness_n0e1se0s1w1nw1"
 6,  2, "tx.darkness_n1e0se0s1w1nw1"
 6,  3, "tx.darkness_n1e1se0s0w1nw1"
 7,  0, "tx.darkness_n0e0se0s0w0nw1"
 7,  1, "tx.darkness_n1e0se0s1w0nw1"
 7,  2, "tx.darkness_n0e1se0s0w1nw1"
 7,  3, "tx.darkness_n1e1se0s1w1nw1"

 8,  0, "tx.darkness_n1e0se1s0w0nw0"
 8,  1, "tx.darkness_n0e1se1s0w0nw0"
 8,  2, "tx.darkness_n0e0se1s1w0nw0"
 8,  3, "tx.darkness_n0e0se1s0w1nw0"
 9,  0, "tx.darkness_n1e1se1s0w0nw0"
 9,  1, "tx.darkness_n0e1se1s1w0nw0"
 9,  2, "tx.darkness_n0e0se1s1w1nw0"
 9,  3, "tx.darkness_n1e0se1s0w1nw0"
10,  0, "tx.darkness_n1e1se1s1w0nw0"
10,  1, "tx.darkness_n0e1se1s1w1nw0"
10,  2, "tx.darkness_n1e0se1s1w1nw0"
10,  3, "tx.darkness_n1e1se1s0w1nw0"
11,  0, "tx.darkness_n0e0se1s0w0nw0"
11,  1, "tx.darkness_n1e0se1s1w0nw0"
11,  2, "tx.darkness_n0e1se1s0w1nw0"
11,  3, "tx.darkness_n1e1se1s1w1nw0"

12,  0, "tx.darkness_n1e0se1s0w0nw1"
12,  1, "tx.darkness_n0e1se1s0w0nw1"
12,  2, "tx.darkness_n0e0se1s1w0nw1"
12,  3, "tx.darkness_n0e0se1s0w1nw1"
13,  0, "tx.darkness_n1e1se1s0w0nw1"
13,  1, "tx.darkness_n0e1se1s1w0nw1"
13,  2, "tx.darkness_n0e0se1s1w1nw1"
13,  3, "tx.darkness_n1e0se1s0w1nw1"
14,  0, "tx.darkness_n1e1se1s1w0nw1"
14,  1, "tx.darkness_n0e1se1s1w1nw1"
14,  2, "tx.darkness_n1e0se1s1w1nw1"
14,  3, "tx.darkness_n1e1se1s0w1nw1"
15,  0, "tx.darkness_n0e0se1s0w0nw1"
15,  1, "tx.darkness_n1e0se1s1w0nw1"
15,  2, "tx.darkness_n0e1se1s0w1nw1"
15,  3, "tx.darkness_n1e1se1s1w1nw1"
}
