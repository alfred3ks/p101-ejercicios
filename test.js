/*
Aquí te presento un programa en JavaScript que muestra todas las tripletas de números diferentes entre sí que suman 15, utilizando un enfoque de fuerza bruta:
*/
for (let i = 1; i <= 9; i++) {
  for (let j = i + 1; j <= 9; j++) {
    for (let k = j + 1; k <= 9; k++) {
      if (i + j + k === 15) {
        console.log(`${i}, ${j}, ${k}`);
      }
    }
  }
}
