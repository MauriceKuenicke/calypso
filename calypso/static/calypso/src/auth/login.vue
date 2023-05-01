<template>
    <div class="login__wrapper">
        <v-card class="login__card px-6 py-8" max-width="344">
            <v-form v-model="form" @submit.prevent="onSubmit">
                <v-text-field v-model="email" :readonly="loading" :rules="[required]" class="mb-2" clearable
                    label="User"></v-text-field>

                <v-text-field v-model="password" type="password" :readonly="loading" :rules="[required]" clearable
                    label="Password" placeholder="Enter your password"></v-text-field>

                <br>

                <v-btn :disabled="!form" :loading="loading" block color="primary" size="large" type="submit"
                    variant="elevated">
                    Sign In
                </v-btn>
            </v-form>
        </v-card>
    </div>
</template>
  
<script>
export default {
    name: "LoginPage",
    data: () => ({
        form: false,
        email: null,
        password: null,
        loading: false,
    }),

    methods: {
        onSubmit() {
            if (!this.form) return

            this.loading = true

            setTimeout(() => (this.loading = false), 2000)
        },
        required(v) {
            return !!v || 'Field is required'
        },
    },
}
</script>
<style scoped>
.login__wrapper {
    position: fixed;
    width: 100%;
    height: 100%;
}

.login__card {
    margin: auto;
    margin-top: 30vh;
    background: rgba(0,0,0,0.1);
}
</style>