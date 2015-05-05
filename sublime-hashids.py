import sublime, sublime_plugin, re
from .hashids.hashids import Hashids

class HashidsAddSettingsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        project_data = sublime.active_window().project_data()

        if project_data == None:
            sublime.status_message("Hashids: Missing project data (project not saved?)")
            return

        if not project_data.get('settings',{}).get("hashids"):
            if not project_data.get('settings'):
                project_data['settings'] = {}

            project_data['settings']["hashids"] = {}

            sublime.active_window().set_project_data(project_data)

        # Don't override confiuration
        else:
            sublime.status_message("Hashids: Configuration already exists")

        # Open configuration in new tab
        sublime.active_window().run_command("open_file",  {"file": "${project}"})


class HashidsEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        view = sublime.active_window().active_view()
        selection = view.sel()
        empty = True

        for region in selection:
            if not region.empty():
                empty = False
                encoded = _encode(view.substr(region))

                if not encoded:
                    sublime.status_message("Hashids: invalid syntax: " + view.substr(region))
                    return

                view.replace(edit, region, encoded)

        if empty:
            sublime.active_window().show_input_panel("Ids to encode", "", _insert_encoded, None, None )
            return

class HashidsDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        view = sublime.active_window().active_view()
        selection = view.sel()
        empty = True

        for region in selection:
            if not region.empty():
                empty = False
                decoded = _decode(view.substr(region))

                if not decoded:
                    sublime.status_message("Hashids: invalid hash: " + view.substr(region))
                    return

                view.replace(edit, region, ",".join(str(i) for i in decoded))


        if empty:
            sublime.active_window().show_input_panel("Hash to decode", "", _insert_decoded, None, None )
            return

def _encode(ids):
    settings = sublime.active_window().active_view().settings().get("hashids", {})
    ids = [int(i) for i in re.compile('(?:(\d+)[,\s]*)',re.I).findall(ids)]

    if not ids:
        return None

    hashids = Hashids(salt=settings["salt"])
    return hashids.encode(*ids)

def _insert_encoded(ids):
    encoded = _encode(ids)
    view = sublime.active_window().active_view()

    view.run_command("insert", {"characters": encoded})

def _decode(encoded):
    settings = sublime.active_window().active_view().settings().get("hashids", {})

    hashids = Hashids(salt=settings["salt"])
    return hashids.decode(encoded)

def _insert_decoded(encoded):
    decoded = _decode(encoded)
    view = sublime.active_window().active_view()

    view.run_command("insert", {"characters": ",".join(str(i) for i in decoded)})
