// DarkCat v5 ESLint config for MyWebApp
export default [
  {
    files: ["*.js", "*.mjs"],
    languageOptions: {
      ecmaVersion: 2023,
      sourceType: "module"
    },
    rules: {
      "semi": ["error", "always"],
      "quotes": ["error", "double"],
      "no-unused-vars": ["warn"],
      "no-console": ["off"]
    }
  },
  {
    files: ["*.ts"],
    languageOptions: {
      ecmaVersion: 2023,
      sourceType: "module"
    },
    rules: {
      "semi": ["error", "always"],
      "quotes": ["error", "double"],
      "@typescript-eslint/no-unused-vars": ["warn"]
    },
    plugins: {
      "@typescript-eslint": require("@typescript-eslint/eslint-plugin")
    }
  }
];
