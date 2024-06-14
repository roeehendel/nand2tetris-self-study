// push constant 17

@17
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 17

@17
D=A
@SP
A=M
M=D


@SP
M=M+1


// eq

@SP
M=M-1
A=M
D=M
@SP
A=M-1

D=M-D
@TRUE_4258204798
D;JEQ

@SP
A=M-1
M=0
@END_4258204798
0;JMP
(TRUE_4258204798)
@SP
A=M-1
M=-1
(END_4258204798)


// push constant 17

@17
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 16

@16
D=A
@SP
A=M
M=D


@SP
M=M+1


// eq

@SP
M=M-1
A=M
D=M
@SP
A=M-1

D=M-D
@TRUE_9274724217
D;JEQ

@SP
A=M-1
M=0
@END_9274724217
0;JMP
(TRUE_9274724217)
@SP
A=M-1
M=-1
(END_9274724217)


// push constant 16

@16
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 17

@17
D=A
@SP
A=M
M=D


@SP
M=M+1


// eq

@SP
M=M-1
A=M
D=M
@SP
A=M-1

D=M-D
@TRUE_4892990835
D;JEQ

@SP
A=M-1
M=0
@END_4892990835
0;JMP
(TRUE_4892990835)
@SP
A=M-1
M=-1
(END_4892990835)


// push constant 892

@892
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 891

@891
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
@TRUE_8871745715
D;JLT

@SP
A=M-1
M=0
@END_8871745715
0;JMP
(TRUE_8871745715)
@SP
A=M-1
M=-1
(END_8871745715)


// push constant 891

@891
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 892

@892
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
@TRUE_6390920598
D;JLT

@SP
A=M-1
M=0
@END_6390920598
0;JMP
(TRUE_6390920598)
@SP
A=M-1
M=-1
(END_6390920598)


// push constant 891

@891
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 891

@891
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
@TRUE_4072691156
D;JLT

@SP
A=M-1
M=0
@END_4072691156
0;JMP
(TRUE_4072691156)
@SP
A=M-1
M=-1
(END_4072691156)


// push constant 32767

@32767
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 32766

@32766
D=A
@SP
A=M
M=D


@SP
M=M+1


// gt

@SP
M=M-1
A=M
D=M
@SP
A=M-1

D=M-D
@TRUE_7825562752
D;JGT

@SP
A=M-1
M=0
@END_7825562752
0;JMP
(TRUE_7825562752)
@SP
A=M-1
M=-1
(END_7825562752)


// push constant 32766

@32766
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 32767

@32767
D=A
@SP
A=M
M=D


@SP
M=M+1


// gt

@SP
M=M-1
A=M
D=M
@SP
A=M-1

D=M-D
@TRUE_2526999511
D;JGT

@SP
A=M-1
M=0
@END_2526999511
0;JMP
(TRUE_2526999511)
@SP
A=M-1
M=-1
(END_2526999511)


// push constant 32766

@32766
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 32766

@32766
D=A
@SP
A=M
M=D


@SP
M=M+1


// gt

@SP
M=M-1
A=M
D=M
@SP
A=M-1

D=M-D
@TRUE_8511612146
D;JGT

@SP
A=M-1
M=0
@END_8511612146
0;JMP
(TRUE_8511612146)
@SP
A=M-1
M=-1
(END_8511612146)


// push constant 57

@57
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 31

@31
D=A
@SP
A=M
M=D


@SP
M=M+1


// push constant 53

@53
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

// push constant 112

@112
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

// neg

@SP
A=M-1

M=-M

// and

@SP
M=M-1
A=M
D=M
@SP
A=M-1

M=D&M

// push constant 82

@82
D=A
@SP
A=M
M=D


@SP
M=M+1


// or

@SP
M=M-1
A=M
D=M
@SP
A=M-1

M=D|M

// not

@SP
A=M-1

M=!M

