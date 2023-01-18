export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const int8 = new Int8Array(length);
  int8[position] = value;
  return int8;
}
