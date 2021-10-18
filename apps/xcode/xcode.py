from talon import Context, actions, ui, Module, app, clip

ctx = Context()
mod = Module()
mod.apps.xcode = """
os: mac
and app.bundle: com.apple.dt.Xcode
"""

ctx.matches = r"""
app: xcode
"""

@ctx.action_class("win")
class WinActions:
    def filename():
        title = actions.win.title()
        result = title.split(" — ")[0]

        print("file name id {}".format(result))

        if "." in result:
            return result

        return ""
