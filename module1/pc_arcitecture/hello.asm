org 0x100 ; Indication that this is a .COM application
section .data
    message db 'Hello, World!', '$' ; Specifying a string to output

section .text
_start:
    mov ah, 09h ; DOS function to output a string
    mov dx, message ; Set DX to address string
    int 21h ; DOS interrupt call

    mov ax, 4c00h ; DOS function to terminate the program
    int 21h ; DOS interrupt call
