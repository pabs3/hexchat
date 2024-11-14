import gdb

class BP (gdb.Breakpoint):
  def stop (self):
    frame = gdb.newest_frame()
    caller = frame.older()
    caller = f'{caller.find_sal().symtab.filename}:{caller.find_sal().line} {caller.function().print_name}'
    block = frame.block()
    for var in block.superblock:
      print(caller, var, var.value(frame)['channel'])
    for var in block:
      print(caller, var, var.value(frame))
    return False

b = BP('src/fe-gtk/maingui.c:248')
#printf "cur_sess %s, sess %s, pref %d, cur %d, active %d, current %d, sf %d\n", cur_sess->channel, sess->channel, prefs.hex_text_scroll_follow, sess == cur_sess, active, current, scroll_follow
