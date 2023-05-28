// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css: ['vuetify/lib/styles/main.sass'],
    build: {
        transpile: ['vuetify'],
    },
    ssr: false,

    vite: {
        server: {
            proxy: {
                "^/api": {
                    target: "http://127.0.0.1:8000",
                    ws: false,
                    changeOrigin: true,
                },
            },
        },
    }
})
