from kivy.app import App
from kivy.uix.button import Button


class AURAApp(App):

    def test_microphone(self, instance):
        try:
            from jnius import autoclass

            PythonActivity = autoclass(
                "org.kivy.android.PythonActivity"
            )

            activity = PythonActivity.mActivity

            activity.requestPermissions(
                ["android.permission.RECORD_AUDIO"],
                100
            )

            instance.text = "MIC PERMISSION REQUESTED 🎙️"

        except Exception as e:
            instance.text = "ERROR ❌"
            print("ERROR:", e)

    def build(self):
        button = Button(
            text="TEST MICROPHONE 🎙️",
            font_size=28
        )

        button.bind(
            on_press=self.test_microphone
        )

        return button


AURAApp().run()
