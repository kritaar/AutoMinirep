/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    // opcional si usas componentes en JS:
    './**/*.js',
  ],
  theme: { extend: {} },
  plugins: [],
}
