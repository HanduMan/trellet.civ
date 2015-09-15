
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
	HanduMan <HanduMan@savageclub.org>
"

[file]
gfx = "a2phex/grid"

[grid_main]

x_top_left = 42
y_top_left = 99
dx = 128
dy = 34
pixel_border = 1

tiles = { "row", "column", "tag"
  0, 0, "grid.main.we"
  1, 0, "grid.main.ns"
  2, 0, "grid.main.ud"

  0, 1, "grid.city.we"
  1, 1, "grid.city.ns"
  2, 1, "grid.city.ud"

  0, 2, "grid.worked.we"
  1, 2, "grid.worked.ns"
  2, 2, "grid.worked.ud"

  0, 3, "grid.selected.we"
  1, 3, "grid.selected.ns"
  2, 3, "grid.selected.ud"

  0, 4, "grid.coastline.we"
  1, 4, "grid.coastline.ns"
  2, 4, "grid.coastline.ud"

  0, 6, "grid.unavailable"

  3, 0, "grid.borders.n"
  3, 1, "grid.borders.s"
  3, 2, "grid.borders.w"
  3, 3, "grid.borders.e"
  3, 4, "grid.borders.u"
  3, 5, "grid.borders.d"
  
  0, 7, "unit.select0"
  0, 8, "unit.select1"
  1, 7, "unit.select2"
  1, 8, "unit.select3"

  2, 6, "user.attention"
  }
