import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Smart Mistake Notebook',
        short_name: 'SMN',
        start_url: '/',
        display: 'standalone',
        background_color: '#ffffff',
        icons: [
          {
            src:
              'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxOTIgMTkyIj48cmVjdCB3aWR0aD0iMTkyIiBoZWlnaHQ9IjE5MiIgcng9IjI0IiBmaWxsPSIjMDk2OWZmIi8+PHRleHQgeD0iOTYiIHk9IjExMiIgZm9udC1zaXplPSI5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0id2hpdGUiPlM8L3RleHQ+PC9zdmc+',
            sizes: '192x192',
            type: 'image/svg+xml'
          },
          {
            src:
              'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cmVjdCB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgcng9IjY0IiBmaWxsPSIjMDk2OWZmIi8+PHRleHQgeD0iMjU2IiB5PSIzMjAiIGZvbnQtc2l6ZT0iMjU2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSJ3aGl0ZSI+UzwvdGV4dD48L3N2Zz4=',
            sizes: '512x512',
            type: 'image/svg+xml'
          }
        ]
      }
    })
  ]
})
