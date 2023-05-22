import { defineNuxtPlugin } from "#app";
import { createVuetify } from 'vuetify'
import "@mdi/font/css/materialdesignicons.css";
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

export default defineNuxtPlugin(nuxtApp => {
    const vuetify = createVuetify({
        theme: {
            defaultTheme: 'darkTheme',
            themes: {
                darkTheme: {
                    dark: true,
                    colors: {
                        background: '#121212',
                        font: '#ffffff',
                        primary: '#C89B3C',
                        layer: '#ffffff'
                    }
                }
            }
        },
        ssr: false,
        components,
        directives,
    })

    nuxtApp.vueApp.use(vuetify)
})