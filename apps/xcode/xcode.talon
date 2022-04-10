app: xcode
-
tag(): user.find_and_replace
tag(): user.line_commands

follow: user.follow()
go back: user.go_back()
go forward: user.go_forward()
go <number> start: user.go_line_start(number)
go <number>: user.go_line_end(number)
fix formatting: user.fix_formatting()
