from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# Import KV Builder and import main.kv as the file to reference for this python script.
from kivy.lang import Builder

Builder.load_file('main.kv')

# Setting variables
toggle_countdown = False
counter = 60
default_time = 60

# Default variables
hours = 1
minutes = 0
seconds = 0


class MyGridLayout(Widget):
    # importing global variables into class
    global counter
    global toggle_countdown
    global hours
    global minutes
    global seconds

    # On application start up:
    def on_start(self):
        # Set text
        self.ids.counter.text = str(counter)

        # Bind all the buttons in the .kv file.
        self.root.ids.start_button.bind()
        self.root.ids.update_time_btn.bind()
        self.root.ids.reset_counter_button.bind()

    # Pause clock count
    def stop_interval(self, *args):
        self.function_interval.cancel()

    # Start the count down
    def start_time(self, *args):
        # Call global variables
        global toggle_countdown
        global counter

        # if Count down hasnt started, start count down
        if (toggle_countdown == False):
            self.ids.function_interval = Clock.schedule_interval(self.countdown, 1)
            self.ids.start_button.text = "Pause"
            # Changing button color on press to green
            self.ids['start_button'].background_color = 1, 0, 0, 1
            toggle_countdown = True
            if seconds == 0 and minutes == 0 and hours == 0:
                self.ids.counter_label.text = str("Finished!")
            return toggle_countdown

        # if Count down started, stop count down
        elif toggle_countdown == True:
            self.ids.function_interval.cancel()
            counter = str(self.ids.counter_label.text)
            self.ids.counter_label.text = "Paused " + str(self.ids.counter_label.text)
            self.ids.start_button.text = "Resume"
            # Changing button color on press to red
            self.ids['start_button'].background_color = 0, 1, 0, 1
            toggle_countdown = False
            if seconds == 0 and minutes == 0 and hours == 0:
                self.ids.counter_label.text = str("Finished!")
            return

    def countdown(self, *args):
        # Import global variables
        global hours
        global minutes
        global seconds

        # making sure vars are int
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        # countdown
        if seconds != 0:
            seconds = seconds - 1
        elif seconds == 0 & (minutes != 0 or hours != 0):
            if minutes != 0:
                minutes = minutes - 1
                seconds = 59
            elif minutes == 0 and hours != 0:
                minutes = 59
                seconds = 59
                hours = hours - 1
            else:
                # if minutes = 0 and hours = 0. , finish
                self.ids.counter_label.text = str("Finished!")
                return
        else:
            # if minutes = 0 and hours = 0 and seconds = 0, finish
            self.ids.counter_label.text = str("Finished!")
            return

        # change label text.
        self.ids.counter_label.text = str("Hours: " + str(hours)
                                          + " Minutes: " + str(minutes) + " Seconds: " + str(seconds))

    # Set time
    def txt_set_time(self, *args):
        global counter
        global hours
        global minutes
        global seconds

        hours = 0
        minutes = 0
        seconds = 0

        # Check if input boxes are empty. If not empty than we add the string into the variable.
        if self.ids.counter_input_field_hours.text != "":
            hours = str(self.ids.counter_input_field_hours.text)
        if self.ids.counter_input_field_minutes.text != "":
            minutes = str(self.ids.counter_input_field_minutes.text)
        if self.ids.counter_input_field_seconds.text != "":
            seconds = str(self.ids.counter_input_field_seconds.text)

        # change label text.
        self.ids.counter_label.text = str("Hours: " + str(hours) + " Minutes: " + str(minutes)
                                          + " Seconds: " + str(seconds))

        # Set the counter as the label text. However this isn't used anymore just setting cos...
        # idk if it breaks anything so not touching it anymore
        counter = self.ids.counter_label.text

    #   reset to 1 hr (default)
    def reset_counter_button(self, *args):
        # Call global variables
        global default_time
        global hours
        global minutes
        global seconds
        #   set default
        hours = 1
        minutes = 0
        seconds = 0

        # change label text.
        self.ids.counter_label.text = str("Hours: " + str(hours) + " Minutes: " + str(minutes)
                                          + " Seconds: " + str(seconds))

    # Update my label
    def update_time(self, *args):
        self.root.ids.counter.text = str(int(self.root.ids.counter.text))

# creating the object root for ButtonApp() class
class MyApp(App):
    def build(self):
        return MyGridLayout()


# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.

if __name__ == '__main__':
    MyApp().run()
