// Learning and testing the D language

// Imports
import std.stdio;

void main() {
	// Print "Hello World!"
	writeln("Hello World!\n");

	// Variables which will never be changed
	immutable inchPerFoot = 12;
	immutable cmPerInch = 2.54;

	// Loop through 5-7 feet, and for each inch it will convert to centimetres
	foreach (feet; 5 .. 7) {
		foreach (inches; 0 .. inchPerFoot) {
			writeln (feet, "'", inches, "\"\t", (feet * inchPerFoot + inches) * cmPerInch);
		}
	}
}

