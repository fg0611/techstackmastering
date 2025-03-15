// @ts-check
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  {
    ignores: ['eslint.config.mjs', 'node_modules/', 'dist/'], // Ignorar estos directorios
  },
  eslint.configs.recommended, // Configuración base recomendada de ESLint
  ...tseslint.configs.recommendedTypeChecked, // Configuración recomendada para TypeScript
  {
    languageOptions: {
      ecmaVersion: 2020, // Permite ES2020+
      sourceType: 'module',
      parserOptions: {
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
  {
    rules: {
      // Regla opcional: Permite el uso de 'any'
      '@typescript-eslint/no-explicit-any': 'off',
      // Regla opcional: Permite el uso de variables no usadas
      '@typescript-eslint/no-unused-vars': 'off',
      // Regla opcional: Permite punto y coma opcional
      'semi': 'off',
    },
  }
);
