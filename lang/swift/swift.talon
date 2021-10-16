mode: command
and mode: user.swift
mode: command
and mode: user.auto_lang
and code.language: swift
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic

settings():
    user.code_private_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_private_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_public_variable_formatter = "PRIVATE_CAMEL_CASE"

state var: "var "
state let: "let "
state if let: "if let "
state guard let: "guard let "

^funk <user.text>$: user.code_default_function(text)
^private funk <user.text>$: user.code_private_function(text)
