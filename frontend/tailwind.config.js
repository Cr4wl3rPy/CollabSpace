/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#1f2937",    // header
        secondary: "#111827",  // sidebar
        background: "#f9fafb", // fondo
      },
      keyframes: {
        rocketFly: {
          '0%, 100%': { transform: 'translateY(0) rotate(0deg)' },
          '25%': { transform: 'translateY(-4px) rotate(5deg)' },
          '50%': { transform: 'translateY(-8px) rotate(15deg)' },
          '75%': { transform: 'translateY(-4px) rotate(5deg)' },
        },
        rocketTrail: {
          '0%, 100%': { opacity: 0 },
          '50%': { opacity: 1 },
        },
      },
      animation: {
        rocketFly: 'rocketFly 0.6s ease-in-out infinite',
        rocketTrail: 'rocketTrail 0.6s ease-in-out infinite',
      },
    },
  },
  plugins: [],
};
