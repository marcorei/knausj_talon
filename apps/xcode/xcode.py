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

@mod.action_class
class ApplicationActions:
    def follow():
        """Go to declaration"""
        actions.key('ctrl-cmd-j')
    def go_back():
        """Go back"""
        actions.key('ctrl-cmd-left')
    def go_forward():
        """Go forward"""
        actions.key('ctrl-cmd-right')
    def go_line_start(line: str):
        """Go to start of line number"""
        actions.key('cmd-l')
        actions.insert(line)
        actions.key('enter')
        actions.sleep('200ms')
        actions.key('cmd-left')
    def go_line_end(line: str):
        """Go to end of line number"""
        actions.key('cmd-l')
        actions.insert(line)
        actions.key('enter')
    def fix_formatting():
        """Format file contents"""
        actions.key('cmd-a')
        actions.key('ctrl-i')

