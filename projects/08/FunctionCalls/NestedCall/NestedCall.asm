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

// function Sys.init 0
(Sys.init)

// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
M=M-1
@3
D=A
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
M=M-1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// call Sys.main 0
// push return-address
@Sys.init$ret1
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
@Sys.main
0;JMP
(Sys.init$ret1)

// pop temp 1
@SP
M=M-1
@5
D=A
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// label LOOP
(Sys.init:LOOP)

// goto LOOP
@Sys.init:LOOP
0;JMP

// function Sys.main 5
(Sys.main)
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
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
M=M-1
@3
D=A
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
M=M-1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 1
@SP
M=M-1
@LCL
D=M
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 2
@SP
M=M-1
@LCL
D=M
@2
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 3
@SP
M=M-1
@LCL
D=M
@3
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1
// push return-address
@Sys.main$ret2
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
@Sys.add12
0;JMP
(Sys.main$ret2)

// pop temp 0
@SP
M=M-1
@5
D=A
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

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

// push local 2
@LCL
D=M
@2
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 3
@LCL
D=M
@3
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 4
@LCL
D=M
@4
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

// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M

// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M

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

// function Sys.add12 0
(Sys.add12)

// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 0
@SP
M=M-1
@3
D=A
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer 1
@SP
M=M-1
@3
D=A
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D

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

// push constant 12
@12
D=A
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

