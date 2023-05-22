export default defineNuxtRouteMiddleware((to, from) => {
    const isAuth = false
    if (!isLoginPage(to.path) && !isAuth) {
        return navigateTo("/login")
    }
})


function isLoginPage(path: string): boolean {
    if (path === '/login') {
        return true
    }
    return false
}