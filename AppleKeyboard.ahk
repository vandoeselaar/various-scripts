#Requires AutoHotkey v2.0

; Cmd (⌘) op een Apple-toetsenbord wordt herkend als de Win-toets in Windows.
; We remappen de linker en rechter Win-toets naar Ctrl.

LWin & c::Send "^c"   ; Cmd + C wordt Ctrl + C
LWin & v::Send "^v"   ; Cmd + V wordt Ctrl + V
LWin & x::Send "^x"   ; Cmd + X wordt Ctrl + X
LWin & a::Send "^a"   ; Cmd + A wordt Ctrl + A
LWin & z::Send "^z"   ; Cmd + Z wordt Ctrl + Z
LWin & y::Send "^y"   ; Cmd + Y wordt Ctrl + Y
LWin & t::Send "^t"   ; Cmd + T opent een nieuw tabblad in een browser
LWin & w::Send "^w"   ; Cmd + W sluit een tabblad

; Cmd + Tab omzetten naar Alt + Tab
LWin & Tab::Send "{Alt down}{Tab}{Alt up}"

; Optioneel: Cmd + Q kan Alt + F4 worden (programma sluiten)
LWin & q::Send "!{F4}"
