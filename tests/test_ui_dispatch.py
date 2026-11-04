"""Initialized-app regression: posted work reaches Tk without its fallback timer."""

import threading
import unittest
from unittest.mock import Mock, patch

import capture as application


class DispatchTests(unittest.TestCase):
    def test_quit_keeps_gui_running_until_pending_hotkey_callback_returns(self):
        with (
            patch.object(application.settings, "load", return_value={}),
            patch.object(application.pystray, "Icon", return_value=Mock()),
        ):
            app = application.App()
        entering = threading.Event()

        def producer():
            entering.set()
            app.root.after(0, lambda: None)

        thread = threading.Thread(target=producer)
        app.menu_hotkey = Mock(thread=thread)

        def begin():
            thread.start()
            self.assertTrue(entering.wait(1))
            app.quit()

        try:
            app.root.after(0, begin)
            timeout = app.root.after(2000, app.root.quit)
            app.root.mainloop()
            app.root.after_cancel(timeout)
            thread.join(0.5)
            self.assertFalse(thread.is_alive())
            app.menu_hotkey.request_stop.assert_called_once()
        finally:
            app.root.destroy()

    def test_initialized_app_dispatches_worker_post_on_gui_thread(self):
        with (
            patch.object(application.settings, "load", return_value={}),
            patch.object(application.pystray, "Icon", return_value=Mock()),
        ):
            app = application.App()
        gui_thread = threading.get_ident()
        calls = []
        returned = threading.Event()

        def action():
            calls.append(threading.get_ident())
            app.root.quit()

        def worker():
            app.post(action)
            returned.set()

        thread = threading.Thread(target=worker)
        try:
            app.root.after(0, thread.start)
            timeout = app.root.after(2000, app.root.quit)
            app.root.mainloop()
            app.root.after_cancel(timeout)
            self.assertEqual(calls, [gui_thread])
            self.assertTrue(returned.wait(0.5))
        finally:
            app.root.destroy()
            thread.join(2)
