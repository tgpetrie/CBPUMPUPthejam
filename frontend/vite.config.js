import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  const port = env.VITE_API_PORT || 5000;

  return {
    plugins: [react()],
    server: {
      proxy: {
        '/api': {
          target: `http://127.0.0.1:${port}`,
          changeOrigin: true,
        },
      },
    },
  };
});