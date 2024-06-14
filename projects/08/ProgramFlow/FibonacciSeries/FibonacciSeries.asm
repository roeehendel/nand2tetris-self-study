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

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 0
@SP
M=M-1
@THAT
D=M
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

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 1
@SP
M=M-1
@THAT
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

// pop argument 0
@SP
M=M-1
@ARG
D=M
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

// label MAIN_LOOP_START
(function_name:MAIN_LOOP_START)

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

// if-goto COMPUTE_ELEMENT
@SP
M=M-1
@SP
A=M
D=M
@function_name:COMPUTE_ELEMENT
D;JNE

// goto END_PROGRAM
@function_name:END_PROGRAM
0;JMP

// label COMPUTE_ELEMENT
(function_name:COMPUTE_ELEMENT)

// push that 0
@THAT
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

// push that 1
@THAT
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

// pop that 2
@SP
M=M-1
@THAT
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

// push pointer 1
@3
D=A
@1
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

// add
@SP
M=M-1
A=M
D=M
@SP
A=M-1
M=D+M

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

// pop argument 0
@SP
M=M-1
@ARG
D=M
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

// goto MAIN_LOOP_START
@function_name:MAIN_LOOP_START
0;JMP

// label END_PROGRAM
(function_name:END_PROGRAM)

