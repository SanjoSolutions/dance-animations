import { defineConfig } from 'vite';

export default defineConfig({
  // Relative asset URLs work both locally and under /dance-animations/ on Pages.
  base: './',
  server: { watch: { ignored: ['**/animations/**', '**/models/**', '**/docs/**', '**/scripts/**', '**/.cache/**', '**/*.blend'] } },
  build: {
    chunkSizeWarningLimit: 800,
    rollupOptions: {
      input: {
        library: 'index.html',
        imprint: 'imprint.html',
        privacy: 'privacy.html',
        licenses: 'licenses.html',
      },
    },
  },
});
