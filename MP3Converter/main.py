import dearpygui.dearpygui as dpg
from pytube import YouTube
import os

dpg.create_context()
dpg.create_viewport(title='MP3Converter', width=400, height=200)

def salvar():
    link = dpg.get_value('link')
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    
    #destination
    out_file = audio.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
with dpg.window(label="Main", width=400, height=200):
    dpg.add_input_text(
        hint="Link do video",
        tag='link')
    dpg.add_button(label="Salve", callback=salvar)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()