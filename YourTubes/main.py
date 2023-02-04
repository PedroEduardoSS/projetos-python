import dearpygui.dearpygui as dpg
import pytube

dpg.create_context()
dpg.create_viewport(title='YourTubes', width=600, height=200)

def callback():
    link = dpg.get_value("link")
    video_download = pytube.YouTube(link)
    video_download.streams.first().download()

with dpg.window(label="YourTubes", width=600, height=200):
    dpg.add_input_text(default_value="https://youtu.be/********", label="Link do video", tag="link")
    dpg.add_button(label="Download", callback=callback)
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()