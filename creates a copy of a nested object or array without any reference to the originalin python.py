const original = { a: 1, b: { c: 2 } };
const copy = structuredClone(original);
copy.b.c = 42;
console.log(original.b.c); // 2 (unchanged)
