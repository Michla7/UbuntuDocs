from gi.repository import Gtk

class MainWindow:
  def __init__(self, widget):
    self.button = GtkButton(text='click')
    self.add(button)
    
  window=MainWindow()
