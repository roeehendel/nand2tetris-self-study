// INIT CODE
// SP=256
@256
D=A
@SP
M=D
// push return-address
@None$ret0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(None$ret0)

// function Main.fibonacci 0
(Main.fibonacci)

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

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@TRUE_6970623368
D;JLT
@SP
A=M-1
M=0
@END_6970623368
0;JMP
(TRUE_6970623368)
@SP
A=M-1
M=-1
(END_6970623368)

// if-goto IF_TRUE
@SP
M=M-1
@SP
A=M
D=M
@Main.fibonacci:IF_TRUE
D;JNE

// goto IF_FALSE
@Main.fibonacci:IF_FALSE
0;JMP

// label IF_TRUE
(Main.fibonacci:IF_TRUE)

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

// label IF_FALSE
(Main.fibonacci:IF_FALSE)

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

// push constant 2
@2
D=A
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

// call Main.fibonacci 1
// push return-address
@Main.fibonacci$ret1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret1)

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

// push constant 1
@1
D=A
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

// call Main.fibonacci 1
// push return-address
@Main.fibonacci$ret2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret2)

// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M

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

// function Sys.init 0
(Sys.init)

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.fibonacci 1
// push return-address
@Sys.init$ret3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Sys.init$ret3)

// label WHILE
(Sys.init:WHILE)

// goto WHILE
@Sys.init:WHILE
0;JMP

