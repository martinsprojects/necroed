# keybindings:

# f1       = show helpfile # DONE!
# f2       = hide menu
# f3       = colorpicker
# f4       = show keybindings
# f5       = show theme
# f9       = run program

# ctrl + n = new
# ctrl + s = save
# ctrl + p = save as
# ctrl + o = open
# ctrl + w = run
# ctrl + d = find
# ctrl + f = find next
# ctrl + e = replace
# ctrl + r = replace next
# ctrl + g = goto
# ctrl + q = exit

root.bind("<F1>", f_show_help)
# root.bind("<F2>", e_hide_menu)
root.bind("<F3>", e_color_picker)
root.bind("<F4>", f_show_keybindings)
root.bind("<F5>",e_color_theme)		
#root.bind("<F9>", run_files)
root.bind("<Control_L><n>", e_new_files)
root.bind("<Control_L><o>", e_open_files)
root.bind("<Control_L><s>", e_save_files)
root.bind("<Control_L><p>", e_save_files_as)
root.bind("<Control_L><d>", e_find_text)