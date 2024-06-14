// INIT CODE
// SP=256
@256
D=A
@SP
M=D
@Sys.init
0;JMP

// function SimpleFunction.test 2
(SimpleFunction.test)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push local 0
@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M

// not
@SP
A=M-1
M=!M

// push argument 0
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M

// push argument 1
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=M-D

// return
// FRAME := R13 = LCL
@LCL
D=M
@R13
M=D
// RET := R14 = *(FRAME - 5)
@R13
D=M
@5
A=D-A
D=M
@R14
M=D
// *ARG = pop()
@SP
M=M-1 // SP--
A=M
D=M // D = *SP
@ARG
A=M
M=D // *ARG = D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(FRAME - 1)
@R13
D=M
@1
A=D-A
D=M
@THAT
M=D
// THIS = *(FRAME - 2)
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
// ARG = *(FRAME - 3)
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
// LCL = *(FRAME - 4)
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto RET
@R14
A=M
0;JMP

