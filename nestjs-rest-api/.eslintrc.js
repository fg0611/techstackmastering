module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2020, // Permite sintaxis ES2020+
    sourceType: 'module',
  },
  plugins: ['@typescript-eslint'],
  extends: [
    'eslint:recommended', // Reglas recomendadas de ESLint
    'plugin:@typescript-eslint/recommended', // Reglas recomendadas para TypeScript
  ],
  rules: {
    // Deshabilitar reglas específicas que no quieres imponer
    'no-console': 'off', // Permite el uso de console.log
    'no-unused-vars': 'off', // No restringe el uso de variables no usadas
    'semi': 'off', // No impone el uso de punto y coma
    'quotes': ['off', 'single'], // No impone tipo de comillas
    '@typescript-eslint/no-explicit-any': 'off', // Permite el uso de 'any'
  },
  ignorePatterns: ['node_modules/', 'dist/'], // Ignorar estas carpetas
};
