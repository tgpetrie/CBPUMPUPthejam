module.exports = {
  darkMode: 'class',
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        bhabit: {
          black: '#000000',
          purple: '#7D00FF',
          orange: '#FF5E00',
          blue: '#00CFFF',
          offwhite: '#E0E0E0',
          gray: '#6E6E6E',
          error: '#FF3B30',
        },
      },
      fontFamily: {
        primary: ['Space Grotesk', 'sans-serif'],
        secondary: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
