<script setup>
import LoginPage from './auth/login.vue'
</script>

<template>
  <v-app>
    <v-main>
      <LoginPage />
    </v-main>
  </v-app>
</template>

<style>
* {
  margin: 0 0 0 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Roboto' 'Arial';
}
</style>
