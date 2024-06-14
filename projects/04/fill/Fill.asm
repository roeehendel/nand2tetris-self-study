// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// while True:
//   if KBD != 0:
//     make_screen_black()
//   else:
//     make_screen_white()
//


@SCREEN
D=A

@8192
D=D+A

@final
M=D

@last
M=0

(LOOP)
	@KBD
	D=M

	@current
	M=D

	@last
	D=D-M

	@CHANGED
	D;JNE

	@LOOP
	0;JMP

(CHANGED)
	@current
	D=M

	@last
	M=D

	@BLACK
	D;JNE

	@WHITE
	0;JMP

(BLACK)
	@color
	M=-1

	@DRAW
	0;JMP

(WHITE)
	@color
	M=0

	@DRAW
	0;JMP

(DRAW)
	@SCREEN
	D=A

	@position
	M=D

	@DRAWLOOP
	0;JMP

(DRAWLOOP)
	@position
	D=M

	@final
	D=D-M

	@LOOP
	D;JGE

	@color
	D=M

	// ---------

	//@position
	//A=M
	//M=D

	//// position = position+1
	//@position
	//M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1
	
	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1
	
	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	@position
	A=M
	M=D
	@position
	M=M+1

	// --------

	@DRAWLOOP
	0;JMP