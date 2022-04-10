from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.swift
mode: user.auto_lang
and code.language: swift
"""

@ctx.action_class("user")
class UserActions:
    def code_is_not_null():
        actions.auto_insert(" != nil")

    def code_is_null():
        actions.auto_insert(" == nil")

    def code_state_if():
        actions.insert("if ()")
        actions.key("left")

    def code_state_else_if():
        actions.insert(" else if ()")
        actions.key("left")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()
    
    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private func {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_default_function(text: str):
        """Inserts function declaration"""
        result = "func {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

@mod.action_class
class LanguageActions:
    def create_body():
        """Create and enter body"""
        actions.insert(r" {}")
        actions.key("left")
        actions.key("enter")
