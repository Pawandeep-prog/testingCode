import streamlit as st
from bokeh.models.widgets import Button, TextInput, Slider
from bokeh.models import CustomJS
from bokeh.events import ButtonClick
from streamlit_bokeh_events import streamlit_bokeh_events

tts_button = Button(label="playing", width=100)

tts_button.js_on_event(ButtonClick, CustomJS(code=f"""
    var u = new SpeechSynthesisUtterance();
    u.text = "button triggered";
    u.lang = 'en-US';

    speechSynthesis.speak(u);
    console.log("logged here");
    """))
st.bokeh_chart(tts_button)

slider = Slider(start=0.1, end=4, value=1, step=.1, title="power")
slider.js_on_change('value',CustomJS(code=f"""
    var u = new SpeechSynthesisUtterance();
    u.text = "button triggered";
    u.lang = 'en-US';

    speechSynthesis.speak(u);
    """))

st.bokeh_chart(slider)


stt_button = Button(label="Speak", width=100)

x = ""

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            console.log(value);
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

print(result)
if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))

