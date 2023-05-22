<template>
  <div>
    <NuxtLayout :name="currentLayout">
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
const defaultTitle = 'Maurice Künicke';
onMounted(() => {
  document.title = defaultTitle;
});


const currentLayout: Ref<string> = ref('default')
</script>

<style></style>