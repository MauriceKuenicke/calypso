<template>
    <v-card class="login__card px-6 py-8 card-max-width">
        <v-form v-model="form" @submit.prevent="onSubmit">
            <v-text-field v-model="email" :readonly="loading" :rules="[required]" class="mb-2" clearable
                label="User"></v-text-field>

            <v-text-field v-model="password" type="password" :readonly="loading" :rules="[required]" clearable
                label="Password" placeholder="Enter your password"></v-text-field>

            <br>

            <v-btn :disabled="!form" :loading="loading" block color="primary" size="large" variant="elevated" type="submit">
                Sign In
            </v-btn>
            <v-btn @click="test">
                Backend Check
            </v-btn>
        </v-form>
    </v-card>
</template>

<script setup lang="ts">
import axios from 'axios'

const form = ref<boolean>(false)
const loading = ref<boolean>(false)
const email = ref<String | null>(null)
const password = ref<String | null>(null)

async function test() {
    console.log(await axios.get('/api/healthcheck'))
}

function onSubmit() {
    if (!form.value) return

    loading.value = true

    setTimeout(() => (loading.value = false), 2000)
}

function required(v: any) {
    return !!v || 'Field is required'
}
</script>

<style scoped>
.login__card {
    margin: auto;
    margin-top: 30vh;
    background: rgba(0, 0, 0, 0.1);
}

.card-max-width {
    max-width: 344px;
}
</style>