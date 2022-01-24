
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
import streamlit.components.v1 as comp

text = st.text_input("Say what ?")

tts_button = Button(label="Speak", width=100)


tts_button.js_on_event("button_click", CustomJS(code=f"""
    var u = new SpeechSynthesisUtterance();
    u.text = "button triggered";
    u.lang = 'en-US';

    speechSynthesis.speak(u);

    alert("button click");
    """))

st.bokeh_chart(tts_button)



x = "hello"

print("spekaing")
comp.html(
    f"""
    <script>
    var u = new SpeechSynthesisUtterance();
    u.text = "{x};
    u.lang = 'en-US';

    speechSynthesis.speak(u);
    </script>
    """
)

