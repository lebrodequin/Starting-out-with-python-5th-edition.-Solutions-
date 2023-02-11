length_of_row = float ( input ('input leghth of row, feet: '))
space_end_post = float ( input ('input space used by an end-post assembly, feet: '))
space_btw_vines =float ( input ('input space between, feet: '))

num_of_grapevines = (length_of_row-2*space_end_post)/space_btw_vines

print ('the number of grapevines is', num_of_grapevines)
