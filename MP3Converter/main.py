import dearpygui.dearpygui as dpg
from pytube import YouTube
import os

dpg.create_context()
dpg.create_viewport(title='MP3Converter', width=600, height=500)


def callback(sender, app_data):
    directory = app_data.get('file_path_name')
    link = dpg.get_value('link')
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    
    out_file = audio.download(output_path=directory)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    with dpg.window(label="Sucesso", width=600, height=100, tag="popup"):
        dpg.add_text(f"Arquivo baixado em:{directory}")
        dpg.add_button(label="Fechar", callback=lambda: dpg.delete_item("popup"))
    
dpg.add_file_dialog(height=400, directory_selector=True, show=False, callback=callback, tag="file_dialog_id")
    
with dpg.window(label="Main", width=600, height=500):
    dpg.add_input_text(
        hint="Link do video",
        tag='link')
    dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("file_dialog_id"))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()