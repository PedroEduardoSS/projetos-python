from gtts import gTTS
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='TextToSpeechApp', width=600, height=600)

def salvar():
    text = dpg.get_value('texto')
    tts = gTTS(text, lang='pt', tld='com.br')
    tts.save('output.mp3')

with dpg.window(label="Main", width=600, height=600):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Salvar", callback=salvar)
    dpg.add_input_text(
        hint="Digite algo...",
        width=500,
        height=500,
        multiline=True,
        tag='texto')

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()