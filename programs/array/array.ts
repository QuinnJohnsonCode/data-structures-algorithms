const a = new ArrayBuffer(6);
console.log(a); // Displays as ArrayBuffer { [Uint8Contents]: <00 00 00 00 00 00>, byteLength: 6 }

const a8 = new Uint8Array(a);
a8[0] = 45;
console.log(a); // ArrayBuffer { [Uint8Contents]: <2d 00 00 00 00 00>, byteLength: 6 }

a8[2] = 45;

const a16 = new Uint16Array(a);
a16[2] = 0x4545;
console.log(a); // ArrayBuffer { [Uint8Contents]: <2d 00 2d 00 45 45>, byteLength: 6 }
