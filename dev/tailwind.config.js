// Tailwind derlemesi: npx tailwindcss@3.4.17 -c dev/tailwind.config.js -i dev/in.css -o site/assets/css/tailwind.css --minify
module.exports = {
  content: [__dirname + '/../site/index.html', __dirname + '/../site/assets/js/site.js'],
  theme: { extend: {
    fontFamily: { sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'] },
    colors: { brand: { lime: '#D8F83C', dark: '#111315', sky: '#0284c7', skyLight: '#38bdf8' } }
  } }
};
