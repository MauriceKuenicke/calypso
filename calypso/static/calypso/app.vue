<template>
  <div>
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
const defaultTitle = 'Calypso Server';
onMounted(() => {
  document.title = defaultTitle;
});

</script>

<style></style>