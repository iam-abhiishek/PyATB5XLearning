class OldBrowser:

    def start_browser(self):
        print("browser is starting")

    def stop_browser(self):
        print("browser is stopping")

class NewBrowser(OldBrowser):
    def start_browser(self):
        super().start_browser()   # parent start browser
        print("new browser is starting")

    def stop_browser(self):
        print("new browser is stopping")

obj_ref = NewBrowser()
obj_ref.start_browser()
obj_ref.stop_browser()